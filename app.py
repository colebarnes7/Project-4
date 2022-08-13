# Dependencies
from flask import Flask, render_template, request
import numpy as np
from pickle import load

# Setting up flask app
app = Flask(__name__)

# Grab our model
model = load(open('./Models/US_RandomForest_08132022.pkl', 'rb'))

# Homepage


@app.route('/')
def home():
    return render_template('index.html')


# Route to setup form allowing user submissions to be tested on model


@app.route('/send', methods=["POST"])
def send():
    # Obtaining form inputs and adding to numpy array
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]

    # Making a prediction using the model
    prediction = model.predict(final_features)

    # Converts the prediction to text
    if prediction == 0:
        prediction_text = "This purchase was not fraud"

    elif prediction == 1:
        prediction_text = "This purchase was fraud"

    # Sending prediction to html page
    return render_template('index.html', result=prediction_text)


if __name__ == '__main__':
    app.run(debug=True)
