# AES Tournament Scraper

This script retrieves tournament event details from Advanced Event Systems (AES), including the number of registered teams for Open Boys divisions across various age groups. It formats the data and writes it to both a CSV file and a Google Sheets document.

## Prerequisites

Ensure you have the following installed:
- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (a fast Python package manager)

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install dependencies using `uv`:
   ```sh
   uv venv
   uv pip install -r requirements.txt
   ```

## Setup

1. Obtain AES API credentials (if required) and Google Sheets API credentials.
2. Create a Google Service Account and download the credentials file as `credentials.json`.
3. Place the `credentials.json` file in the project root.
4. Share the **AES Data** Google Sheet with the Service Account's email address to grant it access.

## Usage

Run the script with a list of tournament event IDs:
```sh
uv pip run scrape.py <tournament_id_1> <tournament_id_2> ...
```

### Example:
```sh
uv pip run scrape.py 12345 67890
```

This will:
- Fetch tournament data from AES.
- Extract team registration details for Open Boys divisions.
- Save the results to `tournaments.csv`.
- Upload the data to a Google Sheets document named **"AES Data"** under the **"Tournaments"** worksheet.

## Output
- **CSV File**: `tournaments.csv` in the project directory.
- **Google Sheets**: Data written to the "AES Data" spreadsheet under the "Tournaments" worksheet.

## Troubleshooting
- Ensure your `credentials.json` file is correctly configured.
- Verify `uv` is installed and available in your environment.
- Ensure the Google Service Account has been shared access to the **AES Data** Google Sheet.
- Check for API rate limits or connectivity issues if data fetching fails.

## License
This project is licensed under the MIT License.

