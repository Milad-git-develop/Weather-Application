import requests
import sys

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None
    
    def display_weather(self, data):
        if data and data.get('cod') == 200:
            city = data['name']
            country = data['sys']['country']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            wind_speed = data['wind']['speed']
            
            print(f"\n{'='*40}")
            print(f"Weather in {city}, {country}")
            print(f"{'='*40}")
            print(f"🌡️  Temperature: {temp}°C")
            print(f"💧 Humidity: {humidity}%")
            print(f"💨 Wind Speed: {wind_speed} m/s")
            print(f"☁️  Conditions: {description.title()}")
            print(f"{'='*40}")
        else:
            print("City not found or API error!")

def main():
    API_KEY = "9adced7ddff5c6dc7f031455d3dec00e"
    app = WeatherApp(API_KEY)
    
    print("🌤️  Weather Application 🌤️")
    print("-" * 30)
    
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        
        if city.lower() in ['quit', 'exit', 'q']:
            print("Goodbye! 👋")
            break
        
        if city:
            print("Fetching weather data...")
            data = app.get_weather(city)
            app.display_weather(data)
        else:
            print("Please enter a city name!")

if __name__ == "__main__":
    main()