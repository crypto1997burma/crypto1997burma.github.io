import feedparser
import json
import os
import time
from datetime import datetime, timezone
from deep_translator import GoogleTranslator

RSS_FEEDS = [
    "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "https://cointelegraph.com/rss"
]

translator = GoogleTranslator(source="auto", target="my")
articles = []

for feed_url in RSS_FEEDS:
    try:
        feed = feedparser.parse(feed_url)

        for item in feed.entries[:10]:
            title = item.get("title", "").strip()
            summary = item.get("summary", "").strip()
            link = item.get("link", "")
            published = item.get("published", "")

            if not title or not link:
                continue

            try:
                my_title = translator.translate(title)
                my_summary = translator.translate(summary[:1500]) if summary else ""
            except Exception as error:
                print("Translation error:", error)
                my_title = title
                my_summary = summary

            articles.append({
                "title": my_title,
                "summary": my_summary,
                "link": link,
                "published": published,
                "source": feed.feed.get("title", "Crypto News")
            })

            time.sleep(1)

    except Exception as error:
        print("Feed error:", error)

with open("news-data.json", "w", encoding="utf-8") as file:
    json.dump(articles, file, ensure_ascii=False, indent=2)

print("Total articles:", len(articles))
print("News update completed!")
