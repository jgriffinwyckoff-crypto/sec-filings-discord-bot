import requests
import feedparser
import time

DISCORD_WEBHOOK = "PASTE_YOUR_WEBHOOK_HERE"

seen = set()

def send_to_discord(message):
    requests.post(DISCORD_WEBHOOK, json={"content": message})

while True:

    feed = feedparser.parse("https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent")

    for entry in feed.entries:

        title = entry.title
        link = entry.link

        if link in seen:
            continue

        seen.add(link)

        if "8-K" in title:

            message = f"🚨 SEC Filing Alert\n{title}\n{link}"

            send_to_discord(message)

    time.sleep(60)
