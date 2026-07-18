import pandas as pd

df = pd.read_csv("data/cleaned_jobs_data.csv")
skill_summary = pd.read_csv("data/skill_summary.csv")

print(df.shape)
print(skill_summary.shape)
with pd.ExcelWriter("output/job_market_report.xlsx", engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Cleaned Jobs", index=False)
    skill_summary.to_excel(writer, sheet_name="Skill Demand", index=False)

    workbook = writer.book
    worksheet = writer.sheets["Skill Demand"]

    chart = workbook.add_chart({"type": "bar"})
    chart.add_series({
        "name": "Demand %",
        "categories": ["Skill Demand", 1, 0, 20, 0],
        "values": ["Skill Demand", 1, 2, 20, 2],
    })
    chart.set_title({"name": "Top 20 In-Demand Skills"})
    chart.set_x_axis({"name": "Demand %"})
    worksheet.insert_chart("E2", chart)

print("Excel report saved to output/job_market_report.xlsx")