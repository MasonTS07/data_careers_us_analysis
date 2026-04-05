import pandas as pd

# Import Raw Data File
df = pd.read_excel('all_data_M_2024.xlsx')

# Selected columns for analysis
cols_to_keep = [
    'AREA', 'AREA_TITLE', 'AREA_TYPE', 'PRIM_STATE', 'NAICS', 'NAICS_TITLE', 'OWN_CODE',
    'OCC_CODE', 'OCC_TITLE', 'TOT_EMP', 'JOBS_1000', 'LOC_QUOTIENT', 'H_MEAN', 'A_MEAN',
    'H_PCT10', 'H_PCT25', 'H_MEDIAN', 'H_PCT75', 'H_PCT90', 'A_PCT10', 'A_PCT25', 'A_MEDIAN',
    'A_PCT75', 'A_PCT90'
    ]

# Updating df to include only selected columns
df = df[cols_to_keep]

# # Checking if columns are in the correct format
# print(df.dtypes)

# Selecting only numeric columns for formatting
numeric_cols = [
    'TOT_EMP', 'JOBS_1000', 'LOC_QUOTIENT', 'H_MEAN', 'A_MEAN',
    'H_PCT10', 'H_PCT25', 'H_MEDIAN', 'H_PCT75', 'H_PCT90',
    'A_PCT10', 'A_PCT25', 'A_MEDIAN', 'A_PCT75', 'A_PCT90'
    ]

# Replacing special characters with NA
df[numeric_cols] = df[numeric_cols].replace(['*', '**', '#', '~'], pd.NA)
# Converting columns to numeric
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# # Confirming numeric columns
# print(df[numeric_cols].dtypes)

# Selecting only data related roles
data_roles = [
    '13-1161',  # Market Research Analysts
    '15-1242',  # Database Administrators
    '15-1243',  # Database Architects
    '15-2031',  # Operations Research Analysts
    '15-2051',  # Data Scientists
]

# Updating df to include only data related roles
df = df[df['OCC_CODE'].isin(data_roles)]

# print(df.shape)
# print(df['OCC_TITLE'].value_counts())
# print(df['AREA_TYPE'].value_counts())
# print(df.groupby('AREA_TYPE')['AREA_TITLE'].first())

# Dropping U.S. territories due to small sample size
df = df[df['AREA_TYPE'] != 3]

# # Confirming dropped territories
# print(df.shape)
# print(df['AREA_TYPE'].value_counts())

# Selecting only salary columns
salary_cols = [
    'A_MEDIAN', 'A_MEAN', 'A_PCT10', 'A_PCT25', 'A_PCT75',
    'A_PCT90', 'TOT_EMP', 'LOC_QUOTIENT'
    ]

# # Checking missing value counts in salary columns
# print(df[salary_cols].isna().sum())
# print(f"\nTotal rows: {df.shape[0]}")

# Dropping rows with important salary information missing
df = df.dropna(subset=['A_MEDIAN', 'A_MEAN', 'TOT_EMP'])

# # Confirming number of dropped rows
# print(df.shape)

# Exporting cleaned data file
df.to_csv('BLS_Data_Roles_Cleaned.csv', index=False)

print("Export Complete")
print(df.shape)