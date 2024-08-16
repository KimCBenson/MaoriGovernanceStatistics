# Maori Governance Statistics
## By Kimberly Benson

## What Is This Repository?
This repository is a place where you can find CSV files that I created for my research paper on Maori knowledge being integrated into New Zealand's environmental governance. I created these files in July/August 2024. The purpose of these files is to create easily usable data for other researchers interested in this topic to use in the future.

**If you use or modify the charts or Python scripts provided, I ask that they be credited under Kimberly Benson.**

## Breakdown of Each File

### 1. maoriparliamentdata.csv
    This is a CSV that contains data on how many Maori MPs were in Parliament each year, the total amount of MPs, and the % of MPs that were Maori. This data was sourced from https://www.parliament.nz/en/visit-and-learn/mps-and-parliaments-1854-onwards/m%C4%81ori-mps-in-the-new-zealand-parliament-1868-onwards/.

### 2. parialiamentstats.py
  This is a Python file that reads data from maoriparliamentdata.csv and creates an easy to follow graph. I used a quartic as a line of best fit for it.

### 3. MaoriParliamentRepresentation.png
  This is a PNG file that is produced by parialiamentstats.py.
   
### 4. CHIstats.csv
  This is a CSV file that contains data from the cultural health index, a project run from 2005 to 2016 that was meant to report the conditions and usability of freshwater bodies for Maori cultural usage. This file only contains the "overall" scores from the project. This data was sourced from https://www.stats.govt.nz/indicators/cultural-health-index-for-freshwater-bodies/.

### 5. culturalhealthindexchart.py
    This is a Python file that reads data from maoriparliamentdata.csv and creates an easy to follow pie chart.

### 6. CHIChart.png
  This is a PNG file that is produced by culturalhealthindexchart.py.
