import collections

Location = collections.namedtuple('Location', 'city state country')


def main():
    # Show the header
    show_header()

    # Get the location request
    location_text = input(
        "Where do you want the weather report (e.g. Portland, US)? ")
    print(f"You selected {location_text}")

    # Convert plaintext over to data we can use
    loc = convert_plaintext_location(location_text)
    print(loc)

    # Get report from the API
    data = call_weather_api(loc)
    # Report the weather


def call_weather_api(loc):
    url = f"https://weather.talkpython.fm/api/weather?city={loc.city}&country={loc.country}&units=metric"
    if loc.state:
        url += f"&state={loc.state}"

    print(f"Would call {url}")


def convert_plaintext_location(location_text):
    if not location_text or not location_text.strip():
        return None

    location_text = location_text.lower().strip()
    parts = location_text.split(',')

    city = ""
    state = ""
    country = "us"
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
