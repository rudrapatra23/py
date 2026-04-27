import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('student_data.csv')
mean_marks = df['Marks'].mean()
max_marks = df['Marks'].max()
min_marks = df['Marks'].min()
std_dev = df['Marks'].std()

print("Student Data Analysis")
print(f"Mean Marks: {mean_marks:.2f}")
print(f"Maximum Marks: {max_marks}")
print(f"Minimum Marks: {min_marks}")
print(f"Standard Deviation: {std_dev:.2f}\n")

sns.set_theme(style="whitegrid")
plt.figure(figsize=(15, 10))


plt.subplot(2, 2, 1)
sns.lineplot(x='Name', y='Marks', data=df, marker='o', color='b')
plt.title('Line Plot: Name vs Marks')
plt.xticks(rotation=45)

plt.subplot(2, 2, 2)
sns.barplot(x='Name', y='Marks', data=df, palette='viridis')
plt.title('Bar Chart: Name vs Marks')
plt.xticks(rotation=45)

plt.subplot(2, 2, 3)
sns.histplot(df['Marks'], bins=5, kde=True, color='purple')
plt.title('Histogram: Marks Distribution')

plt.subplot(2, 2, 4)
sns.scatterplot(x='Age', y='Marks', data=df, s=100, color='red')
plt.title('Scatter Plot: Age vs Marks')

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))

correlation_matrix = df.select_dtypes(include=['number']).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap: Correlation Matrix')
plt.show()

sns.pairplot(df, diag_kind='kde', markers='+')
plt.suptitle('Pair Plot: Relationships Between All Variables', y=1.02)
plt.show()