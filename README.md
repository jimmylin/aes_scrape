# AES Scrape

A Python project designed to scrape data from the AES (Automated Export System) and process it for analysis.

## Features

- **Data Fetching**: Retrieve data from the AES.
- **Data Processing**: Process and analyze the fetched data.
- **CSV Export**: Export processed data to CSV format.

## Requirements

- Python 3.x
- `uv` package manager ([installation guide](https://github.com/astral-sh/uv))

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/jimmylin/aes_scrape.git
   cd aes_scrape
   ```

2. **Install Dependencies Using `uv`**:

   ```bash
   uv venv
   uv pip install -r requirements.txt
   ```

3. **Activate Virtual Environment**:

   ```bash
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```

## Usage

1. **Fetch Data**:

   Run the `fetch_data.py` script to retrieve data from the AES.

   ```bash
   python fetch_data.py
   ```

2. **Scrape Data**:

   Use the `scrape.py` script to process the fetched data.

   ```bash
   python scrape.py
   ```

3. **Hello Script**:

   The `hello.py` script is a simple example script.

   ```bash
   python hello.py
   ```

## Project Structure

- `fetch_data.py`: Script to fetch data from the AES.
- `scrape.py`: Script to process and analyze the fetched data.
- `hello.py`: Example script.
- `tournaments.csv`: Sample CSV file containing data.
- `.gitignore`: Specifies files and directories to be ignored by git.
- `.python-version`: Specifies the Python version used for the project.
- `pyproject.toml`: Contains project metadata and dependencies.
- `uv.lock`: Lock file for dependencies.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or suggestions, please open an issue in this repository.
