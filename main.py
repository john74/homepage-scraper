from fastapi import FastAPI

from sport24 import sport24
from standings import standings

# run server as uvicorn main:app --port 8086  --reload
app = FastAPI()


app.include_router(sport24.router)
app.include_router(standings.router)
