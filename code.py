import requests

def get_weather(city):
    api_key = "your_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] == "404":
        print(f"City {city} not found.")
    else:
        main = data["main"]
        weather = data["weather"][0]
        
        print(f"Weather in {city}: {weather['description']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")

# Example usage
city = input("Enter city name: ")
get_weather(city)
