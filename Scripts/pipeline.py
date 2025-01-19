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
    print("Cleaning dataset...")
    df = pd.read_csv(RAW_DATA_PATH)
    # Remove rows with missing values
    df = df.dropna()
    # Drop unnecessary columns
    df = df.drop(['availableCountries', 'imdbId'], axis=1)
    print("Cleaning completed.")
    return df

# Step 3: Transform the Dataset
def transform_data(df):
    print("Transforming dataset...")
    # Rename columns
    df.columns = ['Title', 'Type', 'Genres', 'Year', 'Rating', 'Votes']
    # Split the 'Genres' column into separate columns
    genres_split = df['Genres'].str.split(', ', expand=True)
    genres_split.columns = [f"Genre_{i+1}" for i in range(genres_split.shape[1])]
    df = pd.concat([df, genres_split], axis=1)
    # Convert 'Year' column to integer
    df['Year'] = df['Year'].astype('Int64')
    print("Transformation completed.")
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
