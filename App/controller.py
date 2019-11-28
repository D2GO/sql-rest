from App.parse import get_json_tem, get_json_uri, get_sql_q, get_page_res
from flask import request, render_template
from flask_restful import abort
import App.model as md
import json
import re


# 得到最终的sql语句或错误提示
def get_templates(folder_, file_, paras):
    try:
        path = folder_ + '/' + file_ + '.read.sql'
        para_q = render_template(path, **paras)
    except:
        abort(500, message=md.para_err_tem)
    return para_q


# 得到查询结果 并将结果转换成json格式
def get_res_tem(engine, par_q):
    try:
        con_e = engine.connect().execute(par_q)
        result = get_json_tem(con_e)
    except:
        abort(500, message=md.db_err_tem)
    return result


# 得到最终的sql语句
def get_query(schema_, table_, parser, paras):
    try:
        para_q, wheres = get_sql_q(schema_, table_, parser, paras)
    except:
        abort(500, message=md.para_err_uri)
    return para_q, wheres


# 得到查询结果 并将结果转换成json格式
def get_res_uri(engine, par_q, wheres, parser):
    try:
        result = get_json_uri(engine, par_q, wheres)
    except:
        abort(500, message=md.db_err_uri)
    try:
        result = get_page_res(result, parser)
    except:
        abort(500, message=md.page_err_uri)
    return result

