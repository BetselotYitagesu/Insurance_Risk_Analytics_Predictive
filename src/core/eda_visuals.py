"""EDA Visualization Fucntion """

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('data/processed/cleaned_insurance_clean.csv')
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Policy_Type', hue='Claim')
plt.title('Claim Distribution by Policy Type')
plt.xlabel('Policy Type')
plt.ylabel('Count')
plt.legend(title='Claim', labels=['No', 'Yes'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/figures/claim_by_policy_type.png')
plt.show()
