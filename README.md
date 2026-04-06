# Data Careers in the US - Salary and Geographic Overview

**Live Dashboard:** [View on Tableau Public](https://public.tableau.com/app/profile/mason.spalding/viz/DataCareersintheUS-SalaryGeographicOverview/Overview?publish=yes)

## Overview

This project analyzes employment and wage data from the US Bureau of Labor Statistics to answer a key question: Where should someone interested in a data role go to maximize their salary and opportunity?

The analysis covers five data-related occupations across the entire United States discovering insights on salary distributions, geographic hotspots, and the highest performing industries.

## Data Source

The data was taken from the Occupational Employment and Wage Statistics program (OEWS) ran by the US Bureau of Labor Statistics. Specifically the data from May 2024.
- Source: [US Bureau of Labor Statistics](https://www.bls.gov/oes/tables.htm)
- Original Dataset: 414,438 Rows, 1,138 occupations, 394 Industries
- Filtered Dataset: 3,028 Rows, 5 occupations, 369 Industries

## Occupations Analyzed

| SOC Code | Role |
|---|---|
| 15-2051 | Data Scientists |
| 15-2031 | Operations Research Analysts |
| 15-1242 | Database Administrators |
| 15-1243 | Database Architects |
| 13-1161 | Market Research Analysts |

## Tools Used

- **Python** - Data Cleaning and Transformations
- **pandas** - Data manipulation and Analysis
- **openpyxl** - Excel File Integration
- **Tableau Public** - Interactive Dashboard and Data Visualization

## Data Cleaning Steps

The raw dataset required the following cleaning steps which can be seen in data_cleaning.py:

- **Salary Data Type Conversion** - The BLS uses special characters (*, **, #, ~) as notes for the salary data. This had to be removed to convert the data into a useable numeric form. Replacing the characters with 'NaN' fixes this issue.
- **Geographic Filtering** - The data covers national, state, metro areas, and US territories. US territories only account for 7 rows making it insufficient to provide meaningful insight thus were removed. 
- **Occupation Filtering** - Removed all occupations unrelated to data and excluded broad groups to prevent double counting. 
- **Missing Value Removal** - Since salary is the key metric, removing rows missing salary information is a must. This only account for 95 rows. 
- **Small Industry Filtering** - Set a minimum employee count to 1,000 to remove industries with to few data points. 

## Key Findings

- Database Architects have the highest average median annual salary at ~129k. This is roughly ~30k more than data scientist. 
- Data Scientist have the the widest salary ranges both including and excluding outliers. Location and industry likely matter more in this role compared to the others. 
- The San Jose and San Francisco metro areas have the highest average median annual salary. This is likely due to the concentration of major tech companies. 
- New York underperforms expectations. While New York does have high salary opportunities the diversity of industries such as government and healthcare drive down the state average. 
- Software publishing and publishing industries are the highest paying industries for data roles. Software publishing is no surprise but the publishing industry is likely driven up by data-heavy financial media companies which invest heavily in talent compared to more traditional media companies. 


