import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load your CSV data
data = pd.read_csv('data/loan_data.csv')

# Assuming these columns exist in your CSV
X = data[['income', 'age', 'credit_score']]
y = data['loan_approval']  # 1 for approved, 0 for not approved

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save Model
pickle.dump(model, open('loan_model.pkl', 'wb'))
