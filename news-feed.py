import feedparser
from datetime import datetime

RSS_FEEDS = [
    "https://www.reuters.com/rssFeed/topNews",
    "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
    "https://www.yna.co.kr/rss/all01.xml",
]

def fetch_rss():
    results = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:5]:
            results.append(f"📰 {entry.title}\n{entry.link}\n\n")
    return results

if __name__ == "__main__":
    news_items = fetch_rss()
    today = datetime.now().strftime("%Y-%m-%d")
    with open(f"./news/news_{today}.txt", "w", encoding="utf-8") as f:
        f.write("".join(news_items))
