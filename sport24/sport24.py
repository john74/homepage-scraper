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
def store_articles(main_category, db: Session = Depends(get_db)):
    anchor_elements = CATEGORY_SELECTORS[main_category]
    category_urls = scraper.get_category_urls(anchor_elements)
    category_name_url_pairs = scraper.get_category_name_url_pairs(category_urls)
    recent_articles = scraper.get_recent_articles(category_name_url_pairs)
    unique_pairs = scraper.get_unique_pairs(recent_articles)
    url_accepted_pairs = scraper.get_url_accepted_pairs(unique_pairs)
    articles = scraper.get_articles(url_accepted_pairs, main_category)

    if not articles:
        return

    for article in articles:
        article_with_same_url = db.query(Article).filter(Article.url == article['url']).scalar()
        if article_with_same_url:
            continue

        existing_article = db.query(Article).filter(
            Article.main_category == main_category,
            Article.category == article['category'],
            Article.website == article['website']
        ).scalar()

        if existing_article:
            existing_article.website = article['website']
            existing_article.main_category = article['main_category']
            existing_article.category = article['category']
            existing_article.url = article['url']
            existing_article.author = article['author']
            existing_article.post_date = article['post_date']
            existing_article.post_time = article['post_time']
            existing_article.images = article['images']
            existing_article.title = article['title']
            existing_article.body = article['body']
        else:
            new_article = Article(**article)
            db.add(new_article)

        db.commit()

    return articles


@router.get("/api/get-sport24-articles")
def get_articles(main_category, db: Session = Depends(get_db)):
    articles = db.query(Article).filter(Article.main_category == main_category).all()
    return articles
