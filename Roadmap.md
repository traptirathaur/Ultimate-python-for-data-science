When we use python for data science, it typically involves a focused task, such as data cleaning, analysis, viz, or building a simple ML model. The structure varies on the specific project but a common outline includes;

### Import Libraries; 
Load necessary libraries like pandas for data manipulation, numpy for numerical operations, matplotlib or seaborn for visualization, and scikit-learn for machine learning.

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error

  ### Load Data: 
  Read the dataset into a pandas DataFrame. This could be from a CSV, Excel, or other data sources.
