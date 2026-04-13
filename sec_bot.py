import requests
import time

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1493059995271696539/HdsqIdmj2AgD8AtBZi6SJS--uQS3Mx9SVExT4QqQ0PCfh60SuMVFr4Gl4omrk45eMomR"

def send_to_discord(message):
    requests.post(DISCORD_WEBHOOK, json={"content": message})

print("SEC bot started")

while True:
    try:
        print("Bot running...")
        
        # test message every 60 seconds
        send_to_discord("🚨 SEC filings bot is running")
        
        time.sleep(60)

    except Exception as e:
        print("Error:", e)
        time.sleep(60)
