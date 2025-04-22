import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from preprocess import preprocess_data
import joblib

# Load the data
data = pd.read_csv('data/train_u6lujuX_CVtuZ9i.csv')

# Preprocess the data
data = preprocess_data(data)

# Define features (X) and target (y)
X = data.drop(columns=['Loan_Status'])  # Exclude target column
y = data['Loan_Status']  # Target column

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = GaussianNB()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Save the trained model
joblib.dump(model, 'model/loan_model.pkl')
