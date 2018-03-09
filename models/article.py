from sqlalchemy import BigInteger, Column, String, DateTime, func, Integer
from sqlalchemy.ext.declarative import declarative_base



# 定义User对象:
from models import Base


class Article(Base):
    # 表的名字:
    __tablename__ = 'article'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    artId = Column(BigInteger)
    title = Column(String)
    authorId = Column(BigInteger)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())