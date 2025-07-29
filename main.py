from fastapi import FastAPI
from kite_helper import kite, get_profile

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Zerodha AI Trading App"}

@app.get("/profile")
def profile():
    return get_profile()
