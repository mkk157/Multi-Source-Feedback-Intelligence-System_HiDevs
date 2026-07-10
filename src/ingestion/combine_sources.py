import pandas as pd


def combine_feedback_sources(
    google_df,
    survey_df
):

    google_df = google_df[
        [
            "source",
            "user_name",
            "rating",
            "feedback_text",
            "review_date"
        ]
    ]

    survey_df = survey_df[
        [
            "source",
            "user_name",
            "rating",
            "feedback_text",
            "review_date"
        ]
    ]

    master_df = pd.concat(
        [google_df, survey_df],
        ignore_index=True
    )

    return master_df