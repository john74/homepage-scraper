from sqlalchemy import Column, Integer, String
from .database import Base


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    author = Column(String)
    date = Column(String)
    time = Column(String)
    small_image = Column(String)
    medium_image = Column(String)
    large_image = Column(String)
    title = Column(String)
    body = Column(String)
