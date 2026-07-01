# MLB National League Standigns Dashboard

## Overview
An automated, end-to-end analytics pipeline that tracks the full MLB National League season in rela time. A python scrips pulls daily standigns form the MLB API, runs an automated schedule via GItHub Actions, and feeds an interactive Power BI dashboard for exploring standigns, trends, and KPIs at a glance. 

The objective is to give the viewer a real time look at the season  without having to look through the MLB website for information. They can track their team's standings and trends from day one. 

## Tools
Python, Pandas, PowerBI, GitHub Actions

## How it works
- Daily automated pull from the MLB Stats API (Python), scheduled via GitHub 
  Actions with email alerts on failure
- Incremental-load logic: only fetches and appends missing dates, avoiding 
  duplicate records and redundant API calls
- Transformed and structured with pandas into a running daily dataset
- Visualized in Power BI with cross-filtering by division and team

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

## Current Limitations
- Currently NL-only (AL support planned)
- Data stored as flat CSV rather than database. This is fine at the current scale but would revisit for multi-season history. 


## Next Steps
- Incorporate wild-card standigns and race tracking across both leagues
- Add a Pythagorean win expectancy metric
- Expand to include AL teams for full-league coverage. 
