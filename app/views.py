from flask.views import MethodView
from app.app import app

class WeatherAPI(MethodView):
    def get(self):
        return 'Weather API'

app.add_url_rule('/api/weather', view_func=WeatherAPI.as_view('api_weather'))
