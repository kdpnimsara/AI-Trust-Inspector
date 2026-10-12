# AI Trust Inspector - Model Doctor

import pandas as pd


def inspect_dataset(file_path):
    try:
        data = pd.read_csv(file_path)

        print("\n========================================")
        print("       AI TRUST INSPECTOR")
        print("           MODEL DOCTOR")
        print("========================================")

        print(f"\nNumber of rows: {data.shape[0]}")
        print(f"Number of columns: {data.shape[1]}")

        print("\nColumn names:")
        print(data.columns.tolist())

        print("\nMissing values:")
        print(data.isnull().sum())

        print("\nDuplicate rows:")
        print(data.duplicated().sum())

        print("\nData types:")
        print(data.dtypes)

        print("\nDataset inspection completed.")

    except FileNotFoundError:
        print("ERROR: Dataset file was not found.")

    except Exception as error:
        print(f"ERROR: {error}")


if __name__ == "__main__":
    inspect_dataset("data/sample_data.csv")