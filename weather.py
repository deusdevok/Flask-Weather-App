from flask import Flask, render_template, request
from local_settings import SECRET_KEY
import requests

app = Flask('__name__')

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/city', methods=('GET', 'POST'))
def get_weather():
    if request.method == 'POST':
        city = request.form['city']

        url_path = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric' + '&appid=' +  SECRET_KEY

        r = requests.get(url_path)
        data = r.json()
                
        '''
        {'coord': {'lon': -58.3772, 'lat': -34.6132}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'base': 'stations', 'main': {'temp': 19.18, 'feels_like': 18.8, 'temp_min': 18.85, 'temp_max': 19.99, 'pressure': 1015, 'humidity': 63}, 'visibility': 10000, 'wind': {'speed': 3.6, 'deg': 230}, 'clouds': {'all': 40}, 'dt': 1663603068, 'sys': {'type': 1, 'id': 8224, 'country': 'AR', 'sunrise': 1663580839, 'sunset': 1663624046}, 'timezone': -10800, 'id': 3435910, 'name': 'Buenos Aires', 'cod': 200}
        '''

        #icon = data['weather'][0]['icon']

        return render_template('index.html', city=city, data=data)

    return render_template('index.html')