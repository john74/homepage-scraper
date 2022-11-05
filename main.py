from fastapi import FastAPI

# uvicorn main:app --port 8086  --reload
app = FastAPI()

@app.get("/")
async def root():
  return {"hello:world"}
