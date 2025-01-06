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


util = Utility()


data = {
    "Name": [" Alice ", "Bob", None, "Alice"],
    "Age": [25, 30, None, 25],
    "Date": ["2021-01-01", "2021-01-02", None, "2021-01-01"]
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

print("Processed DataFrame:")
print(df)
