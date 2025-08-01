# fetcher.py
import feedparser

RSS_FEEDS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml"
]

def get_today_summary():
    summaries = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            summaries.append(f"🔸 {entry.title}\n{entry.link}\n")
    return "\n\n".join(summaries)
