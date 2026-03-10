#!/usr/bin/env python3
"""
World News Aggregator - Fetch Script
Optional standalone script for fetching news outside of OpenClaw.

Usage:
    python fetch-news.py --sources tech,ai --limit 10 --hours 24
"""

import argparse
import json
import sys
from datetime import datetime, timedelta

try:
    import requests
    import feedparser
except ImportError:
    print("Installing dependencies...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    import requests
    import feedparser


SOURCES = {
    "tech": [
        {"name": "TechCrunch", "url": "https://techcrunch.com/feed/", "type": "rss"},
        {"name": "The Verge", "url": "https://www.theverge.com/rss/index.xml", "type": "rss"},
        {"name": "Wired", "url": "https://www.wired.com/feed/rss", "type": "rss"},
    ],
    "ai": [
        {"name": "arXiv AI", "url": "http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=10", "type": "atom"},
        {"name": "Hugging Face", "url": "https://huggingface.co/papers/feed", "type": "rss"},
    ],
    "stock": [
        {"name": "Yahoo Finance", "url": "https://finance.yahoo.com/news/rssindex", "type": "rss"},
    ],
    "cn-tech": [
        {"name": "36Kr", "url": "https://36kr.com/feed", "type": "rss"},
    ],
}


def fetch_rss(url: str, limit: int = 10) -> list:
    """Fetch and parse RSS feed."""
    try:
        feed = feedparser.parse(url)
        entries = []
        for entry in feed.entries[:limit]:
            entries.append({
                "title": entry.get("title", "No title"),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "summary": entry.get("summary", "")[:200] if entry.get("summary") else "",
                "source": feed.feed.get("title", "Unknown"),
            })
        return entries
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []


def fetch_news(sources: list, limit: int = 10, hours: int = 24) -> dict:
    """Fetch news from multiple sources."""
    results = {}
    cutoff = datetime.now() - timedelta(hours=hours)
    
    for source_key in sources:
        if source_key not in SOURCES:
            print(f"Unknown source: {source_key}")
            continue
        
        results[source_key] = []
        for source in SOURCES[source_key]:
            print(f"Fetching {source['name']}...")
            entries = fetch_rss(source["url"], limit)
            results[source_key].extend(entries)
    
    return results


def main():
    parser = argparse.ArgumentParser(description="World News Aggregator")
    parser.add_argument("--sources", type=str, default="tech,ai",
                        help="Comma-separated list of sources (tech,ai,stock,cn-tech)")
    parser.add_argument("--limit", type=int, default=10,
                        help="Number of articles per source")
    parser.add_argument("--hours", type=int, default=24,
                        help="Time range in hours")
    parser.add_argument("--output", type=str, default="json",
                        choices=["json", "markdown"],
                        help="Output format")
    
    args = parser.parse_args()
    sources = [s.strip() for s in args.sources.split(",")]
    
    print(f"Fetching news from: {', '.join(sources)}")
    print(f"Limit: {args.limit} per source, Time range: {args.hours} hours\n")
    
    results = fetch_news(sources, args.limit, args.hours)
    
    if args.output == "json":
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        # Markdown output
        for source_key, entries in results.items():
            print(f"\n## {source_key.upper()}\n")
            for entry in entries:
                print(f"### {entry['title']}")
                print(f"- **Source**: {entry['source']}")
                print(f"- **Link**: {entry['link']}")
                print(f"- **Published**: {entry['published']}")
                print(f"- **Summary**: {entry['summary']}...\n")


if __name__ == "__main__":
    main()
