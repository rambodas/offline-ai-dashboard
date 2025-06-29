import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2024-06-01", end="2024-06-30")

data = pd.DataFrame({
    'date': dates,
    'GMV': np.random.normal(loc=5000000, scale=300000, size=len(dates)).round(0),
    'DAU': np.random.normal(loc=100000, scale=5000, size=len(dates)).round(0),
    'CVR': np.random.normal(loc=2.5, scale=0.15, size=len(dates)).round(2)
})

categories = ['Electronics', 'Fashion', 'Grocery']
for category in categories:
    ratio = np.random.uniform(0.2, 0.5)
    data[category + '_GMV'] = (data['GMV'] * ratio).round(0)

data.to_csv('dummy_business_data.csv', index=False)
print("✅ Dummy data created and saved as dummy_business_data.csv")