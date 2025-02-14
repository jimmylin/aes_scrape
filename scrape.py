import requests
import json
import csv
from fetch_data import fetch_aes_data, fetch_division_data, fetch_team_data
import sys
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def format_date_csv(date_str):
    if date_str:
        try:
            return date_str.split("T")[0]
        except ValueError:
            return None
    return None

def extract_age_group(division_name):
    match = re.search(r'\b(\d{2})[U]?\b', division_name)
    return match.group(1) if match else division_name

def get_max_teams(divisions):
    for div in divisions:
        if "open" in div.get("description", "").lower():
            return div.get("maximumTeams", "N/A")
    for div in divisions:
        if "boys" in div.get("description", "").lower():
            return div.get("maximumTeams", "N/A")
    for div in divisions:
        if "mixed" in div.get("description", "").lower():
            return div.get("maximumTeams", "N/A")
    return "N/A"

def write_to_csv(filename, tournament_list):
    division_headers = set()
    tournament_data = []
    
    for data in tournament_list:
        divisions = fetch_division_data(data.get("eventId"))
        teams = fetch_team_data(data.get("eventId"))
        division_counts = {}
        entry_fee = ""
        max_teams = get_max_teams(divisions)
        
        for div in divisions:
            if "open" in div.get("description", "").lower():
                age_group = extract_age_group(div.get("description", "Unknown Division"))
                registered_teams = sum(1 for team in teams if (team.get("eventDivisionAssignmentId") == div.get("eventDivisionAssignmentId") and team.get("acceptedType", {}).get("displayName", "Unknown") == "Accepted"))
                division_counts[age_group] = f"{registered_teams}/{div.get('maximumTeams', 'N/A')}"
                division_headers.add(age_group)
                if not entry_fee:
                    entry_fee = div.get("entryFee", "")
            elif "boys" in div.get("description", "").lower():
                age_group = extract_age_group(div.get("description", "Unknown Division"))
                registered_teams = sum(1 for team in teams if (team.get("eventDivisionAssignmentId") == div.get("eventDivisionAssignmentId") and team.get("acceptedType", {}).get("displayName", "Unknown") == "Accepted"))
                division_counts[age_group] = f"{registered_teams}/{div.get('maximumTeams', 'N/A')}"
                division_headers.add(age_group)
                if not entry_fee:
                    entry_fee = div.get("entryFee", "")
            elif "mixed" in div.get("description", "").lower():
                age_group = extract_age_group(div.get("description", "Unknown Division"))
                registered_teams = sum(1 for team in teams if (team.get("eventDivisionAssignmentId") == div.get("eventDivisionAssignmentId") and team.get("acceptedType", {}).get("displayName", "Unknown") == "Accepted"))
                division_counts[age_group] = f"{registered_teams}/{div.get('maximumTeams', 'N/A')}"
                division_headers.add(age_group)
                if not entry_fee:
                    entry_fee = div.get("entryFee", "")
        
        address_obj = data.get("address", {})
        address = f"{address_obj.get('line1', '')}, {address_obj.get('city', '')}, {address_obj.get('state', {}).get('abbreviation', '')} {address_obj.get('zip', '')}"
        address = address.replace(" ", "+") if isinstance(address, str) and address.strip() else ""
        
        row = {
            "Tournament ID": f"=HYPERLINK(\"https://aes2.advancedeventsystems.com/events/{data.get('eventId')}\", \"{data.get('eventId')}\")",
            "Tournament Name": data.get("name"),
            "Location": f"=HYPERLINK(\"https://www.google.com/maps/search/?api=1&query={address}\", \"{data.get('locationName', 'Unknown Location')}\")",
            "Start Date": format_date_csv(data.get("startDate")),
            "End Date": format_date_csv(data.get("endDate")),
            "Registration Opens": format_date_csv(data.get("registrationOpenDate")),
            "Registration Closes": format_date_csv(data.get("registrationCloseDate")),
            "Late Registration": format_date_csv(data.get("lateRegistrationDate")),
            "Entry Fee": entry_fee
        }
        row.update(division_counts)
        tournament_data.append(row)
    
    headers = ["Tournament ID", "Tournament Name", "Location", "Start Date", "End Date", "Registration Opens", "Registration Closes", "Late Registration", "Entry Fee"] + sorted(division_headers)
    
    print(f"✅ Data successfully written to {filename}")
    write_to_google_sheets(tournament_data, headers)

def write_to_google_sheets(data, headers):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    
    spreadsheet = client.open("AES Data")
    try:
        sheet = spreadsheet.worksheet("Tournaments")
    except gspread.exceptions.WorksheetNotFound:
        sheet = spreadsheet.add_worksheet(title="Tournaments", rows="1000", cols="20")
    
    sheet.clear()
    sheet.append_row(headers)
    
    for row in data:
        sheet.append_row([row.get(header, "") for header in headers], value_input_option="USER_ENTERED")
    
    print("✅ Data successfully written to Google Sheets")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scrape.py <tournament_id_1> <tournament_id_2> ...")
        sys.exit(1)
    
    tournament_ids = sys.argv[1:]
    all_tournament_data = []

    for tournament_id in tournament_ids:
        data = fetch_aes_data(tournament_id)
        if data:
            all_tournament_data.append(data)
    
    if all_tournament_data:
        write_to_csv("tournaments.csv", all_tournament_data)