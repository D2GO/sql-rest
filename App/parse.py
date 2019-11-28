from sqlalchemy import text
import json


# 得到根据传入的特殊参数拼接出sql模板
def get_sql_q(schema_, table_, parser, paras):
    table = schema_+'.'+table_
    args = parser.parse_args()
    wheres = []
    for i in paras:
        if i not in args.keys():
            wheres.append((i, paras[i]))
    if args['_join']:
        j = get_join(args['_join'])
        table = table+j['join']+schema_+'.'+j['t2']+' on '+j['t1f']+j['eq']+j['t2f']
    if args['_count']:
        sql_q = "SELECT COUNT("+args['_count']+") FROM " + table
    elif args['_select']:
        sql_q = "SELECT "+args['_select']+" FROM " + table
    else:
        sql_q = "SELECT * FROM " + table
    if wheres != []:
        for i, j in enumerate(wheres):
            if i == 0:
                sql_q += ' WHERE '+j[0]+'=:'+'u'+j[0]
            else:
                sql_q += ' AND '+j[0]+'=:'+'u'+j[0]
    sql_q += ';'
    return sql_q, wheres


# 得到_join关键字的拼接结果所需的字典
def get_join(r):
    j = {}
    rs = r.split(':')
    ll = ['join', 't2', 't1f', 'eq', 't2f']
    dic = {'INNER': ' INNER JOIN ', 'LEFT': ' LEFT JOIN ', 'RIGHT': ' RIGHT JOIN ',
           'OUTER': ' OUTER JOIN ', 'eq': ' = ', 'lt': ' > ', 'gt': ' < ', 'lte': ' >= ',
           'gte': ' <= '}  # 待补充
    for i, k in enumerate(ll):
        if k == 'join' or k == 'eq':
            j[k] = dic[rs[i]]
        else:
            j[k] = rs[i]
    return j


# 对结果进行分页 (如果页数超出了结果的范围暂时没有提示功能)
def get_page(res, n, m):
    ll = 0
    arr = []
    while m*ll < len(res):
        arr.append(res[m*ll:m*(ll+1)])
        ll += 1
    return arr[n-1]


# 得到分页后的结果
def get_page_res(result, parser):
    args = parser.parse_args()
    if args['_page']:
        n = args['_page']
        m = args['_page_size'] if args['_page_size'] else 10
        result_ = get_page(eval(result), int(n), int(m))
        result =  json.dumps(result_, ensure_ascii=False)
    return result


# 将查询结果转换成json格式
def get_json(con_e):
    r = con_e.cursor.description
    prop = []
    for i in r:
        prop.append(i[0])
    rows = con_e.fetchall()
    res = []
    for i in rows:
        dic = {}
        for p, q in zip(prop, i):
            q = str(q)  # 如果不转换成字符串会出现格式问题 比如uuid,datetime等格式
            dic[p] = q
        res.append(dic)
    result = json.dumps(res, ensure_ascii=False)
    return result


# 得到sql模板的查询结果 并将结果转换成json格式
def get_json_tem(con_e):
    return get_json(con_e)


# 得到uri的查询结果 并将结果转换成json格式
def get_json_uri(engine, par_q, wheres):
    paras = {}
    for i in wheres:
        paras['u'+i[0]] = i[1]
    par_q = text(par_q)
    c = engine.connect().execute(par_q, **paras)
    result = get_json(c)
    return result

