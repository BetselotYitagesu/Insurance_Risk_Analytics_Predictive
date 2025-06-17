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

📊 Task 3: A/B Testing & Statistical Analysis
Objective

To statistically assess whether different customer or policy groups exhibit significant differences in claim behavior, using hypothesis testing and visual analysis.
Key Steps

    Exploratory Comparisons: Analyzed claim distribution by Policy_Type, VehicleClass, and Product.

    Statistical Tests:

        Applied t-tests and ANOVA to compare means of TotalClaims across groups.

        Used chi-square tests to assess independence between categorical variables like Claim and Policy_Type.

    Visualization:

        Countplots and boxplots created using seaborn and matplotlib to visualize group-level differences.

    Interpretation:

        Results helped identify segments with significantly higher claim rates.

Output

    Statistical test results and visualizations included in notebooks/task-3-ab-testing.ipynb.

    Insights used to inform modeling strategies in Task 4.

🤖 Task 4: Predictive Modeling & Premium Optimization
Objective

To predict the claim severity (TotalClaims) using machine learning models, with the goal of optimizing premiums and minimizing risk.
Data Preparation

    Feature Engineering:

        Filtered dataset for policies where TotalClaims > 0.

        Encoded categorical features using OneHotEncoder.

    Train/Test Split:

        Split into 80% training and 20% testing sets.

Models Trained

    Linear Regression

    Random Forest Regressor

    Gradient Boosting Regressor

Performance (RMSE)
Model RMSE
Linear Regression 36,968.67
Random Forest Regressor 36,433.03
Gradient Boosting 35,634.86 ✅
Deliverables

    All modeling code is in notebooks/task-4-modeling.ipynb.

    Final trained models saved under models/ using joblib.

📃 License

This project is part of the 10 Academy training program and intended for educational and research purposes only.
