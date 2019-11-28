from flask_restful import Resource, abort, reqparse
from flask import request
from App.connection import init_connect
from App.controller import get_templates, get_res_tem, get_query, get_res_uri
import App.model as md


MAX_OVERFLOW = 0  # 超过连接池大小外最多创建的连接
POOL_SIZE = 5  # 连接池大小
POOL_TIMEOUT = 30  # 池中没有线程最多等待的时间，否则报错
POOL_RECYCLE = -1  # 多久之后对线程池中的线程进行一次连接的回收（重置）

engine = init_connect(MAX_OVERFLOW, POOL_SIZE, POOL_TIMEOUT, POOL_RECYCLE)

parser = reqparse.RequestParser()
parser.add_argument('_join')
parser.add_argument('_count')
parser.add_argument('_select')
parser.add_argument('_page')
parser.add_argument('_page_size')


# 测试用
class index(Resource):
    def get(self):
        return {'index': md.test_html}


# 通过.sql模版查询数据
class rest_sql(Resource):
    def get(self, folder_, file_):
        if engine == 0 :
            abort(500, message=md.con_err)
        try:
            paras = dict(request.args)
            par_q = get_templates(folder_, file_, paras)
        except:
            abort(500, message=md.sql_err_tem)
        else:
            try:
                print(par_q)
                result = get_res_tem(engine, par_q)
            except:
                abort(500, message=md.db_err_uri)
        return result


# url直接调用查询数据
class rest_uri(Resource):
    def get(self, database_, schema_, table_):
        if engine == 0:
            abort(500, message=md.con_err)
        try:
            paras = dict(request.args)
            par_q, wheres = get_query(schema_, table_, parser, paras)
        except:
            abort(500, message=md.sql_err_uri)  
        else:
            try:
                print(par_q)
                result = get_res_uri(engine, par_q, wheres, parser)
            except:
                abort(500, message=md.db_err_uri)
        return result

