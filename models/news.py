from sqlalchemy import Integer,Text,String
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    pass

class News(Base):
    __tablename__="news"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True,comment="新闻ID")
    title:Mapped[str]=mapped_column(String(200),nullable=False,comment="新闻标题")
    brief:Mapped[str]=mapped_column(String(200),nullable=True,comment="新闻摘要")
    href:Mapped[str]=mapped_column(String(200),nullable=True,comment="新闻链接")
    img:Mapped[str]=mapped_column(String(200),nullable=True,comment="新闻图片名称")