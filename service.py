from fastapi import FastAPI, Request
from gpt_work import create_wish, deepai

app = FastAPI()


@app.post('/')
async def create_wish_and_picture(request: Request):
    req = await request.json()
    names = req["names"]
    result = {"text": [], "picture": []}
    for name in names:
        result["text"].append(create_wish(name))
        result["picture"].append(deepai())
    return result
