# Loan Approval Prediction System

A machine learning-based system that predicts whether a loan application will be approved or not based on various applicant characteristics.

## Project Overview

This project uses machine learning to predict loan approval status based on applicant information such as income, credit history, education, and other relevant factors. The system is built using Python and includes both a training module and a prediction interface.

## Features

- Machine learning model trained on historical loan data
- Preprocessing pipeline for handling missing values and categorical data
- Interactive command-line interface for making predictions
- Model accuracy of approximately 78%

## Project Structure

```
loan-approval-prediction/
├── data/                  # Dataset directory
│   └── loan_data.csv      # Training dataset
├── model/                 # Trained model directory
│   └── loan_model.pkl     # Saved model file
├── src/                   # Source code
│   ├── preprocess.py      # Data preprocessing functions
│   ├── train_model.py     # Model training script
│   └── predict.py         # Prediction functions
└── app.py                 # Main application interface
```

## Requirements

- Python 3.6+
- pandas
- scikit-learn
- joblib

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd loan-approval-prediction
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Training the Model

To train the model with your dataset:

```bash
python src/train_model.py
```

### Making Predictions

To use the prediction interface:

```bash
python app.py
```

The application will prompt you to enter the following information:
- Gender (Male/Female)
- Marital Status (Yes/No)
- Number of Dependents (0/1/2/3+)
- Education (Graduate/Not Graduate)
- Self Employment Status (Yes/No)
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term (in months)
- Credit History (1/0)
- Property Area (Urban/Semiurban/Rural)

## Model Details

The model uses the following features for prediction:
- Categorical features are encoded using Label Encoding
- Missing values are handled using appropriate imputation strategies
- The model is trained using scikit-learn's Random Forest Classifier

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 