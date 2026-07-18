import pandas as pd

df = pd.read_csv("data/cleaned_jobs_data.csv")
df["job_skills"] = df["job_skills"].fillna("")
df["job_summary"] = df["job_summary"].fillna("")
print(df["job_skills"].head(10))
def split_skills(skill_string):
    if skill_string == "":
        return []
    skills = skill_string.split(",")
    skills = [s.strip().lower() for s in skills]
    return skills

df["skills_list"] = df["job_skills"].apply(split_skills)

print(df["skills_list"].head(10))
from collections import Counter

all_skills = []
for skills in df["skills_list"]:
    all_skills.extend(skills)

skill_counts = Counter(all_skills)

print(len(all_skills))
print(len(skill_counts))
print(skill_counts.most_common(15))
import numpy as np

total_postings = len(df)

top_20 = skill_counts.most_common(20)
skills_names = [item[0] for item in top_20]
skills_counts = np.array([item[1] for item in top_20])

demand_percentage = np.round((skills_counts / total_postings) * 100, 2)

for skill, count, pct in zip(skills_names, skills_counts, demand_percentage):
    print(f"{skill}: {count} postings ({pct}%)")
    skill_summary = pd.DataFrame({
    "skill": skills_names,
    "postings_count": skills_counts,
    "demand_percentage": demand_percentage
})

skill_summary.to_csv("data/skill_summary.csv", index=False)
print(skill_summary)