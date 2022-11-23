from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import scraper
from .variables import QUERY_PARAMETERS
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
    category_selector = QUERY_PARAMETERS[category]
