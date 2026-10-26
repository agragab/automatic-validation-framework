from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import models
import main

app = FastAPI()

@app.get("/health")
def homepage():
    return ("healthy!")


#receives json with readings, returns validated plaintext report of readings.
@app.post("/json", response_class=PlainTextResponse)
def receive_json(payload: list[models.ReadingUnit]):
    return (main.main(payload))
    