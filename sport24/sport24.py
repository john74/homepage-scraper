from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .import scraper
from .variables import QUERY_PARAMETERS
from .import models, database
from .models import Article


# router path operation
# https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=apir#import-apirouter
router = APIRouter()
# create database tables
models.Base.metadata.create_all(bind=database.engine)

# dependency
# https://fastapi.tiangolo.com/tutorial/sql-databases/?h=models.base#create-a-dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
