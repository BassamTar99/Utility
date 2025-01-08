"""Utility
# The Utility class provides a collection of methods for data preprocessing, cleaning, transformation,and visualization to simplify common data handling tasks in pandas DataFrames.
Functions:
   1.	remove_duplicates: If you want to remove duplicate rows.
   2.	drop_columns: If you want to drop specific columns from the DataFrame.
   3.	handle_missing_data: If you want to handle missing data by dropping rows or columns.
   4.	convert_to_datetime: If you want to convert a column to datetime format.
   5.	trim_whitespace: If you want to remove leading and trailing whitespaces from text columns.
   6.	standardize_column_names: If you want to convert all column names to lowercase for consistency.
   7.	fill_missing_values: If you want to fill missing values using mean, median, or mode.
   8.	encode_categorical_features: If you want to apply one-hot encoding to categorical columns.
   9.	add_new_feature: If you want to add a new feature based on a custom calculation.
   10.	feature_scaling: If you want to scale numerical features to a range, e.g., 0 to 1.
   11.	normalize_data: If you want to normalize numerical columns to have a mean of 0 and standard deviation of 1.
   12.	log_transformation: If you want to apply a log transformation to reduce skewness.
   13.	group_by_aggregation: If you want to group data by a column and apply an aggregation function.
   14.	cumulative_sum: If you want to calculate the cumulative sum of a column.
   15.	plot_histogram: If you want to visualize the distribution of a column with a histogram.
   16.	summary_statistics: If you want to get summary statistics like mean, median, etc.
   17.	visualize_missing_data: If you want to visualize missing data in the DataFrame using a heatmap.
   18.	load_data_from_csv: If you want to load a DataFrame from a CSV file.
   19.	load_data_to_csv: If you want to save a DataFrame to a CSV file.
   20.	check_missing_values: If you want to check for missing values in the DataFrame.
   21.	check_duplicates: If you want to check for duplicate rows in the DataFrame.
   22.	get_column_data_types: If you want to retrieve the data types of all columns.
       
 Requirements:
    - pandas: For data manipulation and analysis.
    - numpy: For numerical operations like logarithmic transformations.
    - matplotlib: For data visualization (e.g., histograms).
    - seaborn: For advanced visualizations (e.g., missing data heatmaps).
    - scikit-learn: For scaling and normalizing data.

List of Features:
    - Data Cleaning: Remove duplicates, handle missing data, and standardize column names.
    - Data Transformation: Convert data types, scale, normalize, and apply log transformations.
    - Feature Engineering: Add new features, encode categorical variables, and compute cumulative sums.
    - Aggregation: Group data and apply aggregation functions.
    - Visualization: Plot histograms and visualize missing data.
    - File Handling: Load data from and save data to CSV files.
    - Inspection: Check missing values, duplicates, and column data types.
