from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Route for the Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route to get Real-Time Weather
@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    
    if not city:
        return jsonify({'error': 'Please enter a city name!'})

    # 1. Geocoding: Convert City Name -> Latitude & Longitude
    # We use Open-Meteo's Geocoding API
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    
    try:
        geo_response = requests.get(geo_url).json()
        
        if 'results' not in geo_response:
            return jsonify({'error': 'City not found. Try a bigger city!'})
            
        lat = geo_response['results'][0]['latitude']
        lon = geo_response['results'][0]['longitude']
        city_name = geo_response['results'][0]['name']
        country = geo_response['results'][0]['country']

        # 2. Weather: Get Real Data using Lat/Lon
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url).json()
        
        current_weather = weather_response['current_weather']
        
        # 3. Return the real data to your website
        return jsonify({
            'city': city_name,
            'country': country,
            'temperature': current_weather['temperature'],
            'windspeed': current_weather['windspeed'],
            'status': 'Success'
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)