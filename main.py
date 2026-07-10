import pandas as pd

from src.preprocessing.data_cleaner import (
    clean_feedback_data
)

# Load dataset
df = pd.read_csv(
    "data/processed/master_feedback.csv"
)

# Clean dataset
clean_df = clean_feedback_data(df)

# Save
clean_df.to_csv(
    "data/processed/cleaned_feedback.csv",
    index=False
)

print("\nCleaned dataset created successfully!")

print("\nShape:")
print(clean_df.shape)

print("\nColumns:")
print(clean_df.columns.tolist())

print("\nSample:")
print(clean_df.head())