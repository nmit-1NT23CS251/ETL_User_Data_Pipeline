# ETL User Data Pipeline

A simple ETL (Extract, Transform, Load) pipeline built using Python. The project fetches user data from a REST API, transforms the data using Pandas, saves the processed data into a CSV file, and uses Pytest for unit testing.

## Features

- Fetches user data from a REST API
- Converts JSON data into a Pandas DataFrame
- Extracts city and company information from nested data
- Converts email addresses to lowercase
- Renames columns for better readability
- Removes duplicate records
- Saves the transformed data into a CSV file
- Includes unit tests using Pytest

## Technologies Used

- Python
- Pandas
- Requests
- Pytest
- REST API
- CSV

## ETL Process

### 1. Extract
The data is fetched from the JSONPlaceholder Users REST API using the Python `requests` library.

### 2. Transform
The extracted JSON data is converted into a Pandas DataFrame and cleaned. The transformation includes extracting nested city and company information, normalizing email addresses, renaming columns, and removing duplicates.

### 3. Load
The transformed data is saved as a CSV file inside the `output` folder.

## Project Structure

```text
ETL_User_Data_Pipeline/
│
├── output/
│   └── users.csv
├── etl.py
├── test_etl.py
├── requirements.txt
└── README.md
```

## Installation

Install the required Python packages:

```bash
python3 -m pip install -r requirements.txt
```

## Running the ETL Pipeline

Run the following command:

```bash
python3 etl.py
```

The processed data will be saved to:

```text
output/users.csv
```

## Running the Tests

Run the unit tests using:

```bash
python3 -m pytest -v
```

The tests verify:

- REST API data extraction
- DataFrame creation
- Expected output columns
- Email normalization
- City extraction
- Company extraction
- Empty data handling
- CSV file creation
- CSV content

## Output Columns

The generated CSV file contains:

- `user_id`
- `full_name`
- `username`
- `email`
- `phone`
- `website`
- `city`
- `company_name`

## Conclusion

This project demonstrates a basic ETL workflow using Python. It extracts data from a REST API, cleans and transforms the data using Pandas, loads the final data into a CSV file, and uses Pytest to verify that the pipeline works correctly.
