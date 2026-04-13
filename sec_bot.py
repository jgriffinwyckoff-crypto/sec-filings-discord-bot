import requests
import feedparser
import time

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1493059995271696539/HdsqIdmj2AgD8AtBZi6SJS--uQS3Mx9SVExT4QqQ0PCfh60SuMVFr4Gl4omrk45eMomR"

seen = set()

def load_biotech_tickers():
    with open("biotech_tickers.txt", "r") as f:
        return {line.strip().upper() for line in f if line.strip()}

BIOTECH_TICKERS = load_biotech_tickers()

def send_to_discord(msg):
    requests.post(DISCORD_WEBHOOK, json={"content": msg}, timeout=15)

print("Biotech SEC watcher started", flush=True)
print(f"Loaded {len(BIOTECH_TICKERS)} biotech tickers", flush=True)
send_to_discord(f"Check Loaded {len(BIOTECH_TICKERS)} biotech tickets and bot is live")

while True:
    try:
        print("Checking filings...", flush=True)

        feed = feedparser.parse(
            "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&output=atom"
        )

        for entry in feed.entries:
            title = entry.title
            link = entry.link
            title_upper = title.upper()

            if link in seen:
                continue

            seen.add(link)

            if "8-K" not in title_upper:
                continue

            matched_ticker = None
            for ticker in BIOTECH_TICKERS:
                if ticker in title_upper:
                    matched_ticker = ticker
                    break

            if not matched_ticker:
                continue

            msg = f"""🚨 **Biotech SEC Filing**
**Ticker:** {matched_ticker}
**Title:** {title}
{link}"""

            print(f"Posting {matched_ticker}: {title}", flush=True)
            send_to_discord(msg)

        time.sleep(60)

    except Exception as e:
        print("Error:", e, flush=True)
        time.sleep(60)
