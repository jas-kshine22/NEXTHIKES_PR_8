import pandas as pd

# Load dataset
df = pd.read_csv("all_upwork_jobs_2024-02-07-2024-03-24.csv")

def recommend_jobs(input_title):
    input_title = input_title.lower()

    matched_jobs = df[
        df['clean_title'].str.contains(input_title, na=False)
    ]

    recommendations = matched_jobs['title'].head(5).tolist()

    if len(recommendations) == 0:
        return ["No similar jobs found"]

    return recommendations
