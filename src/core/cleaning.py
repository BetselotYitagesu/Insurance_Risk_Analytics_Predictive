"""Clean insurance dataset by handling missing values and dropping noisy"""


def clean_insurance_data(df):
    """Clean insurance dataset by handling missing values and dropping noisy"""

    # Drop columns with excessive missing values
    df = df.drop(columns=['Rebuilt', 'Converted'], errors='ignore')
    df = df.drop(columns=['WrittenOff'], errors='ignore')

    # Normalize CrossBorder if it exists
    if 'CrossBorder' in df.columns:
        df['CrossBorder'] = df['CrossBorder'].fillna('No')
        df['CrossBorder'] = df['CrossBorder'].map({'Yes': 1, 'No': 0})
    # Handle NewVehicle values
    if 'NewVehicle' in df.columns:
        df['NewVehicle'] = df['NewVehicle'].fillna('Unknown')
        df['NewVehicle'] = df['NewVehicle'].map({
            'Less than 6 months': 'Yes',
            'More than 6 months': 'No',
            'Unknown': 'Unknown'
            })

    # Fill categorical values with mode
    for col in ['Gender', 'MaritalStatus', 'VehicleType']:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].mode()[0])

    # Fill numeric estimate with median
    if 'CustomValueEstimate' in df.columns:
        med = df['CustomValueEstimate'].median()
        df['CustomValueEstimate'] = df['CustomValueEstimate'].fillna(med)

    # Drop rows where CapitalOutstanding is missing
    if 'CapitalOutstanding' in df.columns:
        df = df.dropna(subset=['CapitalOutstanding'])

    # Handle remaining missing values
    for col in ['VehicleIntroDate', 'NumberOfDoors', 'mmcode', 'bodytype']:
        if col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].fillna(df[col].mode()[0])
            else:
                df[col] = df[col].fillna(df[col].median())

    return df
