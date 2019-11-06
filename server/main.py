from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: str
    email: str
    uploads: int = 0
    name: str = ""
    hash: str
    nsfw: bool = False
    created_at: datetime


class UserIn(BaseModel):
    email: str
    hash: str


class Image(BaseModel):
    id: str
    url: str
    secure_url: str
    title: str
    height: int
    width: int
    format: str
    nsfw: bool = False
    views: int = 0
    created_at: datetime = None
    author_id: str


app = FastAPI()


@app.post("/users/register")
async def create_user(user: UserIn):
    return user


@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.get("/images")
async def get_all_images():
    return {"images": [{"url": "https://www.image.net"}]}


@app.get("/images/uploads/{user_id}")
async def read_item(skip: int = 0, limit: int = 10, page: int = 1):
    return {"images": [{"url": "foobar.com"}]}


@app.post("/images/upload")
async def upload_image(file: UploadFile = File(...)):
    return {"filename": file.filename}
