from flask import Flask, request, render_template, jsonify
import requests  # Ajouter cette importation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  # Assurez-vous d'avoir un fichier 'form.html'

@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les valeurs du formulaire
    preg = float(request.form['Pregnancies'])
    glucose = float(request.form['Glucose'])
    bp = float(request.form['BloodPressure'])
    skinthickness = float(request.form['SkinThickness'])
    insulin = float(request.form['Insulin'])
    bmi = float(request.form['BMI'])
    dpf = float(request.form['DPF'])
    age = float(request.form['Age'])

    # Construire les données à envoyer à l'API FastAPI
    data = {
        "Pregnancies": preg,
        "Glucose": glucose,
        "BloodPressure": bp,
        "SkinThickness": skinthickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DPF": dpf,
        "Age": age
    }

    # Envoyer la requête POST à l'API FastAPI
    api_url = "http://localhost:80/predict"  # Assurez-vous que le port est correct
    response = requests.post(api_url, json=data)
    result = response.json()

    # Afficher le résultat
    return render_template('result.html', prediction_text=result['ans'])
if __name__ == "__main__":
    app.run(debug=True)