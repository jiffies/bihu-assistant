from sqlalchemy import BigInteger, Column, String, DateTime, func, Integer
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:

# 定义User对象:
from models import Base


class VoteRecord(Base):
    # 表的名字:
    __tablename__ = 'vote_record'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    artId = Column(BigInteger)
    result = Column(Integer)
    message = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())