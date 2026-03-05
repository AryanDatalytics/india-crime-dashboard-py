import pandas as pd

# CSV load karo
df = pd.read_csv("crime_dataset_india.csv")

import matplotlib.pyplot as plt

# 1️⃣ Crime Domain Count
crime_counts = df['Crime Domain'].value_counts()

print("\nCrime Domain Counts:\n")
print(crime_counts)

# 2️⃣ Bar Graph
crime_counts.plot(kind='bar')
plt.title("Crime Domain Distribution")
plt.xlabel("Crime Domain")
plt.ylabel("Number of Cases")
plt.xticks(rotation=45)
#plt.show()

# Percentage Calculation
percentage = (crime_counts / crime_counts.sum()) * 100

print("\nCrime Domain Percentage:\n")
print(percentage.round(2))

gender_counts = df['Victim Gender'].value_counts()

print("\nCrime by Victim Gender:\n")
print(gender_counts)

gender_counts.plot(kind='bar')
plt.title("Crime by Victim Gender")
#plt.show()

# Create Age Groups
bins = [0, 18, 30, 45, 60, 100]
labels = ['0-18', '19-30', '31-45', '46-60', '60+']

df['Age Group'] = pd.cut(df['Victim Age'], bins=bins, labels=labels)

age_group_counts = df['Age Group'].value_counts()

print(age_group_counts)

age_group_counts.plot(kind='bar')
plt.title("Crime Distribution by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Cases")
#plt.show()

bins = [0, 18, 30, 45, 60, 100]
labels = ['0-18', '19-30', '31-45', '46-60', '60+']

df['Age Group'] = pd.cut(df['Victim Age'], bins=bins, labels=labels)
age_domain = pd.crosstab(df['Age Group'], df['Crime Domain'])

print(age_domain)
import matplotlib.pyplot as plt

age_domain.plot(kind='bar', stacked=True)

plt.title("Crime Type by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Crimes")
plt.xticks(rotation=45)

#plt.show()