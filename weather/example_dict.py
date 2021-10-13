def main():
    d = {
        'city': 'Portland',
        'state': 'ME',
        'details': ['Cold', 'Snowy', 'Winter']
    }

    print(d.get('country', 'USA'))
    d['country'] = 'AU'
    print(d.get('country', 'USA'))
    print(d)


w = {
  "weather": {
    "description": "overcast clouds",
    "category": "Clouds"
  },
  "wind": {
    "speed": 0.89,
    "deg": 186
  },
  "units": "metric",
  "forecast": {
    "temp": 7.6,
    "feels_like": 7.6,
    "pressure": 1016,
    "humidity": 92,
    "low": 6,
    "high": 8
  },
  "location": {
    "city": "Portland",
    "state": 'OR',
    "country": "US"
  },
  "rate_limiting": {
    "unique_lookups_remaining": 45,
    "lookup_reset_window": "1 hour"
  }
}

print(f"{w.get('forecast').get('temp')} C")

if __name__ == '__main__':
    main()
