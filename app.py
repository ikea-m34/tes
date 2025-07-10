from fastapi import FastAPI, Request
import os

app = FastAPI()

VERIFY_TOKEN = os.getenv("META_VERIFY_TOKEN", "hehehe")  # fallback default

@app.get("/webhook")
async def verify(request: Request):
    params = dict(request.query_params)
    token = params.get("hub.verify_token")
    mode = params.get("hub.mode")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN and challenge:
        return int(challenge)

    return {"error": "Token mismatch or missing challenge"}

