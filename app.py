from fastapi import FastAPI, Request
from fastapi.responses import Response  # ⬅️ Tambahkan ini

app = FastAPI()

VERIFY_TOKEN = "hehehe"

@app.get("/")
def root():
    return {"message": "Server is alive!"}

@app.get("/webhook")
async def verify(request: Request):
    params = dict(request.query_params)
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    print("📥 Webhook params masuk:", params)

    if mode == "subscribe" and token == VERIFY_TOKEN and challenge:
        print("✅ Webhook verified.")
        return Response(content=challenge, media_type="text/plain")  # ⬅️ FIX

    print("❌ Webhook verification failed.")
    return {"error": "Invalid token or missing challenge"}

@app.post("/webhook")
async def receive_event(request: Request):
    data = await request.json()
    print("📩 Event masuk:", data)
    return {"status": "ok"}
