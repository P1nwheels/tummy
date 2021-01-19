import json
import os


import requests


class Weather:
    def __init__(self, file):
        self.file = file
        # Washington DC lat and lon
        self.default_obj = {
            "lat": 38.89511,
            "lon": -77.03637,
            "units": "standard"
        }


    def get_weather_json(self):
        try:
            f = open(self.file)
        except FileNotFoundError:
            temp_obj = self.default_obj
            f = open(self.file, 'w+')
            json.dump(temp_obj, f, indent=4)
            rv = temp_obj
            f.close()
        else:
            rv = json.load(f)
            f.close()
        finally:
            return rv


    def get_weather_url(self):
        to_exclude = ["minutely", "hourly", "daily", "alerts"]
        wdata = self.get_weather_json()
        URL = "https://api.openweathermap.org/data/2.5/onecall?"
        URL += f"lat={wdata['lat']}"
        URL += f"&lon={wdata['lon']}"
        excluded = ",".join(to_exclude)
        URL += f"&exclude={excluded}"
        URL += f"&units={wdata['units']}"
        URL += f"&appid={os.getenv('WEATHERAPIKEY')}"
        return URL


    def get_weather(self):
        r = requests.get(self.get_weather_url())
        data = r.json()['current']
        print(f"""
    Description: {data['weather'][0]['description'].title()}
    Temp: {data['temp']}
    Feels like: {data['feels_like']}
    Wind speeds: {data['wind_speed']}
        """)


    def configure_json(self, lat=None, lon=None, units=None):
        with open(self.file, "w") as f:
            temp_obj = self.default_obj
            temp_obj['lat'] = lat or self.default_obj['lat']
            temp_obj['lon'] = lon or self.default_obj['lon']
            temp_obj['units'] = units or self.default_obj['units']
            json.dump(temp_obj, f, indent=4)

    
def parse_weather_args(subcommand, args, weather):
    if subcommand == "config":
        if args:
            try:
                lat = float(args[0])
                lon = float(args[1])
                units = args[2]
            except ValueError:
                print("\n    Please provide a valid latitude/longitude.\n")
            except IndexError:
                print("\n    Please provide a latitude, longitude, and unit of measurement.\n")
            else:
                weather.configure_json(lat, lon, units)
        else:
            print("\n    Configuring using default values.\n")
            weather.configure_json()
    else:
        weather.get_weather()