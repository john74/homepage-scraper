from fastapi import APIRouter, Depends

from .import scraper
from .variables import QUERY_PARAMETERS
from .import models, database
from sqlalchemy.orm import Session

router = APIRouter()
models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_sport24_articles(category):
    """
    Returns the articles from all football and basketball
    navbar categories
    """
    category_urls = scraper.get_category_urls(QUERY_PARAMETERS[category])
    articles = await scraper.get_articles(category_urls)
    return articles


@router.post("/api/store-sport24-articles")
async def store_articles(categories, db: Session = Depends(get_db)):
    """
    Returns the articles from all football and basketball
    navbar categories
    """
    articles = await get_sport24_articles(categories)
    for article_category, article in articles.items():
        existing_article = db.query(models.Article).filter(
            models.Article.category == article_category,
            models.Article.website == article['website']
        ).scalar()

        if existing_article:
            existing_article.website = article['website']
            existing_article.category = article_category
            existing_article.url = article['url']
            existing_article.author = article['author']
            existing_article.date = article['date']
            existing_article.time = article['time']
            existing_article.small_image = article['small_image']
            existing_article.medium_image = article['medium_image']
            existing_article.large_image = article['large_image']
            existing_article.title = article['title']
            existing_article.body = article['body']
        else:
            new_article = models.Article(**article)
            db.add(new_article)

        db.commit()

@router.get("/api/sport24-articles")
def get(db: Session = Depends(get_db)):
    a = db.query(models.Article).all()
    return a
