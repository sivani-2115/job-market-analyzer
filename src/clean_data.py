import pandas as pd

df = pd.read_csv("data/raw_jobs_data.csv")

print(df.shape)
print(df.columns)
print(df.head())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df["job_link"].duplicated().sum())
print(df.dtypes)
print(df["first_seen"].head(10))
df["first_seen"] = pd.to_datetime(df["first_seen"])
print(df["first_seen"].dtype)
print(df["first_seen"].nunique())
print(df["first_seen"].min(), "to", df["first_seen"].max())
print(df["job level"].value_counts())
print(df["job_type"].value_counts())
df["summary_missing"] = df["job_summary"].isnull()
df["skills_missing"] = df["job_skills"].isnull()

print(df["summary_missing"].sum())
print(df["skills_missing"].sum())
df["job_summary"] = df["job_summary"].fillna("")
df["job_skills"] = df["job_skills"].fillna("")

print(df["job_summary"].isnull().sum())
print(df["job_skills"].isnull().sum())
df.to_csv("data/cleaned_jobs_data.csv", index=False)

