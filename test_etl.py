import os
import pandas as pd

from etl import extract_data, transform_data, load_data


def sample_data():
    return [
        {
            "id": 1,
            "name": "John Doe",
            "username": "john",
            "email": "JOHN@EXAMPLE.COM",
            "phone": "1234567890",
            "website": "john.com",
            "address": {
                "city": "Bangalore"
            },
            "company": {
                "name": "TechNova"
            }
        }
    ]


def test_extract_data():
    data = extract_data()

    assert isinstance(data, list)
    assert len(data) > 0


def test_transform_returns_dataframe():
    data = sample_data()

    df = transform_data(data)

    assert isinstance(df, pd.DataFrame)


def test_transformed_columns():
    data = sample_data()

    df = transform_data(data)

    expected_columns = [
        "user_id",
        "full_name",
        "username",
        "email",
        "phone",
        "website",
        "city",
        "company_name"
    ]

    assert list(df.columns) == expected_columns


def test_email_is_lowercase():
    data = sample_data()

    df = transform_data(data)

    assert df.iloc[0]["email"] == "john@example.com"


def test_city_extraction():
    data = sample_data()

    df = transform_data(data)

    assert df.iloc[0]["city"] == "Bangalore"


def test_company_extraction():
    data = sample_data()

    df = transform_data(data)

    assert df.iloc[0]["company_name"] == "TechNova"


def test_empty_data():
    df = transform_data([])

    assert isinstance(df, pd.DataFrame)
    assert df.empty


def test_load_data(tmp_path):
    data = sample_data()

    df = transform_data(data)

    output_file = tmp_path / "test_users.csv"

    load_data(df, str(output_file))

    assert os.path.exists(output_file)


def test_loaded_csv_content(tmp_path):
    data = sample_data()

    df = transform_data(data)

    output_file = tmp_path / "test_users.csv"

    load_data(df, str(output_file))

    loaded_df = pd.read_csv(output_file)

    assert len(loaded_df) == 1
    assert loaded_df.iloc[0]["full_name"] == "John Doe"