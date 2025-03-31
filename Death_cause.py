import csv
import matplotlib.pyplot as plt


selected_causes = ["Unintentional injuries", "Alzheimer's disease", "Stroke", "CLRD", "Diabetes"]
deaths_data = {cause: 0 for cause in selected_causes}

with open("NCHS_-_Leading_Causes_of_Death__United_States.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["State"].strip() != "United States":
            continue
        
        if row["Year"].strip() != "2017":
            continue

        cause = row["Cause Name"].strip()
        if cause not in selected_causes:
            continue
        
        try:
            deaths = int(row["Deaths"].replace(",", ""))
        except ValueError:
            continue
        deaths_data[cause] += deaths

causes = list(deaths_data.keys())
deaths = [deaths_data[cause] for cause in causes]

plt.figure(figsize=(10, 6))
plt.bar(causes, deaths, color='skyblue')
plt.xlabel("Cause Name")
plt.ylabel("Number of Deaths")
plt.title("Deaths by Cause in the United States of Year 2017")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
