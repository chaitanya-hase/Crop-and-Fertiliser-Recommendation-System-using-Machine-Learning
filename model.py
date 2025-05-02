import pandas as pd 
import numpy as np

crop_df = pd.read_csv('crop.csv') 
print("Shape of dataset:", crop_df.shape)
print("\nFirst 5 rows:\n", crop_df.head())
print("\nLast 5 rows:\n", crop_df.tail())
print("\nNull values in each column:\n", crop_df.isnull().sum())
print("\nSummary statistics:\n", crop_df.describe())
print("\nData types:\n", crop_df.dtypes)
print("\nUnique crops:\n", crop_df['label'].unique())



fertilizer_df = pd.read_csv('fertilizer.csv')  
print("Shape of dataset:", fertilizer_df.shape)
print("\nFirst 5 rows:\n", fertilizer_df.head())
print("\nLast 5 rows:\n", fertilizer_df.tail())
print("\nNull values in each column:\n", fertilizer_df.isnull().sum())
print("\nSummary statistics:\n", fertilizer_df.describe())
print("\nData types:\n", fertilizer_df.dtypes)
print("\nUnique Crop Types:\n", fertilizer_df['Crop Type'].unique())
print("\nUnique Soil Types:\n", fertilizer_df['Soil Type'].unique())
print("\nUnique Fertilizers:\n", fertilizer_df['Fertilizer Name'].unique())