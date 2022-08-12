# Dependencies
from flask import Flask, render_template, request
import numpy as np
from pickle import load

# Setting up flask app
app = Flask(__name__)

# Grab our model
model = load(open('./Models/testmodel.pkl', 'rb'))

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

    # Sending prediction to html page
    return render_template('index.html', result=prediction)


if __name__ == '__main__':
    app.run(debug=True)
