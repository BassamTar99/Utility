import pandas as pd
class Utility():
     def remove_duplicates(self, df):
        
        return df.drop_duplicates()

     def drop_columns(self, df, columns):
        
        return df.drop(columns=columns)

     def handle_missing_data(self, df, drop_columns=True):
        
        if drop_columns:
            return df.dropna(axis=1)  
        else:
            return df.dropna(axis=0)  
        
     def convert_to_datetime(self, df, column):
        
        df[column] = pd.to_datetime(df[column], errors='coerce')
        return df

     def trim_whitespace(self, df):
        
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.strip()
        return df

     def standardize_column_names(self, df):
        
        df.columns = [col.lower() for col in df.columns]
        return df

     def fill_missing_values(self, df, column, method='mean'):
        
        if method == 'mean':
            df[column].fillna(df[column].mean(), inplace=True)
        elif method == 'median':
            df[column].fillna(df[column].median(), inplace=True)
        elif method == 'mode':
            df[column].fillna(df[column].mode()[0], inplace=True)
        return df
     def encode_categorical_features(self, df, columns):
        """Encode categorical features using one-hot encoding."""
        return pd.get_dummies(df, columns=columns)

     def add_new_feature(self, df, new_column_name, calculation):
        """Add a new feature to the DataFrame based on a calculation."""
        df[new_column_name] = calculation(df)
        return df

     def feature_scaling(self, df, columns):
        """Scale features to a standard range (e.g., 0 to 1)."""
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
        df[columns] = scaler.fit_transform(df[columns])
        return df
     def normalize_data(self, df, columns):
        """Normalize data to have a mean of 0 and a standard deviation of 1."""
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        df[columns] = scaler.fit_transform(df[columns])
        return df

     def log_transformation(self, df, column):
        """Apply log transformation to a column to reduce skewness."""
        import numpy as np
        df[column] = np.log1p(df[column])  # log1p to handle log(0) cases
        return df
     def group_by_aggregation(self, df, group_by_column, agg_column, agg_func):
        """Group by a column and apply an aggregation function."""
        return df.groupby(group_by_column)[agg_column].agg(agg_func).reset_index()

     def cumulative_sum(self, df, column):
        """Compute the cumulative sum of a column."""
        df[f"{column}_cumsum"] = df[column].cumsum()
        return df
     def plot_histogram(self, df, column):
        """Plot a histogram of a specified column."""
        import matplotlib.pyplot as plt
        plt.hist(df[column].dropna(), bins=20, color='blue', edgecolor='black')
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

     def summary_statistics(self, df):
        """Generate summary statistics for the DataFrame."""
        return df.describe()

     def visualize_missing_data(self, df):
        """Visualize missing data in the DataFrame."""
        import seaborn as sns
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
        plt.title("Missing Data Visualization")
        plt.show()




util = Utility()


data = {
    "Name": [" Alice ", "Bob", None, "Alice"],
    "Age": [25, 30, None, 25],
    "Date": ["2021-01-01", "2021-01-02", None, "2021-01-01"],
    "Category": ["A", "B", "A", "C"]
}

df = pd.DataFrame(data)


print("Original DataFrame:")
print(df)


df = util.remove_duplicates(df)


df = util.drop_columns(df, columns=["Age"])

df = util.handle_missing_data(df, drop_columns=False)

df = util.convert_to_datetime(df, column="Date")


df = util.trim_whitespace(df)

df = util.standardize_column_names(df)

df = util.fill_missing_values(df, column="age", method='mean')

df = util.encode_categorical_features(df, columns=["category"])


df = util.add_new_feature(df, new_column_name="name_length", calculation=lambda x: x["name"].str.len())


df = util.feature_scaling(df, columns=["age"])
df = util.normalize_data(df, columns=["age"])


df = util.log_transformation(df, column="age")
grouped_df = util.group_by_aggregation(df, group_by_column="category", agg_column="age", agg_func="mean")
print("Grouped DataFrame:")
print(grouped_df)


df = util.cumulative_sum(df, column="age")
print("DataFrame with Cumulative Sum:")
print(df)


util.plot_histogram(df, column="age")

print("Summary Statistics:")
print(util.summary_statistics(df))

util.visualize_missing_data(df)

print("Processed DataFrame:")
print(df)
