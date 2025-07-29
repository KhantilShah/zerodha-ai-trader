# main.py

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from kite_helper import generate_login_url, generate_session, get_profile

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Zerodha AI Trading App"}

@app.get("/login")
def login():
    return RedirectResponse(generate_login_url())

@app.get("/callback")
def callback(request: Request):
    request_token = request.query_params.get("request_token")
    if not request_token:
        return {"error": "Missing request_token"}

    session = generate_session(request_token)
    return {"access_token": session["access_token"]}

@app.get("/profile")
def profile():
    return get_profile()
