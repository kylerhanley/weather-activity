from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_city = request.form.get("city")
        user_state = request.form.get("state")
        user_country = "US"
        api_key = "b4d8a2a529e1c2b76c50d4c6291284ef"
        url = f'https://api.openweathermap.org/data/2.5/weather?q={user_city},{user_state},{user_country}&appid={api_key}&units=imperial'
        print(user_city, user_state)
        # if user has not entered input
        if user_city is None or user_state is None:
            return "Please enter city and state"
        # API call with user input data
        response = requests.get(url)
        # API call successful
        if response.status_code == 200:
            weather_data = response.json()
            results, main, temperature, wind_speed = get_weather_measurements(weather_data)
            return render_template("results.html", activities=results, main=main, temperature=temperature,
                                   wind_speed=wind_speed)
        else:
            return "The location entered is invalid, try again"
    return render_template("home.html")


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
        results = is_thunderstorms()
    elif conditions == "raining":
        results = is_raining()
    elif conditions == "snowing":
        results = is_snowing()
    elif conditions == "misty":
        results = is_misting()
    elif conditions == "foggy":
        results = is_foggy()
    elif conditions == "tornado":
        results = is_tornado()
    elif conditions == "hurricane":
        results = is_hurricane()
    elif conditions == "windy":
        results = is_windy()
    elif conditions == "clear and hot" or conditions == "cloudy and hot":
        results = is_hot()
    elif conditions == "clear and mild" or conditions == "cloudy and mild":
        results = is_mild()
    elif conditions == "clear and cold" or conditions == "cloudy and cold":
        results = is_cold()

    return results, main, temperature, wind_speed


def get_weather_conditions(main, temperature, wind_speed):
    if main == "Thunderstorm":
        return "thunderstorms"
    if main == "Rain" or main == "Drizzle":
        return "raining"
    if main == "Snow":
        return "snowing"
    if main == "Mist":
        return "misty"
    if main == "Fog":
        return "foggy"
    if main == "Tornado":
        return "tornado"
    if main == "Hurricane":
        return "hurricane"
    if main == "hazy":
        return "foggy"
    if main == "Clear":
        if wind_speed > 20.0:
            return "windy"
        if temperature >= 85:
            return "clear and hot"
        if 55 <= temperature <= 80:
            return "clear and mild"
        if 32 <= temperature <= 54:
            return "clear and cold"
    if main == "Clouds":
        if wind_speed > 15.0:
            return "windy"
        if temperature >= 80:
            return "cloudy and hot"
        if 55 <= temperature <= 80:
            return "cloudy and mild"
        if 32 <= temperature <= 54:
            return "cloudy and cold"


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
    results = [
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
        "Speed Skating",
        "Figure Skating",
        "Short Track Speed Skating",
        "Long Track Speed Skating",
        "Ski Cross",
        "Alpine Skiing",
        "Ski Orienteering",
    ]
    return results


def is_misting():
    results = [
        "Nature Walk",
        "Photography",
        "Bird Watching",
        "Hiking",
        "Botanical Garden Visit",
        "Fishing",
        "Paddle Boating",
        "Outdoor Yoga",
        "Stargazing",
        "Geocaching"

    ]
    return results


def is_foggy():
    results = [
        "Morning Jog",
        "Golf ",
        "Tennis ",
        "Disc Golf ",
        "Soccer",
        "Basketball ",
        "Beach Volleyball ",
        "Skateboarding ",
        "Mountain Biking ",
        "Trail Running",
        "Paddleboarding ",
        "Kayaking ",
        "Fishing ",
        "Horseback Riding",
        "Archery ",
        "Frisbee ",
        "Softball ",
        "Baseball",
        "Rugby",
        "Lacrosse"
    ]
    return results


def is_tornado():
    results = ["There is a tornado! Take cover!"]
    return results


def is_hurricane():
    results = ["There is a hurricane! Stay inside and stay away from windows"]
    return results


def is_windy():
    results = [
        "Kite Flying",
        "Windsurfing",
        "Sailing",
        "Paragliding",
        "Hang Gliding",
        "Kiteboarding",
    ]
    return results


def is_hot():
    results = [
        "Swimming",
        "Water Polo",
        "Surfing",
        "Kayaking",
        "Paddleboarding",
        "Water Skiing",
        "Tubing",
        "Jet Skiing",
        "Sailing",
        "Canoeing",
        "Diving",
        "Snorkeling",
        "Wakeboarding",
        "Outdoor Water Park",
        "Rowing",
    ]
    return results


def is_mild():
    results = [
        "Soccer",
        "Basketball",
        "Baseball",
        "Softball",
        "Tennis",
        "Golf",
        "Cycling",
        "Hiking",
        "Running",
        "Skateboarding",
        "Ultimate Frisbee",
        "Frisbee Golf",
        "Badminton",
        "Disc Golf",
        "Parkour",
        "Rock Climbing",
        "Mountain Biking",
        "Trail Running",
        "Horseback Riding",
        "Canoeing",
        "Kayaking",
        "Flag Football",
        "Ultimate Frisbee",
        "Rugby",
        "Lacrosse",
        "Field Hockey",
        "Volleyball",
        "Handball",
    ]
    return results


def is_cold():
    results = [
        "Ice Hockey",
        "Ice Fishing",
        "Curling",
        "Indoor Rock Climbing",
        "Indoor Swimming",
        "Indoor Tennis",
        "Indoor Basketball",
        "Indoor Volleyball",
        "Indoor Soccer",
        "Indoor Trampoline Park",
        "Indoor Bowling",
        "Indoor Mini Golf",
        "Board Games",
        "Cooking and Baking",
        "Reading",
        "Museum Visits",
        "Yoga",
        "Gym Workouts",
        "Indoor Cycling",
        "Pilates (indoor)",
        "Dance Classes",
    ]
    return results



if __name__ == "__main__":
    app.run(debug=True)
