import pandas as pd

df = pd.read_csv("titanic.csv")

# Missing values check
print(df.isnull().sum())

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Remove duplicates
df = df.drop_duplicates()

# Rename column
df = df.rename(columns={'Sex': 'Gender'})

# Save cleaned data
df.to_csv("cleaned_titanic.csv", index=False)

print("Data cleaned successfully!")