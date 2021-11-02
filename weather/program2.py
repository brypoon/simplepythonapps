import collections
import requests
import os
import sys

Location = collections.namedtuple('Location', 'city country state')
Weather = collections.namedtuple('Weather', 'location units temp condition')


def main():
    show_header()

    # Get the location request
    location_text = input(
        "Weather report for: (e.g. <city> Portland, <country> optional, <state> optional)? ")
    loc = convert_plaintext_location(location_text)
    if not loc:
        print(f"Could not find anything about {location_text}.")
        return

    weather = call_weather_api(loc)
    if not weather:
        print(f"Could not get weather for {location_text} from API.")
        return
    report_weather(loc, weather)


def report_weather(loc, weather):
    location_name = get_location_name(loc)
    scale = get_scale(weather)
    print(
        f"The weather in {location_name}is {weather.temp}{scale} with {weather.condition}")


def get_scale(weather):
    if weather.units == 'imperial':
        scale = "F"
    else:
        scale = "C"
    return scale


def get_location_name(location):
    if not location.state:
        return f"{location.city.capitalize()}, {location.country.upper()}"
    else:
        return f"{location.city.capitalize()}, {location.state.upper()}, {location.country.upper()}"


def call_weather_api(loc):
    api_key = os.getenv('OWM_API_KEY')

    if not api_key:
        print("Error: no 'OWM_API_KEY' provided")
        sys.exit(1)

    url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={loc.city}"
    if loc.country:
        url += f",{loc.country}"
    if loc.state:
        url += f",{loc.state}"
    

    resp = requests.get(url)
    if resp.status_code in {400, 404, 500}:
        print(f"Error: {resp.text}.")
        return None

    data = resp.json()

    return convert_api_to_weather(data, loc)


def convert_api_to_weather(data, loc):
    temp = data.get('main').get('temp')
    w = data.get('weather')
    condition = f"{w[0]['description'].title()}."
    weather = Weather(loc, data.get('units'), temp, condition)

    return weather


def convert_plaintext_location(location_text):
    if not location_text or not location_text.strip():
        return None

    location_text = location_text.lower().strip()
    parts = location_text.split(',')

    city = ""
    state = ""
    country = ""
    if len(parts) == 1:
        city = parts[0].strip()
    elif len(parts) == 2:
        city = parts[0].strip()
        country = parts[1].strip()
    elif len(parts) == 3:
        city = parts[0].strip()
        state = parts[1].strip()
        country = parts[2].strip()
    else:
        return None

    # print(f"City={city}, State={state}, Country={country}")
    return Location(city, state, country)


def show_header():
    print('-----------------------')
    print('     WEATHER APP')
    print('-----------------------')
    print()


if __name__ == '__main__':
    main()
