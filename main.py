from src.ingestion.google_loader import fetch_google_reviews
from src.ingestion.survey_loader import load_survey_data
from src.ingestion.combine_sources import combine_feedback_sources


GOOGLE_APP_ID = "com.microsoft.teams"

google_df = fetch_google_reviews(
    app_id=GOOGLE_APP_ID,
    count=50
)

survey_df = load_survey_data(
    "data/raw/survey_feedback.csv"
)

master_df = combine_feedback_sources(
    google_df,
    survey_df
)

master_df.to_csv(
    "data/processed/master_feedback.csv",
    index=False
)

print("\nGoogle Reviews:", len(google_df))
print("Survey Reviews:", len(survey_df))
print("Master Records:", len(master_df))

print("\nMaster dataset created successfully!")