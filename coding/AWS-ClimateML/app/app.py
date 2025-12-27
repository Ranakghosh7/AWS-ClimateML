from flask import Flask, request, jsonify, render_template
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

model = pickle.load(open("model/model.pkl", "rb"))

@app.route("/")
def home():
    return "CloudClimateML API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({"RainTomorrow": int(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
