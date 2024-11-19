import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data_cleaning.csv.csv")

print(df.info())
print(df.describe())
print(df.head())

missing_values = df.isnull().sum()
print("Missing Values Per Column:")
print(missing_values)

# Visualize missing values with a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Before Cleaning')
plt.show()

# Histogram to check distributions
df.hist(bins=20, figsize=(10, 10), color='skyblue')
plt.suptitle('Data Distributions Before Cleaning')
plt.show()

df.fillna({'Email': "Unknown"}, inplace=True)
df.fillna({'Address': "Unknown"}, inplace=True)
df.fillna({'Avatar': "Unknown"}, inplace=True)
df.fillna({'Avg. Session Length': df['Avg. Session Length'].mean()}, inplace=True)
df.fillna({'Time on App': df['Time on App'].mean()}, inplace=True)
df.fillna({'Time on Website': df['Time on Website'].mean()}, inplace=True)
df.fillna({'Length of Membership': df['Length of Membership'].mean()}, inplace=True)
df.fillna({'Yearly Amount Spent': df['Yearly Amount Spent'].mean()}, inplace=True)

df.drop_duplicates(inplace=True)

print("Data Info After Cleaning:")
print(df.info())
print("Missing Values Per Column After Filling:")
print(df.isnull().sum())

# Histogram to check distributions after cleaning
df.hist(bins=20, figsize=(10, 10), color='lightgreen')
plt.suptitle('Data Distributions After Cleaning')
plt.show()

# Countplot for the 'Avatar' column
sns.countplot(x='Avatar', data=df)
plt.xticks(rotation=90)
plt.title('Avatar Count After Cleaning')
plt.show()






