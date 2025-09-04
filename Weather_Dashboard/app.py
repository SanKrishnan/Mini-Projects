from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

def get_weather_data(city):
    my_api = os.environ.get("API_KEY", "35f4e77c137e0108200f1ab75484e567")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_api}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            return None
    except Exception:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        if not weather_data:
            error = "Could not retrieve weather data. Please check the city name."
    return render_template('index.html', weather=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
