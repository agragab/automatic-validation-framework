from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import models
import main

app = FastAPI()

@app.get("/")
def homepage():
    return ("hello world")

@app.post("/json")
def receive_json(payload: models.jsonnaya):
    return (payload.exposure)


#receives json with readings, returns validated plaintext report of readings.
@app.post("/jsonat", response_class=PlainTextResponse)
def receive_json(payload: models.jsonnat):
    return (main.main(payload))
    