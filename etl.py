import os
import requests
import pandas as pd


API_URL = "https://jsonplaceholder.typicode.com/users"


def extract_data():
    """
    Extract user data from the REST API.
    """
    print("Extracting data from REST API...")

    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    data = response.json()

    print(f"Successfully extracted {len(data)} records.")
    return data


def transform_data(data):
    """
    Transform the extracted data using pandas.
    """
    print("Transforming data...")

    if not data:
        return pd.DataFrame()

    df = pd.DataFrame(data)

    # Select required columns
    df = df[
        [
            "id",
            "name",
            "username",
            "email",
            "phone",
            "website",
            "address",
            "company",
        ]
    ].copy()

    # Extract city from nested address data
    df["city"] = df["address"].apply(
        lambda x: x.get("city", "Unknown")
        if isinstance(x, dict)
        else "Unknown"
    )

    # Extract company name from nested company data
    df["company_name"] = df["company"].apply(
        lambda x: x.get("name", "Unknown")
        if isinstance(x, dict)
        else "Unknown"
    )

    # Convert email addresses to lowercase
    df["email"] = df["email"].str.lower()

    # Remove unnecessary nested columns
    df = df.drop(columns=["address", "company"])

    # Rename columns for better readability
    df = df.rename(
        columns={
            "id": "user_id",
            "name": "full_name",
        }
    )

    # Remove duplicate records
    df = df.drop_duplicates(subset=["user_id"])

    print("Data transformation completed.")

    return df


def load_data(df, output_file="output/users.csv"):
    """
    Load the transformed data into a CSV file.
    """
    print("Loading data into CSV...")

    # Create output folder if it does not exist
    output_directory = os.path.dirname(output_file)

    if output_directory:
        os.makedirs(output_directory, exist_ok=True)

    df.to_csv(output_file, index=False)

    print(f"Data successfully saved to {output_file}")


def run_pipeline():
    """
    Run the complete ETL pipeline.
    """
    print("\n--- ETL Pipeline Started ---\n")

    data = extract_data()

    transformed_data = transform_data(data)

    load_data(transformed_data)

    print("\n--- ETL Pipeline Completed Successfully ---")

    print("\nTransformed Data:")
    print(transformed_data)

    return transformed_data


if __name__ == "__main__":
    run_pipeline()