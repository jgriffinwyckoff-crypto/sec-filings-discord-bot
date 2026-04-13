import requests
import feedparser
import time

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1493059995271696539/HdsqIdmj2AgD8AtBZi6SJS--uQS3Mx9SVExT4QqQ0PCfh60SuMVFr4Gl4omrk45eMomR"

seen = set()

def send_to_discord(message):
    requests.post(DISCORD_WEBHOOK, json={"content": message})

print("SEC bot started")

while True:
    try:
        print("Checking SEC filings...")

        feed = feedparser.parse("https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&output=atom")

        for entry in feed.entries:
            title = entry.title
            link = entry.link

            if link in seen:
                continue

            seen.add(link)

            if "8-K" in title:
                print(f"Posting new filing: {title}")
                send_to_discord(f"🚨 **SEC Filing Alert**\n{title}\n{link}")

        time.sleep(60)

    except Exception as e:
        print("Error:", e)
        time.sleep(60)
