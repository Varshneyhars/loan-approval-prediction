from src.predict import predict_loan_status

print("Welcome to the Loan Approval Prediction System!")
print("Please enter the following details:")

# Collect user input for the prediction
gender = input("Gender (Male/Female): ")
married = input("Married (Yes/No): ")
dependents = int(input("Dependents (0/1/2/3+): "))
education = input("Education (Graduate/Not Graduate): ")
self_employed = input("Self Employed (Yes/No): ")
applicant_income = float(input("Applicant Income: "))
coapplicant_income = float(input("Coapplicant Income: "))
loan_amount = float(input("Loan Amount: "))
loan_amount_term = int(input("Loan Amount Term (in months): "))
credit_history = int(input("Credit History (1/0): "))
property_area = input("Property Area (Urban/Semiurban/Rural): ")

# Prepare input data as a dictionary
input_data = {
    'Gender': gender,
    'Married': married,
    'Dependents': dependents,
    'Education': education,
    'Self_Employed': self_employed,
    'ApplicantIncome': applicant_income,
    'CoapplicantIncome': coapplicant_income,
    'LoanAmount': loan_amount,
    'Loan_Amount_Term': loan_amount_term,
    'Credit_History': credit_history,
    'Property_Area': property_area
}

# Predict loan status
result = predict_loan_status(input_data)
print(f"Prediction: {result}")
