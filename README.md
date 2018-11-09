# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run Instructions](README.md#run-instructions)

# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years.

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

# Approach

1. Read CSV file into a dictionary with key as the case ID and remaining columns as values. Repeat for header.
2. Standardize column names of file.
3. Retrieve column number for the required columns (CASE_STATUS, SOC_NAME, STATE) from the header dictionary.
4. Retrieve all types of occupations from the data of only certified cases. Repeat the same with the states.
5. Calculate frequency of each occupation. Repeat the same with the states.
7. Sort by count and incase of tie alphabetically sort by occupation name/state name.
8. Calculate percentage for each occupation/state.
9. Retrieve top 10 results and write to file.

# Run Instructions

Place the input file in the input directory as follows: './input/h1b_input.csv' and run the 'run.sh' script. Output will be created and stored in the './output/' directory.
To run, unit test cases place them in insight_testsuite and run the 'run_tests.sh' script.
