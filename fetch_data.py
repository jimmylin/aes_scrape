import requests
import json

def fetch_aes_data(tournament_id):
    url = f"https://www.advancedeventsystems.com/api/landing/events/{tournament_id}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(f"✅ Data fetched for tournament {tournament_id}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data for tournament {tournament_id}: {e}")
        return None

def fetch_division_data(tournament_id):
    url = f"https://www.advancedeventsystems.com/api/landing/events/{tournament_id}/divisions"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(f"✅ Division data fetched for tournament {tournament_id}")
        return data.get("value", [])
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching division data for tournament {tournament_id}: {e}")
        return []

def fetch_team_data(tournament_id):
    url = f"https://www.advancedeventsystems.com/api/landing/events/{tournament_id}/teams"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(f"✅ Team data fetched for tournament {tournament_id}")
        return data.get("value", [])
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching team data for tournament {tournament_id}: {e}")
        return []