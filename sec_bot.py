import requests
import time

DISCORD_WEBHOOK = "PASTE_YOUR_WEBHOOK_HERE"

def send_to_discord(message):
    r = requests.post(DISCORD_WEBHOOK, json={"content": message}, timeout=15)
    print("Discord status:", r.status_code, flush=True)
    print("Discord response:", r.text, flush=True)

print("Bot file started", flush=True)

try:
    send_to_discord("✅ Debug test from Railway startup")
except Exception as e:
    print("Startup error:", str(e), flush=True)

while True:
    print("Heartbeat...", flush=True)
    time.sleep(60)
