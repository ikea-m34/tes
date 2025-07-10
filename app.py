from fastapi import FastAPI, Request
import os

app = FastAPI()

VERIFY_TOKEN = os.getenv("META_VERIFY_TOKEN", "hehehe")

@app.get("/webhook")
async def verify(request: Request):
    params = dict(request.query_params)
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN and challenge:
        print("✅ Webhook verified.")
        return int(challenge)

    print("❌ Webhook failed:", params)
    return {"error": "Invalid verification attempt"}

