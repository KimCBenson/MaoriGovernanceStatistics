# import statements
import pandas as pd
import matplotlib.pyplot as plt

# read the CSV file into a DataFrame
df = pd.read_csv('CHIstats.csv')

# create  labels with number of sites and percentage
labels = [f'{row["Quality"]} ({row["Amount"]} of sites, {row["Amount"] / df["Amount"].sum() * 100:.1f}%)' 
          for _, row in df.iterrows()]

# creates the color palette
colors = ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7']

# create a figure and axis with adjusted size
fig, ax = plt.subplots(figsize=(14, 10))  # Increase figure size to make room for the legend

# plot pie chart
patches, _ = ax.pie(df['Amount'], startangle=140, colors=colors, textprops={'fontsize': 14})

# add a legend with custom labels
ax.legend(patches, labels, title="Quality", title_fontsize='13', fontsize='12', loc="center left", bbox_to_anchor=(1, 0.5))

# Add a title with larger font size
ax.set_title('Results of the Cultural Health Index', fontsize=18)

# adjust the layout to make room for the legend
plt.subplots_adjust(right=0.75)

# display the plot
plt.show()
