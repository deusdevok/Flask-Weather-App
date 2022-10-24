# Weather app using Flask and OpenWeather API

Blog post explaining how to make this app step by step: https://deusdev.tech/blog/flask-weather-app/

- Using [https://openweathermap.org/](https://openweathermap.org/)
- API docs: [https://openweathermap.org/forecast5](https://openweathermap.org/forecast5)
- Icons: [https://openweathermap.org/weather-conditions](https://openweathermap.org/weather-conditions)

## Using this repository

- `cd` to your desired folder to work on
- `git clone https://github.com/deusdevok/Flask-Weather-App.git`
- Make a new virtual environment
    - `python -m venv venv`
- Activate the virtual environment
    - `venv\Scripts\activate`
- Make a new file called `local_settings.py` and store your API Secret Key in a variable called `SECRET_KEY`
    - `SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'`
- `pip install -r requirements.txt`
