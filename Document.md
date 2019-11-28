##程序结构
start_serve.py 程序启动文件

**App**    

\- views.py 处理请求视图类
  
  \- controller.py 控制逻辑
  
  \- parse.py 解析请求
  
  \- connection.py 连接数据库
  
  \- config.py 读取配置文件
  
  \- model.py 存放错误信息 
      
  **sql_tem** 存放模板文件的文件夹   
  
  **Test** 存放测试文件的文件夹
    
   \- test.py 测试程序
  
  \- Test_uri.md 测试请求   
  
prest.toml 配置文件
 
readme.md  

##程序主要函数/类
**class rest_sql** .sql模板的请求视图类  
 get\_templates(folder_, file_, paras)   
 得到模板与参数拼接好的SQL语句  
 get\_res\_tem(engine, par_q)  
 将上面得到的SQL语句发送给数据库得到查询结果
 
**class rest_sql** uri的请求视图类  
get\_query(schema_, table_, parser, paras)  
根据uri请求地址和请求参数（按照SQL语法规则）逐步拼接成SQL语句  
get\_res\_uri(engine, par_q, wheres, parser)
将上面拼接好的SQL语句发送给数据库进行查询，如有需要将结果进行分页

##程序存在的问题
1. uri请求对应的SQL解析逻辑还可以进一步优化
2. 可以进一步增加和完善错误提示功能
