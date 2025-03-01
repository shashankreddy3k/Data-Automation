import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Define paths and constants
DATASET_NAME = "octopusteam/full-netflix-dataset"
SAVE_FOLDER = os.path.join(os.getcwd(), "Data")  # Save folder set to the GitHub repository directory
RAW_DATA_PATH = os.path.join(SAVE_FOLDER, "data.csv")  # Update if your dataset's file name changes
TRANSFORMED_DATA_PATH = os.path.join(SAVE_FOLDER, "transformed_dataset.csv")

# Step 1: Fetch the Dataset
def fetch_data():
    print("Fetching dataset...")
    # Set up Kaggle API credentials
    username = os.getenv('KAGGLE_USERNAME')
    key = os.getenv('KAGGLE_KEY')

    if not username or not key:
        raise ValueError("Environment variables KAGGLE_USERNAME or KAGGLE_KEY are not set.")

    # Initialize Kaggle API
    api = KaggleApi()
    api.authenticate()
    os.makedirs(SAVE_FOLDER, exist_ok=True)
    api.dataset_download_files(DATASET_NAME, path=SAVE_FOLDER, unzip=True)
    print(f"Dataset downloaded and saved in {SAVE_FOLDER}")

# Step 2: Clean the Dataset
def clean_data():
    print("\nCleaning dataset...")
    df = pd.read_csv(RAW_DATA_PATH)
    print(f"Initial row count: {df.shape[0]}")

    # Correct column names based on dataset
    required_columns = ['title', 'releaseYear', 'imdbAverageRating', 'imdbNumVotes']
    
    # Ensure all required columns exist
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in dataset: {missing_cols}")

    # Drop rows where essential columns are missing
    df = df.dropna(subset=required_columns)
    print(f"Row count after dropping nulls in critical columns: {df.shape[0]}")

    # Drop unnecessary columns
    columns_to_drop = ['imdbId', 'availableCountries']
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns], errors='ignore')
    print(f"Row count after dropping unnecessary columns: {df.shape[0]}")

    print("Cleaning completed.\n")
    return df

# Step 3: Transform the Dataset
def transform_data(df):
    print("\nTransforming dataset...")
    print(f"Row count before transformation: {df.shape[0]}")

    # Rename columns based on actual dataset
    rename_dict = {
        'title': 'Title',
        'type': 'Type',
        'genres': 'Genres',
        'releaseYear': 'Year',
        'imdbAverageRating': 'Rating',
        'imdbNumVotes': 'Votes'
    }
    df = df.rename(columns=rename_dict)

    # Handle missing genres before splitting
    df['Genres'] = df['Genres'].fillna('Unknown')

    # Split 'Genres' into multiple columns
    genres_split = df['Genres'].str.split(', ', expand=True)

    # Keep only the first genre and rename it to 'Genre'
    df['Genre'] = genres_split[0]  # Keep only the first genre

    # Drop unnecessary columns
    df = df.drop(columns=['Genres'], errors='ignore')

    # Convert 'Year' column to integer safely
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')  # Convert invalid years to NaN
    df = df.dropna(subset=['Year'])  # Drop rows where Year is NaN
    df['Year'] = df['Year'].astype('Int64')

    print(f"Row count after transformation: {df.shape[0]}")
    print("Transformation completed.\n")
    return df

# Step 4: Save the Transformed Dataset
def save_data(df):
    print("Saving dataset...")
    df.to_csv(TRANSFORMED_DATA_PATH, index=False)
    print(f"Transformed dataset saved successfully at {TRANSFORMED_DATA_PATH}")

# Main Pipeline Function
def main():
    try:
        # Step 1: Fetch the dataset
        fetch_data()
        
        # Step 2: Clean the dataset
        df_cleaned = clean_data()
        
        # Step 3: Transform the dataset
        df_transformed = transform_data(df_cleaned)
        
        # Step 4: Save the transformed dataset
        save_data(df_transformed)

        print("Pipeline executed successfully!")
    except Exception as e:
        print(f"Pipeline execution failed: {e}")

if __name__ == "__main__":
    main()
