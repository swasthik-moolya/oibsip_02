import requests
import json

def get_weather(city):

  api_key = "da181272f646ce2f396fb58b3a9476dd"
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  complete_url = f"{base_url}appid={api_key}&q={city}"

  try:
    response = requests.get(complete_url)
    data = json.loads(response.text)
    return data
  except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
    return None

def display_weather(data):
  if data:
    temperature = round(data["main"]["temp"] - 273.15, 2)
    humidity = data["main"]["humidity"]
    weather_description = data["weather"][0]["description"]

    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {weather_description}")
  else:
    print("Unable to fetch weather data.")

def main():
  city = input("Enter city name: ")
  weather_data = get_weather(city)
  display_weather(weather_data)

if __name__ == "__main__":
  main()
