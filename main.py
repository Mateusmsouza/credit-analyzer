from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health_check():
    return {"Im feeling good": ":)"}

