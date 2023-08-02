import requests

weather_api = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def weather_data():
    res = requests.get(weather_api)
    if res.status_code == 200:
        return res.json()["list"]
    else:
        print("Weather data not available")
        return None

def get_temperature(date):
    weatherData = weather_data()
    if weatherData:
        for data in weatherData:
            if date in data["dt_txt"]:
                return data["main"]["temp"]
        print("Temperature data not available for the specified date.")
    return None

def get_wind_speed(date):
    weatherData = weather_data()
    if weatherData:
        for data in weatherData:
            if date in data["dt_txt"]:
                return data["wind"]["speed"]
        print("Wind speed data not available for the specified date.")
    return None

def get_pressure(date):
    weatherData = weather_data()
    if weatherData:
        for data in weatherData:
            if date in data["dt_txt"]:
                return data["main"]["pressure"]
        print("Pressure data not found for the specified date.")
    return None

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting the program.")
            break

        elif choice == "1":
            date = input("Enter the date in the format given(YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature(date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature} K")

        elif choice == "2":
            date = input("Enter the date in the format given(YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")

        elif choice == "3":
            date = input("Enter the date in the format given(YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
