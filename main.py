import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
df = pd.read_csv("data/police_shootings.csv")

#Convert date column to datetime
df['Date of Incident (month/day/year)'] = pd.to_datetime(df['Date of Incident (month/day/year)'], errors='coerce')

#Create 'Year' column
df['Year'] = df['Date of Incident (month/day/year)'].dt.year

#Combined Chart: Deaths per Year (Bar chart) + Cumulative deaths over time (Line chart)
# Bar data: deaths per year
deaths_per_year = df['Year'].value_counts().sort_index()
#Line data: cumulative deaths over time
df_sorted = df.sort_values('Date of Incident (month/day/year)')
df_sorted['Cumulative Deaths'] = range(1, len(df_sorted) + 1)
# Plot combined chart
fig, ax1 = plt.subplots(figsize=(12, 6))

#Bar: Deaths per year
ax1.bar(deaths_per_year.index, deaths_per_year.values, color='skyblue', label='Deaths Per Year')
ax1.set_xlabel("Year")
ax1.set_ylabel("Deaths Per Year", color='darkblue')
ax1.tick_params(axis='y', labelcolor='darkblue')
ax1.set_title("Deaths Per Year and Cumulative Deaths Over Time")
#Line: Cumulative deaths over time
ax2 = ax1.twinx()
ax2.plot(df_sorted['Date of Incident (month/day/year)'], df_sorted['Cumulative Deaths'],
         color='darkred', linewidth=2, label='Cumulative Deaths')
ax2.set_ylabel("Cumulative Deaths", color='red')
ax2.tick_params(axis='y', labelcolor='red')
fig.tight_layout()
plt.savefig("visuals/deathsanalysischart.png")
plt.show()
plt.close()

#show % share of deaths per year (Pie chart)
deaths_per_year = df['Year'].value_counts().sort_index()
plt.figure(figsize=(8, 8))
plt.pie(
    deaths_per_year,
    labels=deaths_per_year.index,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85,  # Percent inside slices
    textprops={'fontsize': 9}
)
# Optional donut style for better readability
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)
plt.title("Share of Deaths Per Year in the US", fontsize=14)
plt.tight_layout()
plt.savefig("visuals/percentshareofdeathsperyear.png")
plt.show()
plt.close()

#Yearly Disposition Trend (Stacked Bar Chart)
yearly_dispo = df.groupby(['Year', 'Official disposition of death (justified or other)']).size().unstack(fill_value=0)
plt.figure(figsize=(12, 6))
yearly_dispo.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='Set2')
plt.title("Yearly Breakdown of Official Dispositions")
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/yearlydisposition.png")
plt.show()
plt.close()

#Yearly Criminal Charges Trend (Stacked Bar Chart)
yearly_charges = df.groupby(['Year', 'Criminal Charges?']).size().unstack(fill_value=0)
plt.figure(figsize=(12, 6))
yearly_charges.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='Set3')
plt.title("Yearly Breakdown of Criminal Charges Filed")
plt.xlabel("Year")
plt.ylabel("Number of Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/yearlycriminalcharges.png")
plt.show()
plt.close()