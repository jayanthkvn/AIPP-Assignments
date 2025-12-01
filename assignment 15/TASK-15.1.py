import requests
import json

def get_weather(city):
    api_key = "70696becf81cb3a5496512bc93819f74"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.json())
        return

    data = response.json()
    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
