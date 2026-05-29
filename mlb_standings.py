import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
import urllib.request
import json

import csv
import os
print('loaded!')


'''Set up Base Variables'''
BASE_URL = 'https://statsapi.mlb.com/api/v1'
LEAGUE_IDS = {'AL': 103, 'NL': 104}
DIVISION_NAMES = {203: 'West', 205: 'Central', 204: 'East'}
SEASON = 2026
DATE = datetime.today().strftime('%Y-%m-%d')
start_date = '2026-3-26'



def fetch_standings(league_id: int, date:str, season:int) -> dict:
    '''
    Fetch raw standings JSON from MLB API
    '''
    url = (f'{BASE_URL}/standings'
           f'?leagueId={league_id}'
           f'&season={season}'
           f'&standingsTypes=regularSeason'
           f'&date={date}'
    )
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())

def get_last_ten(team_record: dict) -> str:
    '''Pulls last 10 games'''
    for split in team_record['records']['splitRecords']:
        if split['type'] == 'lastTen':
            return [split['wins'], split['losses']]
    return 'N/A'

def parse_standings(data:dict, day) -> list[dict]:
    """
    Extract fields we care about from JSON. Returns team Records list
    """

    teams = []
    for division_record in data['records']:
        for team in division_record['teamRecords']:
            teams.append({
                'date': day,
                'team': team['team']['name'],
                'wins': team['wins'],
                'losses': team['losses'],
                'percent': float(team['winningPercentage']),
                'run_diff': team['runDifferential'],
                'last_10_wins': get_last_ten(team)[0],
                'last_10_losses': get_last_ten(team)[1],
                'day_of_season': (date.fromisoformat(day)-date(2026, 3, 26)).days +1,
                'division': DIVISION_NAMES.get(division_record['division']['id'])
            })
    
    return teams
    
def save_to_csv(df: pd.DataFrame, filepath: str) -> None:
    '''Saves to csv for Power Bi'''
    file_exists = os.path.exists(filepath)

    if file_exists:
        existing=pd.read_csv(filepath)

        #check for existing dates
        existing['date'] = pd.to_datetime(existing['date'], format = 'mixed').dt.strftime('%m/%d/%Y')
        existing_dates = set(existing['date'].values)
        df = df[~df['date'].isin(existing_dates)]
        
        # check if all dates saved
        if df.empty:
            (print('All dates alraedy saved!'))
            return
        
    # standardize date    
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%m/%d/%Y')

    # save to CSV
    df.to_csv(
        filepath, 
        mode = 'a', 
        header = not file_exists,
        index = False
    )

    print('Saved!')

def get_missing_dates(filepath: str, start_date: str) -> list:
    """ Returns list of missing dates between opening day and today"""
    existing = pd.read_csv(filepath)
    existing_dates = pd.to_datetime(existing['date'], format = 'mixed')
    existing_dates = pd.DatetimeIndex(existing_dates)
    expected = pd.date_range(start = start_date, end = datetime.today())
    missing = expected.difference(existing_dates)

    return missing.strftime('%Y-%m-%d').tolist()


def main():
    missing_dates = get_missing_dates(r'C:\Users\crees\OneDrive\Documents\Fun Analyst Projects\Baseball API\mlb_standings.csv', start_date)
    for day in missing_dates:
        
        print(F'Fetching MLB Standings for {day}')
        raw_data = fetch_standings(LEAGUE_IDS['NL'], day, SEASON)
        teams = parse_standings(raw_data, day)
        pd_df = pd.DataFrame(teams)

        save_to_csv(pd_df, r'C:\Users\crees\OneDrive\Documents\Fun Analyst Projects\Baseball API\mlb_standings.csv')


if __name__ == "__main__":
    main()