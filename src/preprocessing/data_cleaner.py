import pandas as pd
import re


def clean_feedback_data(df):
    """
    Clean and enrich feedback data.
    """

    print("Initial Records:", len(df))

    # Remove null feedback
    df = df.dropna(subset=["feedback_text"])

    # Remove blank feedback
    df = df[df["feedback_text"].astype(str).str.strip() != ""]

    # Remove duplicate feedback
    df = df.drop_duplicates(subset=["feedback_text"])

    # Clean text
    def clean_text(text):

        text = str(text).lower()

        # Remove URLs
        text = re.sub(r"http\S+", "", text)

        # Remove special characters
        text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    df["feedback_text"] = df["feedback_text"].apply(clean_text)

    # Convert review date
    df["review_date"] = pd.to_datetime(
        df["review_date"],
        errors="coerce"
    )

    # Feedback length
    df["feedback_length"] = (
        df["feedback_text"]
        .astype(str)
        .apply(len)
    )

    # Rating category
    def get_rating_category(rating):

        try:
            rating = float(rating)

            if rating <= 2:
                return "Negative"

            elif rating == 3:
                return "Neutral"

            else:
                return "Positive"

        except:
            return "Unknown"

    df["rating_category"] = (
        df["rating"]
        .apply(get_rating_category)
    )

    print("Final Records:", len(df))

    return df