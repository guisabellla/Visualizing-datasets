import csv
import matplotlib.pyplot as plt

# Define the selected causes
selected_causes = ["Unintentional injuries", "Alzheimer's disease", "Stroke", "CLRD", "Diabetes"]

# Initialize a dictionary to store the total deaths for each selected cause.
deaths_data = {cause: 0 for cause in selected_causes}

# Open and read the CSV file
with open("NCHS_-_Leading_Causes_of_Death__United_States.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Filter: Only include rows for "United States"
        if row["State"].strip() != "United States":
            continue
        
        # Filter: Only include rows for the year 2017
        if row["Year"].strip() != "2017":
            continue
        
        # Check if the cause is one of the selected causes
        cause = row["Cause Name"].strip()
        if cause not in selected_causes:
            continue
        
        # Convert the "Deaths" field to an integer.
        # Remove any commas that may be present in the number.
        try:
            deaths = int(row["Deaths"].replace(",", ""))
        except ValueError:
            continue
        
        # Aggregate deaths by summing up the values (in case there are multiple rows for a cause)
        deaths_data[cause] += deaths

# Prepare the data for plotting
causes = list(deaths_data.keys())
deaths = [deaths_data[cause] for cause in causes]

# Create the bar graph
plt.figure(figsize=(10, 6))
plt.bar(causes, deaths, color='skyblue')
plt.xlabel("Cause Name")
plt.ylabel("Number of Deaths")
plt.title("Deaths by Cause in the United States of Year 2017")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
