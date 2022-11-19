from fastapi import APIRouter

# from . import scraper
# from . variables import QUERY_PARAMETERS
from . import schemas, models, database

router = APIRouter()
models.Base.metadata.create_all(bind=database.engine)

# @router.get("/api/sport24-articles/")
# async def get_sport24_articles(category):
#     """
#     Returns the articles from all football and basketball
#     navbar categories
#     """
#     category_urls = scraper.get_category_urls(QUERY_PARAMETERS[category])
#     return await scraper.get_articles(category_urls)

@router.get("/api/sport24-articles/")
async def get_sport24_articles(request: schemas.ArticleBase):
    """
    Returns the articles from all football and basketball
    navbar categories
    """
    return request
    # category_urls = scraper.get_category_urls(QUERY_PARAMETERS[category])
    # return await scraper.get_articles(category_urls)
