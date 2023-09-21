

# CLI Based Weather Forecasting Application

import requests

# Location Input

def get_location():
    location=input("Enter your city or Location: ")
    return location


# API Integration

def get_weather(location, unit='metric',api_key='46bc758a6a8a24f5f9e9917eebd95536'):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "units": unit, "appid": api_key}
    try:
        response = requests.get(base_url,params=params)
        data=response.json()
        if response.status_code==200:
            return data
        else:
            print("Error: Unable to fetch data.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Display Weather

def display_weather(data):
    if data:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        weather_condition = data["weather"][0]["description"]

        print(f"Weather in {data['name']}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Condition: {weather_condition}")


# Unit Conversion

def get_temp():
    unit=input("Choose temperature unit (Celsius or Fahrenheit):").strip().lower()
    if unit=="celsius":
        return "metric"
    elif unit=="fahrenheit":
        return "imperial"
    else:
        print("Invalid unit")
        return "metric"



locations=get_location()    
unit=get_temp()

data=get_weather(locations,unit)

if data:
    display_weather(data)
else:
    print("Weather data is not avaliable")    
