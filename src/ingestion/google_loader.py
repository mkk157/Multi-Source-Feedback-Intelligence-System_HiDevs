from google_play_scraper import reviews
import pandas as pd


def fetch_google_reviews(
    app_id: str,
    count: int = 100
):
    result, _ = reviews(
        app_id,
        lang="en",
        country="us",
        count=count
    )

    df = pd.DataFrame(result)

    df = df[
        [
            "userName",
            "score",
            "content",
            "at"
        ]
    ]

    df.columns = [
        "user_name",
        "rating",
        "feedback_text",
        "review_date"
    ]

    df["source"] = "Google Play"

    return df