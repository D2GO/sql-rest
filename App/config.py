import configparser


# 得到配置文件解析结果
def get_config():
    val = {}
    cf = configparser.ConfigParser()
    cf.read('./prest.toml')
    val['user'] = getValue(cf, 'pg', 'user')[1:-1]
    val['host'] = getValue(cf, 'pg', 'host')[1:-1]
    val['pasw'] = getValue(cf, 'pg', 'pass')[1:-1]
    val['port_p'] = getValue(cf, 'pg', 'port')
    val['database'] = getValue(cf, 'pg', 'database')[1:-1]
    return val


# 得到配置文件中的端口号
def get_port():
    cf = configparser.ConfigParser()
    cf.read('./prest.toml')
    val = getValue(cf, 'http', 'port')
    return val


# 得到配置文件中的.sql模板地址
def get_loc():
    cf = configparser.ConfigParser()
    cf.read('./prest.toml')
    val = getValue(cf, 'queries', 'location')[1:-1]
    return val


# 获得分组下指定的值
def getValue(cf, section, name):
    value = cf.get(section, name)
    return value

