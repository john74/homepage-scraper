from sqlalchemy import Column, Integer, String
from .database import Base


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, index=True)
    website = Column(String)
    main_category = Column(String)
    category = Column(String)
    url = Column(String, unique=True, nullable=False)
    author = Column(String)
    post_date = Column(String)
    post_time = Column(String)
    images = Column(String)
    title = Column(String)
    body = Column(String)
