# pipeline_ingestion.py
import pandas as pd
import sqlite3

def ingest_and_clean(csv_file, db_file):
    # Load CSV data
    df = pd.read_csv(csv_file)
    # Data cleaning: remove rows with missing values and standardize text
    df.dropna(subset=['log_message'], inplace=True)
    df['log_message'] = df['log_message'].str.lower().str.strip()
    # Connect to SQLite database and store cleaned data
    conn = sqlite3.connect(db_file)
    df.to_sql('logs', conn, if_exists='replace', index=False)
    conn.close()
    print("Data ingested and stored successfully.")

if __name__ == "__main__":
    ingest_and_clean('data/log_data.csv', 'data/logs.db')
