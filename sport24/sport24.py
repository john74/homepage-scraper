from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .import scraper
from .variables import QUERY_PARAMETERS
from .import models, database
from .models import Article


router = APIRouter()
models.Base.metadata.create_all(bind=database.engine)
