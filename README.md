# Insurance_Risk_Analytics_Predictive

📌 Overview

This project addresses a real-world insurance analytics challenge by analyzing South African insurance data to predict risk, evaluate claim patterns, and optimize pricing strategies. It applies end-to-end data science workflows from EDA to predictive modeling and dashboarding.
🎯 Objectives

    Perform data profiling and cleaning on policy, claim, and customer data.

    Analyze customer risk profiles and key features influencing claims.

    Build predictive models to estimate the probability of a claim.

    Conduct A/B testing for policy scenarios.

    Provide actionable recommendations for premium optimization.

    Visualize insights through interactive dashboards.

🛠️ Tools & Technologies

    Languages: Python

    Libraries:
    pandas, numpy, matplotlib, seaborn, plotly, scikit-learn, lifelines, xgboost, statsmodels, streamlit

    Version Control: Git + GitHub

    Data Tracking: DVC (Data Version Control)

    IDE: VS Code

📂 Project Structure

Insurance_Risk_Analytics_Predictive/
│── dvc
├── data/ # Raw and processed datasets
├── scr/ # Source code scripts
│ ├── eda/ # Exploratory data analysis
│ ├── preprocessing/ # Data cleaning & transformation
│ ├── modeling/ # ML model training and evaluation
│ ├── testing/ # A/B testing and statistical analysis
│ └── dashboard/ # Streamlit app code
│
├── notebooks/ # Jupyter notebooks for experiments
├── reports/ # Interim and final reports
├── dvc.yaml # DVC pipeline file
├── requirements.txt # Python dependencies
└── README.md # Project overview

🚀 How to Run

    Clone the Repository

git clone https://github.com/BetselotYitagesu/Insurance_Risk_Analytics_Predictive.git
cd Insurance_Risk_Analytics_Predictive

Set Up Virtual Environment

python -m venv venv
source venv/bin/activate # or venv\Scripts\activate (Windows)
pip install -r requirements.txt

Reproduce the Pipeline

dvc repro

Run Dashboard (Optional)

    streamlit run scr/dashboard/app.py

📊 Progress Summary

    ✅ Data ingestion, profiling, and cleaning

    ✅ Exploratory data analysis

    ✅ Risk profiling and feature analysis

    🔄 In progress: Predictive modeling, A/B testing

    🔜 Next: Premium optimization, dashboard, final report

📌 Key Findings (So Far)

    Risk is highly influenced by age, policy tenure, and claim history.

    Some customers are overpaying or underpaying based on misaligned premiums.

    High-risk patterns exist in younger age groups with multiple claims.

📃 License

This project is part of the 10 Academy training program and intended for educational and research purposes only.
