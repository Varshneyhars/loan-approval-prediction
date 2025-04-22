import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(data):
    # Create a copy of the data to avoid SettingWithCopyWarning
    data = data.copy()
    
    # Drop the 'Loan_ID' column if it exists (for training data)
    if 'Loan_ID' in data.columns:
        data = data.drop(columns=['Loan_ID'])
    
    # Fill missing values in 'Dependents' with the most frequent value first
    data['Dependents'] = data['Dependents'].fillna(data['Dependents'].mode()[0])
    
    # Then clean the 'Dependents' column, replacing '3+' with 3 and convert to int
    data['Dependents'] = data['Dependents'].replace('3+', 3).astype(int)
    
    # Handle categorical columns: Use label encoding for binary categories like 'Gender', 'Married', 'Self_Employed', etc.
    label_columns = ['Gender', 'Married', 'Self_Employed', 'Education', 'Loan_Status', 'Property_Area', 'Credit_History']
    label_encoder = LabelEncoder()
    
    for col in label_columns:
        if col in data.columns:  # Only process columns that exist
            data[col] = label_encoder.fit_transform(data[col].astype(str))
    
    # Fill missing values in numeric columns with the median value
    data['LoanAmount'] = data['LoanAmount'].fillna(data['LoanAmount'].median())
    data['Loan_Amount_Term'] = data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0])
    
    # Return the preprocessed data
    return data
