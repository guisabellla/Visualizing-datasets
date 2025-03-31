'''
import csv
import matplotlib.pyplot as plt

# Define the causes you're interested in
selected_causes = [ "Unintentional injuries", "Alzheimer's disease", "Stroke", "CLRD", "Diabetes"]

# Dictionary to store the death rate for each selected cause
cause_death_rate = {}

with open("NCHS_-_Leading_Causes_of_Death__United_States.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    # Iterate through each row in the CSV file
    for row in reader:
        # Filter: Only use rows where the state is "United States"
        if row['State'] != 'United States':
            continue
        # Filter: Only include rows for the selected causes
        cause = row['Cause Name']
        if cause not in selected_causes:
            continue
        # Convert the age-adjusted death rate to float
        try:
            death_rate = float(row['Deaths'])
        except ValueError:
            continue  # Skip rows where conversion fails
        # Store the death rate for the cause
        cause_death_rate[cause] = death_rate

# Prepare the data for plotting
# Use the order defined in selected_causes for consistency
causes = []
death_rates = []
for cause in selected_causes:
    if cause in cause_death_rate:
        causes.append(cause)
        death_rates.append(cause_death_rate[cause])

# Create the bar graph
plt.figure(figsize=(14, 10))
plt.bar(causes, death_rates, color='skyblue')
plt.xlabel("Cause of Death")
plt.ylabel("Age-Adjusted Death Rate")
plt.title("Age-Adjusted Death Rates for Selected Causes (United States)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
'''


import csv
import matplotlib.pyplot as plt

with open('NCHS_-_Leading_Causes_of_Death__United_States.csv', encoding='utf8') as csvfile:
    text = csvfile.read()
    data.extend(csv.loads(text))
    print(f'len(data)={len(data)}')




'''
for file in files:
    with open(file, encoding='utf8') as fin:
        text = fin.read()
        #print(text)
        data.extend(json.loads(text))
        #data.extend(xs) === data += xs
print(f'len(data)={len(data)}')

#import pprint
#pprint.pprint(data[0])

trump_counts = 0
russia_counts = 0
obama_counts = 0
fakenews_counts = 0
mexico_counts = 0
america_counts = 0
great_counts = 0
again_counts = 0
for i, tweet in enumerate(data):
    #if 'trump' in tweet['text'] or 'Trump' in tweet['text'] or 'TRUMP' in tweet['text']:
    if 'trump' in tweet['text'].lower():
        trump_counts += 1
    if 'russia' in tweet['text'].lower():
        russia_counts += 1
    if 'obama' in tweet['text'].lower():
        obama_counts += 1
    if 'fake news' in tweet['text'].lower():
        fakenews_counts += 1
    if 'mexico' in tweet['text'].lower():
        mexico_counts += 1
    if 'america' in tweet['text'].lower():
        america_counts += 1
    if 'great' in tweet['text'].lower():
        great_counts += 1
    if 'again' in tweet['text'].lower():
        again_counts += 1
print(f'trump_counts={trump_counts}')
print(f'russia_counts={russia_counts}')
print(f'obama_counts={obama_counts}')
print(f'fake news_counts={fakenews_counts}')
print(f'mexico_counts={mexico_counts}')
print(f'america_counts={america_counts}')
print(f'great_counts={great_counts}')
print(f'again_counts={again_counts}')

#print(f"i={i}, lang={tweet['lang']}, text={tweet['text']}")

word_counts = {
    'trump':0,
    'russia':0,
    'obama':0,
    'fake news':0,
    'mexico':0,
    'america':0,
    'great':0,
    'again':0,
}
for i, tweet in enumerate(data):
    for word in word_counts:
        if word in tweet['text'].lower():
            word_counts[word] += 1
import pprint
pprint.pprint(word_counts)
'''