# 🎬 Data Automation Pipeline for Movie Dataset

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.0%2B-brightgreen)
![License](https://img.shields.io/badge/License-MIT-orange)

A robust data automation pipeline for fetching, cleaning, and transforming movie data. This repository automates the end-to-end process of preparing structured movie datasets for analysis or integration into applications like recommendation systems.

---


## 🚀 Features

- **Automated Data Fetching**: Pulls data from sources (e.g., Kaggle) or processes local files.
- **Data Cleaning**:
  - Handles missing values (e.g., empty `availableCountries`).
  - Standardizes formats (genres, release years).
- **Data Transformation**:
  - Filters or aggregates data (e.g., IMDb ratings > 7.0).
  - Generates enriched datasets (e.g., decade categorization).
- **CI/CD Integration**: Automated workflows via GitHub Actions.

---

## ⚙️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shashankreddy3k/shashankreddy3k-data-automation.git
   cd shashankreddy3k-data-automation
Install Dependencies:

bash
pip install -r requirements.txt
Kaggle API Setup (if fetching data from Kaggle):

Follow Kaggle’s API documentation to set up credentials.

---
## 🛠 Usage

1. Running the Pipeline Locally
Execute the main transformation script:

bash
python Scripts/"Data fetching cleaning and transformation.py"
2. Pipeline Outputs
Raw Data: Data/data.csv

Transformed Data: Data/transformed_dataset.csv

3. Sample Data Schema (data.csv)
Column	Description	Example Value
title	Movie title	"Forrest Gump"
type	Media type (movie/TV)	"movie"
genres	Genre tags	"Drama, Romance"
releaseYear	Year of release	1994
imdbId	IMDb identifier	"tt0109830"
imdbAverageRating	IMDb average rating (0-10)	8.8
imdbNumVotes	Number of IMDb votes	2,367,290
availableCountries	Countries where available (optional)	"US,UK"

---
## 🔄 Workflow Automation (GitHub Actions)
The .github/workflows/main.yml file automates:

Scheduled Runs: Daily/weekly data refreshes.

Data Validation: Checks for schema consistency.

Error Handling: Alerts for missing fields or failed transformations.

---
## 📊 Data Sources
Primary Dataset: Data/data.csv (static file).

External Sources: Optional integration with Kaggle datasets using the Kaggle API.

---
## 🤝 Contributing
Fork the repository.

Create a branch: git checkout -b feature/your-feature.

Commit changes: git commit -m "Add your feature".

Push to the branch: git push origin feature/your-feature.

Open a Pull Request.

---
## 📜 License
Distributed under the MIT License. See LICENSE for details.

---
## 🙏 Acknowledgements
Dataset inspired by IMDb and Kaggle.

Built with Pandas and GitHub Actions.
