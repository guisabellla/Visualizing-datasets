import json
import matplotlib.pyplot as plt


with open("China_GDP.json", "r") as f:
    china_json = json.load(f)
china_records = china_json[1]

with open("US_GDP.json", "r") as f:
    us_json = json.load(f)
us_records = us_json[1]


china_filtered = [rec for rec in china_records if 2000 <= int(rec["date"]) <= 2023]
us_filtered = [rec for rec in us_records if 2000 <= int(rec["date"]) <= 2023]


china_filtered = sorted(china_filtered, key=lambda rec: int(rec["date"]))
us_filtered = sorted(us_filtered, key=lambda rec: int(rec["date"]))


years_china = [int(rec["date"]) for rec in china_filtered]
gdp_china = [rec["value"] for rec in china_filtered]

years_us = [int(rec["date"]) for rec in us_filtered]
gdp_us = [rec["value"] for rec in us_filtered]

plt.figure(figsize=(10, 6))
plt.plot(years_china, gdp_china, marker='o', label="China")
plt.plot(years_us, gdp_us, marker='o', label="USA")
plt.xlabel("Year")
plt.ylabel("GDP (10 trillion current US$)")
plt.title("GDP of China vs USA (2000-2023)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()