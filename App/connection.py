from sqlalchemy import create_engine
from App.config import get_config


# 创建数据库连接
def create_connect(info, MAX_OVERFLOW, POOL_SIZE, POOL_TIMEOUT, POOL_RECYCLE):
	try:
		engine = create_engine('postgresql://' + info['user'] + ':' + info['pasw'] + '@' + \
			                  info['host'] + ':' + info['port_p'] + '/' + info['database'], \
			                  max_overflow=MAX_OVERFLOW, pool_size=POOL_SIZE, \
			                  pool_timeout=POOL_TIMEOUT, pool_recycle=POOL_RECYCLE)
	except:
	    return 0
	else:
		return engine


# 初始化数据库连接
def init_connect(MAX_OVERFLOW, POOL_SIZE, POOL_TIMEOUT, POOL_RECYCLE):
    info = get_config()
    engine = create_connect(info, MAX_OVERFLOW, POOL_SIZE, POOL_TIMEOUT, POOL_RECYCLE)
    return engine
