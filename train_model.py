import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data from CSV file
data = pd.read_csv('loan_data.csv')

# Features and target variable
X = data[['income', 'age', 'credit_score']]
y = data['loan_approved']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save trained model as a pickle file
with open('loan_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained successfully and saved as 'loan_model.pkl'")
