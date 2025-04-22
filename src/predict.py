import joblib
import pandas as pd
from .preprocess import preprocess_data

# Load the trained model
model = joblib.load('model/loan_model.pkl')

def predict_loan_status(input_data):
    # Convert input data to a dataframe
    input_df = pd.DataFrame([input_data])

    # Preprocess the input data
    processed_data = preprocess_data(input_df)

    # Make a prediction
    prediction = model.predict(processed_data)
    
    # Return result (1 = Approved, 0 = Not Approved)
    if prediction[0] == 1:
        return "Loan Approved"
    else:
        return "Loan Not Approved"

# Example usage (only runs if this file is run directly)
if __name__ == '__main__':
    input_data = {
        'Gender': 'Male',
        'Married': 'No',
        'Dependents': 0,
        'Education': 'Graduate',
        'Self_Employed': 'No',
        'ApplicantIncome': 5849,
        'CoapplicantIncome': 0,
        'LoanAmount': 360,
        'Loan_Amount_Term': 360,
        'Credit_History': 1,
        'Property_Area': 'Urban'
    }

    result = predict_loan_status(input_data)
    print(result)
