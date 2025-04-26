# Importing the matplotlib library for plotting graphs and visualizations
import matplotlib.pyplot as plt
# Importing seaborn for enhanced data visualizations, especially for statistical plots
import seaborn as sns
# Importing the iris dataset from sklearn (a built-in dataset for classification tasks)
from sklearn.datasets import load_iris
# Importing pandas to create and manipulate DataFrames (tabular data structures)
import pandas as pd


# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Display the first few rows of the DataFrame
print(df.head(5))

# Display the target variable (species) and target names
print(iris.target[:100])
print(iris.target_names)

# Add the target variable to the DataFrame as a new column
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Scatter plot matrix
sns.set(style="whitegrid")
sns.pairplot(df, hue='species', markers=["o", "s", "D"])

# Show the plot
plt.suptitle("Iris Dataset Feature Comparison", y=1.02)
plt.show()
