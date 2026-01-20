import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def load_data():
    return {
        "jobs": pd.read_csv(os.path.join(BASE_DIR, "data/ai_jobs.csv")),
        "skills": pd.read_csv(os.path.join(BASE_DIR, "data/skills_demand.csv")),
        "country": pd.read_csv(os.path.join(BASE_DIR, "data/country_ai_trends.csv"))
    }

