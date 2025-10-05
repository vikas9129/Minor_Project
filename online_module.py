# online_module.py

import webbrowser

def search_google(command, speak):
    query = command.lower().replace("search", "").strip()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching Google for {query}")

def weather(command, speak):
    speak("Weather feature is not implemented yet, but requires internet connection.")

def get_online_commands():
    return {
        "search_google": search_google,
        "weather": weather
    }
