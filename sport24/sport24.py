from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import scraper
from .variables import CATEGORY_SELECTORS
from . import models, database
from .models import Article


# router path operation
# https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=apir#import-apirouter
router = APIRouter()
# create database tables
models.Base.metadata.create_all(bind=database.engine)

# https://fastapi.tiangolo.com/tutorial/sql-databases/?h=models.base#create-a-dependency
def get_db():
    """
    Dependency.
    Creates an independent database session per request,
    and closes the connection when all the request
    operations are finished
    """
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/api/store-sport24-articles")
def store_articles(category, db: Session = Depends(get_db)):
    anchor_elements = CATEGORY_SELECTORS[category]
    category_urls = scraper.get_category_urls(anchor_elements)
    category_name_url_pairs = scraper.get_category_name_url_pairs(category_urls)
    recent_articles = scraper.get_recent_articles(category_name_url_pairs)
    unique_pairs = scraper.get_unique_pairs(recent_articles)
