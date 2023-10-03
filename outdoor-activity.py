
from flask import Flask, render_template, request, redirect
import json, requests
app = Flask(__name__)

@app.route("/", methods =["GET","POST"])
def home():
    if request.method == "POST":
        user_city = request.form.get("city")
        user_state = request.form.get("state")
        user_country = "US"
        api_key = "b4d8a2a529e1c2b76c50d4c6291284ef"
        url = f'https://api.openweathermap.org/data/2.5/weather?q={user_city},{user_state},{user_country}&appid={api_key}&units=imperial'
        print(user_city, user_state)
        if user_city is None or user_state is None:
            return "Please enter city and state"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            results = get_weather_measurements(weather_data)
            return results
        else:
            return "The location entered is invalid, try again"
    return render_template("index.html")

def get_weather_measurements(weather_data):
    # getting the values of main, temperature, wind
    main = weather_data.get("weather")
    main = main[0]
    main = main.get("main")
    temperature = weather_data.get("main")
    temperature = temperature.get("temp")
    wind = weather_data.get("wind")
    wind_speed = wind.get("speed")
    conditions = get_weather_conditions(main, temperature, wind_speed)
    if conditions == "thunderstorms":
        results = is_thunderstorms
    elif conditions == "raining":
        results = is_raining
    elif conditions == "snowing":
        results = is_snowing
    return results

def get_weather_conditions(main,temperature,wind_speed):
    if main == "Thunderstorm":
        return "thunderstorms"
    if main == "Rain" or main == "Drizzle":
        return "raining"
    if main == "Snow":
        return "snowing"
def is_thunderstorms():
    results = [
        "indoor climbing",
        "indoor tennis",
        "basketball",
        "table tennis",
        "badminton",
        "squash",
        "racquetball",
        "indoor swimming",
        "gymnastics",
        "yoga",
        "martial arts",
        "weightlifting",
        "CrossFit",
        "trampoline park",
    ]
    return results

def is_raining():
    results = [
        "indoor climbing",
        "indoor tennis",
        "basketball",
        "table tennis",
        "badminton",
        "squash",
        "racquetball",
        "indoor swimming",
        "gymnastics",
        "yoga",
        "martial arts",
        "weightlifting",
        "CrossFit",
        "trampoline park",
        "mudding",
        "dirt biking",
        "ice hockey"
    ]

    return results

def is_snowing():
    results = snow_sports = [
        "Skiing",
        "Snowboarding",
        "Cross-Country Skiing",
        "Snowshoeing",
        "Ice Skating",
        "Ice Hockey",
        "Curling",
        "Sledging",
        "Biathlon",
        "Snowmobiling",
        "Ski Jumping",
        "Nordic Combined",
        "Freestyle Skiing",
        "Ski Mountaineering",
        "Bobsleigh",
        "Luge",
        "Skeleton",
        "Snowkiting",
        "Winter Triathlon",
        "Telemark Skiing",
        "Speed Skating",
        "Figure Skating",
        "Short Track Speed Skating",
        "Long Track Speed Skating",
        "Ski Cross",
        "Alpine Skiing",
        "Ski Orienteering",
        "Snow Volleyball",
    ]
    return results







if __name__ == "__main__":
    app.run(debug = True)