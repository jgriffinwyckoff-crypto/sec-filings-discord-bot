import requests
import time
import sys

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1493059995271696539/HdsqIdmj2AgD8AtBZi6SJS--uQS3Mx9SVExT4QqQ0PCfh60SuMVFr4Gl4omrk45eMomR"

def send_to_discord(message):
    r = requests.post(DISCORD_WEBHOOK, json={"content": message}, timeout=15)
    print(f"Discord status: {r.status_code}", flush=True)

print("SEC bot started", flush=True)

try:
    send_to_discord("✅ SEC bot started on Railway")
except Exception as e:
    print(f"Startup Discord error: {e}", flush=True)

while True:
    print("Heartbeat...", flush=True)
    time.sleep(60)
