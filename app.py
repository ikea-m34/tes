from fastapi import FastAPI, Request

app = FastAPI()

VERIFY_TOKEN = "hehehe"  # hardcoded sementara

@app.get("/")  # ← ini buat root check
def root():
    return {"message": "Server is alive!"}

@app.get("/webhook")  # ← ini buat webhook GET
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

