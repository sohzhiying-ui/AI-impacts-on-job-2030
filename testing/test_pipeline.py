import pandas as pd

# Load dataset
file_path = '/content/drive/MyDrive/Agile Data Science PMA /AI_Impact_on_Jobs_2030.csv'
df = pd.read_csv(file_path)

# Automated validation: to check missing values
def validate_missing_values(dataframe):
    missing_report = dataframe.isnull().sum()
    print("Missing Values Report:\n", missing_report)
    if missing_report.sum() == 0:
        print(" No missing values detected.")
    else:
        print(" Missing values found. Please clean before modeling.")

# Run validation
validate_missing_values(df)
