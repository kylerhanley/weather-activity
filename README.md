# Weather Based Activity Suggestion App: 

This Flask application takes a user's location and suggests activities to them based on the weather in their current area (which is obtained using OpenWeather API). The user enters their current city and state and a list of potential activites is generated based on the real time weather conditions in their current location. For example if it is snowing in the user's current location, the app will suggest activites such as skiing, snowboarding, snowmobiling, ice skating, and other suitable activities for snowy conditions. 
### Home page: 
![Screenshot 2024-01-04 090351](https://github.com/kylerhanley/weather-activity/assets/122304552/a4cf99e2-2004-4528-8c88-1d7db5b26fe1)

### Results Page: 
![Screenshot 2024-01-04 192707](https://github.com/kylerhanley/weather-activity/assets/122304552/67cd2b77-59f8-4899-881b-196757ea370b)

# How It's Made: 


### Technologies Used

Flask: The backend of the application is developed using Flask, a lightweight and flexible web framework for Python.

HTML and CSS: The frontend is designed using HTML for structuring the web pages and CSS for styling 

OpenWeatherMap API: The application fetches real-time weather data using the OpenWeatherMap API, enabling accurate and up-to-date weather condition reporting.

### How it Works

1. User Input: Users enter the city and state for which they want weather-based activity recommendations.

2. Weather Data Retrieval: The application sends a request to the OpenWeatherMap API, retrieving weather data for the specified location.

3. Weather Condition Analysis: The application analyzes the main weather condition, temperature, and wind speed to categorize the weather.

4. Activity Recommendations: Based on the weather conditions, the application suggests a list of suitable activities for the user.

# Main Goal  

The primary goal in doing this project was to learn how to use APIs with Flask in order to create a application that provides dynamic 
information to the user. 

