##依赖包：
-  sqlalchemy
1. configparser
2. flask_restful
3. flask
4. json


## 配置文件：（例）
```
[http] 

port = 6000  //该服务的端口

[pg] 

user = “postgres”   //pg数据库的相关信息 

host = "10.8.8.111" 

pass = "Yangcong345" 

port = 5666 

database = "event_tracking" 


[queries] 

location = “sql_tem"    //.sql模版的位置 
```

## 连接池设置
```
MAX_OVERFLOW = 0  # 超过连接池大小外最多创建的连接
POOL_SIZE = 5  # 连接池大小
POOL_TIMEOUT = 30  # 池中没有线程最多等待的时间，否则报错
POOL_RECYCLE = -1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
```
在view.py中设置

## 启动服务：

`python3 start_serve.py`

## .sql模版文件：（例）

`SELECT * FROM public.pointpool WHERE pointid = {{field1}}; `

//直接填写要查询的sql语句，{{ }}中是要在uri地址中传入的参数，此处要注意参数的引号


## .sql模版测试：
```
http://127.0.0.1:6000/_QUERIES/sql_tem/sql_tem_get1?field1=2bceef38-634a-11e8-9a2d-1b370b934e93
```

###if功能
```
SELECT * FROM table
WHERE name = "{% if field1 %}{{field1}}{% endif %}"
;
```

###defaultOrValue功能
```
SELECT * FROM table WHERE name = '{{ field1 | default('2bceef38-634a-11e8-9a2d-1b370b934e93', true) }}'
;
```

###更多使用方法可参考：
<a href="http://docs.jinkan.org/docs/jinja2/templates.html" target="_blank">jinja2文档</a>
## uri测试：

```
http://127.0.0.1:6000/event_tracking/public/pointpool?pointid=2bceef38-634a-11e8-9a2d-1b370b934e93
```

###参数： 

选择参数：  
`?_select=column (select statement by columns) `

统计数量：  
`?_count=* (use count function) `

`?_conut=column (use count function) `

选择分页：  
`?_page=2&_page_size=10 (pagination, page_size 10 by default) `


###JOIN  

`/DATABASE/SCHEMA/Table?_join=Type:Table2:Table.field:Operator:Table2.field`







