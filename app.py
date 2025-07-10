from fastapi import FastAPI, Request

app = FastAPI()

VERIFY_TOKEN = "hehehe"  # Hardcoded token untuk testing

# Route root untuk cek server aktif
@app.get("/")
def root():
    return {"message": "Server is alive!"}

# Route webhook GET (verifikasi dari Facebook)
@app.get("/webhook")
async def verify(request: Request):
    params = dict(request.query_params)
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    print("📥 Webhook params masuk:", params)

    if mode == "subscribe" and token == VERIFY_TOKEN and challenge:
        print("✅ Webhook verified.")
        return int(challenge)

    print("❌ Webhook verification failed.")
    return {"error": "Invalid token or missing challenge"}

# (Optional) Route POST webhook untuk nerima event dari Meta
@app.post("/webhook")
async def receive_event(request: Request):
    data = await request.json()
    print("📩 Event masuk:", data)
    return {"status": "ok"}


