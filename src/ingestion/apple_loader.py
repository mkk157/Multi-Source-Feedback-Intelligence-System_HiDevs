import feedparser
import pandas as pd


def fetch_apple_reviews(app_id: str):

    rss_url = (
        f"https://itunes.apple.com/us/rss/customerreviews/id={app_id}/json"
    )

    feed = feedparser.parse(rss_url)

    reviews = []

    for entry in feed.entries:

        review = {
            "user_name": entry.get("author", ""),
            "rating": None,
            "feedback_text": entry.get("summary", ""),
            "review_date": entry.get("published", ""),
            "source": "Apple Store"
        }

        reviews.append(review)

    return pd.DataFrame(reviews)
