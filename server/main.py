from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.get("/images")
async def get_all_images():
    return {"images": [{"url": "https://www.image.net"}]}


@app.get("/images/uploads/{user_id}")
async def read_item(skip: int = 0, limit: int = 10, page: int = 1):
    return {"images": [{"url": "foobar.com"}]}
