# Job Market Skills Analyzer

## Problem
Analyzed real Data Analyst / Business Analyst job postings to identify
the most in-demand skills, helping prioritize learning and resume focus
for campus placements.

## Dataset
12,894 unique job postings (LinkedIn, scraped Dec 2023 snapshot)
Source: Kaggle

## Tools
Python, pandas, NumPy, xlsxwriter

## Process
1. Cleaned and validated 12,894 job postings (handled missing values
   using flag columns, not deletion)
2. Converted and validated date fields
3. Extracted and normalized skills from free-text job_skills column
   (case normalization fixed a data quality bug that was splitting
   "Data Analysis" into two separate counts)
4. Calculated skill demand percentages using NumPy across the full dataset
5. Exported a two-sheet Excel report with an embedded bar chart

## Key Findings
- Data Analysis appears in 36% of postings — the single most requested skill
- SQL follows closely at 33%
- Top 5 skills: Data Analysis, SQL, Project Management, Communication,
  Data Visualization
- 78% of postings are Onsite roles; only 15% are fully Remote

## How to run
1. `pip install -r requirements.txt`
2. `python src/clean_data.py`
3. `python src/extract_skills.py`
4. `python src/export_excel.py`

Output: `output/job_market_report.xlsx`
