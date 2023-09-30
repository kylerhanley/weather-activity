
from flask import Flask, render_template, request, redirect
import json, requests
app = Flask(__name__)

@app.route("/", methods =["GET","POST"])
def home():
    if request.method == "POST":
        return redirect("/get_api_data")
    else:
        return render_template("index.html")

@app.route("/get_api_data",methods= ["GET"])
def get_api_data():
    user_city = request.args.get("city")
    user_state = request.args.get("state")
    user_country = "US"
    api_key = "b4d8a2a529e1c2b76c50d4c6291284ef"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={user_city},{user_state},{user_country}&appid={api_key}&units=imperial'
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        results = suggest_activities(weather_data)
        return results
    else:
        return "The location entered is invalid, try again"

def suggest_activities(weather_data):
    # getting the values of main, temperature, wind
    main = weather_data.get("weather")
    main = main[0]
    main = main.get("main")
    temperature = weather_data.get("main")
    temperature = temperature.get("temp")
    wind = weather_data.get("wind")
    wind_speed = wind.get("speed")
    return f'{main} {temperature} {wind_speed}'

if __name__ == "__main__":
    app.run(debug = True)