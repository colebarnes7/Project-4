# Dependencies
from flask import Flask, render_template
# import pickle

# Setting up flask app
app = Flask(__name__)

# Possible way to grab our model
# model = pickle.load(open('model_name.pkl', 'rb'))

# Homepage
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)