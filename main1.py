
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_path = 'data.csv'  # Change this to the path of your CSV file
df = pd.read_csv(file_path)

# Set plot aesthetics
sns.set(style="whitegrid")
plt.figure(figsize=(15, 10))

# 1. Bar Plot: Distribution of EV models by brand
plt.subplot(2, 3, 1)
brand_count = df['Brand'].value_counts().head(10)  # Top 10 brands by model count
sns.barplot(x=brand_count.values, y=brand_count.index, palette="coolwarm")
plt.title("Top 10 Brands by Number of Models")
plt.xlabel("Number of Models")
plt.ylabel("Brand")

# 2. Scatter Plot: Price vs Range
plt.subplot(2, 3, 2)
sns.scatterplot(data=df, x='Range_Km', y='PriceEuro', hue='Segment', palette='viridis', s=80, alpha=0.7)
plt.title("Price vs Range of EVs")
plt.xlabel("Range (Km)")
plt.ylabel("Price (Euro)")

# 3. Histogram: Distribution of Acceleration Times
plt.subplot(2, 3, 3)
sns.histplot(df['AccelSec'], bins=10, kde=True, color='orange')
plt.title("Distribution of EV Acceleration Times")
plt.xlabel("Acceleration Time (0-100 km/h in sec)")
plt.ylabel("Frequency")

# 4. Box Plot: Price Comparison across Body Styles
plt.subplot(2, 3, 4)
sns.boxplot(data=df, x='BodyStyle', y='PriceEuro', palette="Set2")
plt.title("Price Comparison across Body Styles")
plt.xlabel("Body Style")
plt.ylabel("Price (Euro)")

# 5. Heatmap: Correlation between Numeric Features
plt.subplot(2, 3, 5)
corr_matrix = df[['AccelSec', 'TopSpeed_KmH', 'Range_Km', 'Efficiency_WhKm', 'FastCharge_KmH', 'PriceEuro']].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1, cbar_kws={'label': 'Correlation'})
plt.title("Correlation Heatmap")

# Adjust layout
plt.tight_layout()
plt.show()
