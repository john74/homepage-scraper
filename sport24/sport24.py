from fastapi import APIRouter, Depends

from .import scraper
from .variables import QUERY_PARAMETERS
from .import models, database
from .models import Article
from sqlalchemy.orm import Session

router = APIRouter()
models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# async def get_articles(article_category):
#     """
#     Returns the articles from all football and basketball
#     navbar categories
#     """
#     category_urls = scraper.get_category_urls(QUERY_PARAMETERS[article_category])
#     articles = await scraper.get_articles(category_urls)
#     return articles


@router.post("/api/store-sport24-articles")
async def store_articles(subcategory, db: Session = Depends(get_db)):
    """
    Returns the articles from all football and basketball
    navbar categories
    """
    subcategory_urls = scraper.get_subcategory_urls(QUERY_PARAMETERS[subcategory])
    articles = await scraper.get_articles(subcategory_urls)
    for article in articles:
        existing_article = db.query(Article).filter(
            Article.general_category == subcategory,
            Article.category == article['category'],
            Article.website == article['website']
        ).scalar()

        if existing_article:
            existing_article.website = article['website']
            existing_article.category = article['category']
            existing_article.general_category = subcategory
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
            article['general_category'] = subcategory
            new_article = Article(**article)
            db.add(new_article)

        db.commit()

@router.get("/api/sport24-articles")
def get_articles_by_category(general_category, db: Session = Depends(get_db)):
    articles = db.query(Article).filter(Article.general_category == general_category).all()
    return articles
