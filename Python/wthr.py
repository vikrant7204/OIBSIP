import requests, json

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Print the entire JSON response
        print(data)

        # Continue with extracting relevant information
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)
        humidity = data["main"]["humidity"]
        weather_condition = data["weather"][0]["description"]

        print(f"Weather in {location}:")
        print(f"Temperature: {temperature_celsius:.2f} °C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_condition}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with the actual API key from OpenWeatherMap
    api_key = "05e8b776a44e435cfae660c187d8ab5c"
    location = input("Enter city or ZIP code: ")

    get_weather(api_key, location)
