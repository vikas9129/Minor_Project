import wikipedia
import requests
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wikipedia_search(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
        return result
    except:
        speak("Sorry, I couldn't find anything on Wikipedia.")
        return None

def weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # put your API key here
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        data = requests.get(url).json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            report = f"The temperature in {city} is {temp} degree Celsius with {desc}."
            speak(report)
            return report
        else:
            speak("City not found.")
    except:
        speak("Error fetching weather details.")
