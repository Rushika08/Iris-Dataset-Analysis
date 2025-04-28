# Pairwise Attribute Visualization

![Scatter Plot Example](https://github.com/Rushika08/Iris-Dataset-Analysis/blob/main/Plots.png)

## Description

Each attribute is plotted against every other attribute to explore pairwise relationships.

- When an attribute is plotted against a different attribute, a scatter plot is used to visualize the relationship between the two variables.
- When an attribute is plotted against itself, a scatter plot would not be informative since all points would lie on a straight line. 
- Therefore, on the diagonal, a **density plot** (a smooth version of a histogram) is displayed to visualize the **distribution** and **probability density function** (PDF) of that attribute.

This approach provides a comprehensive view of how each feature interacts with others and how each feature is distributed individually.

## Conclusion

By observing the plots, we can clearly see there are three distinct clusters:

- The **Setosa** species (blue color) forms a very distinct and separate cluster.
- The **Versicolor** (orange color) and **Virginica** (green color) species have overlapping regions but still display patterns of separation.

Thus, based on the visual grouping, we can conclude that there are **three natural clusters**, which correctly match the **known number of species**.
