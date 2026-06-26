# NL_standings_2026
How can you not be romantic about baseball?

## Overview
A quick breadown of the MLB National League. 
An end-to-end project starting with MLB API pull with python, transformation with pandas, and visual created with Power BI. 

The objective was to give the viewer a real time look at the season and a quick glance without having to look through the MLB website for information. 

## Tools
Python, Pandas, PowerBI

## Dataset
Data pulled using MLB API with Python. 
New row added every day for each team with: 
 - Date
 - Team Name
 - Wins
 - Losses
 - Win %
 - Run Differential
 - Wins in last 10 games
 - Losses in last 10 games
 - Day of Season
 - Division
 - Games Back in the Division
 - Division Rank

## Files
- .github/workflows       - Allows for python script to autorun and update CSV daily
- MLB_NL_Dashboard.pbix   - Power Bi Interactive dashboard
- MLB_NL_Dashboard.pdf    - PDF Of Power BI for easy viewing
- mlb_standings.csv       - daily updated data
- mlb_standings_script.py - Python script to pull, transform, and upload data.  
