import pandas as pd

def load_data():
    return {
        "jobs": pd.read_csv("data/ai_jobs.csv"),
        "skills": pd.read_csv("data/skills_demand.csv"),
        "country": pd.read_csv("data/country_ai_trends.csv")
    }
