from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world!"}

@app.get("/images")
async def get_all_images():
    return {"images": [{"url": 'https://www.image.net'}]}