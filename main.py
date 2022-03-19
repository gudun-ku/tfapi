from fastapi import FastAPI
from router import topic

app = FastAPI()
app.include_router(topic.router)


@app.get("/", tags=["common"])
def index():
    return {"health": "OK"}
