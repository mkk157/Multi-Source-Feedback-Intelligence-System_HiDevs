import pandas as pd


def load_survey_data(file_path):

    df = pd.read_csv(file_path)

    df["source"] = "Survey"
    df["user_name"] = "Survey_User"
    df["review_date"] = pd.Timestamp.today()

    return df