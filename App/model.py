
test_html = u'这里是sql-rest, 输入你要操作的RESTful请求！'

con_err = u'数据库连接错误, 请检查数据库配置参数！'
sql_err_tem = u'SQL语句格式错误, 请检查.sql模板和uri请求参数！'
db_err_tem = u'数据库查询错误, 请检查.sql模板和uri请求参数！'
sql_err_uri = u'SQL语句格式错误, 请检查uri请求参数！'
db_err_uri = u'数据库查询错误, 请检查uri请求参数！'

para_err_tem = u'SQL模板语句或对应参数填写错误, 请检查.sql模板文件和uri请求参数！'
para_err_uri = u'uri或请求参数填写错误, 请检查uri请求参数！'
page_err_uri = u'分页出现错误, 请重新检查相关参数！'


'''
# 用于解决json中中文无法显示的问题
import json

def trans(str):
	return eval(json.dumps(str, ensure_ascii=False))

test_html = trans(test_html)
con_err = trans(con_err)
sql_err_tem = trans(sql_err_tem)
db_err_tem = trans(db_err_tem)
sql_err_uri = trans(sql_err_uri)
db_err_uri = trans(db_err_uri)
para_err_tem = trans(para_err_tem)
para_err_uri = trans(para_err_uri)
page_err_uri = trans(page_err_uri)
'''
