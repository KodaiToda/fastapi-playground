from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
  return {"message": "Hello, World"}

@app.get("/hello")
async def hello():
  return {"message": "Say Hello"}

@app.get("/countries/{country_name}")
async def country(country_name: str):
  return {"country_name": country_name}

@app.get("/library/")
async def library(book_name: str = 'Harry Potter', book_no: int = 1):
  return {
    "book_name": book_name,
    "book_no": book_no
  }