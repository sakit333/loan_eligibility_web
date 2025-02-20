from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('loan_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    income = float(request.form['income'])
    age = float(request.form['age'])
    credit_score = float(request.form['credit_score'])

    features = np.array([[income, age, credit_score]])
    prediction = model.predict(features)
    result = 'Yes' if prediction[0] == 1 else 'No'

    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
