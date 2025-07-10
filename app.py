from fastapi import FastAPI, Request
import os

app = FastAPI()

VERIFY_TOKEN = os.getenv("META_VERIFY_TOKEN", "ganti_token_ini")

@app.get("/webhook")
async def verify(request: Request):
    params = dict(request.query_params)
    if params.get("hub.mode") == "subscribe" and params.get("hub.verify_token") == VERIFY_TOKEN:
        return int(params.get("hub.challenge"))
    return {"error": "Verifikasi gagal"}

@app.post("/webhook")
async def receive_event(request: Request):
    data = await request.json()
    print("📩 Event masuk:", data)
    return {"status": "ok"}
