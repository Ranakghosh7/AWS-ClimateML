# ☁️ CloudClimateML: AWS-Deployed Weather Prediction API

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EC2-orange?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

> **Live Demo:** [http://51.21.220.147:5000](http://51.21.220.147:5000)  
> *(Hosted on AWS EC2 Free Tier)*

---

## 📖 Overview
**CloudClimateML** is a full-stack Machine Learning application deployed to the cloud. It predicts whether it will rain tomorrow based on real-time meteorological data inputs.

The goal of this project was to build an end-to-end **MLOps pipeline**: taking a raw dataset, training a Random Forest model, building a REST API with Flask, and deploying it to a live Linux server on AWS.

![Demo Screenshot](demo_screenshot.png)

---

## 🛠️ Tech Stack
This project uses industry-standard tools for Cloud and AI:

| Category | Technologies Used |
| :--- | :--- |
| **Cloud Infrastructure** | AWS EC2 (Elastic Compute Cloud), Ubuntu 24.04 LTS |
| **Backend API** | Python 3, Flask, Gunicorn |
| **Machine Learning** | Scikit-Learn (Random Forest), Pandas, NumPy |
| **Frontend UI** | HTML5, CSS3 (Glassmorphism / Cyberpunk Design) |
| **DevOps & Tools** | Git, SSH, SCP, Linux Process Management (nohup) |

---

## 🧠 Model Performance
The AI model was trained on the **WeatherAUS** dataset (10 years of historical data from the Australian Bureau of Meteorology).

* **Algorithm:** Random Forest Classifier
* **Accuracy:** ~85% on Test Data
* **Input Features:**
    1.  Temperature (°C)
    2.  Humidity (%)
    3.  Wind Speed (km/h)
    4.  Cloud Cover (0-8 scale)
    5.  Pressure (hPa)

---

## 🌐 API Usage (JSON)
Developers can use this project as a backend API. It accepts JSON data and returns a JSON prediction.

### 1. Endpoint
`POST /predict`

### 2. Request Format
Send a JSON object with a list of the 5 weather features:
```json
{
  "features": [23.5, 65, 0.0, 7.4, 1013.2]
}
