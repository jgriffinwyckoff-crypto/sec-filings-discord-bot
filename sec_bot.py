import requests
import feedparser
import time

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1493059995271696539/HdsqIdmj2AgD8AtBZi6SJS--uQS3Mx9SVExT4QqQ0PCfh60SuMVFr4Gl4omrk45eMomR"

seen = set()

def send_to_discord(msg):
    requests.post(DISCORD_WEBHOOK, json={"content": msg})

print("SEC watcher started", flush=True)

while True:

    try:

        print("Checking filings...", flush=True)

        feed = feedparser.parse(
            "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&output=atom"
        )

        for entry in feed.entries:

            title = entry.title
            link = entry.link

            if link in seen:
                continue

            seen.add(link)

            if "8-K" in title:

                msg = f"""
🚨 **SEC Filing**

{title}

{link}
"""

                send_to_discord(msg)

        time.sleep(60)

    except Exception as e:
        print("Error:", e, flush=True)
        time.sleep(60)
