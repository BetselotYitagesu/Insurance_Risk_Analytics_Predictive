import pandas as pd
import os
from core.cleaning import clean_insurance_data

# Define paths
input_path = 'data/raw/insurance_data.csv'
output_path = 'data/processed/cleaned_insurance_data.csv'


def main():
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"{input_path} not found")

    # Load, clean, and save
    df = pd.read_csv(input_path, on_bad_lines='skip')
    cleaned_df = clean_insurance_data(df)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cleaned_df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}")


if __name__ == '__main__':
    main()
