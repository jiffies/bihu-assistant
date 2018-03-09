# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('sqlite:///bihu.db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)