import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load IPL dataset
ipl = pd.read_csv('/content/drive/MyDrive/ipl_data.csv')
df = ipl

# Histogram of Total Scores
plt.figure(figsize=(10, 6))
plt.hist(df['total'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Total Scores')
plt.xlabel('Total Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Drop unnecessary features
df = ipl.drop(['date', 'runs', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5','mid', 'striker', 'non-striker'], axis=1)

# Split features and target variable
X = df.drop(['total'], axis=1)
y = df['total']
