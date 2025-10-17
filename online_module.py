import webbrowser
import shutil
import wikipedia
import datetime
import requests
from utils import get_chrome_path

chrome_path = get_chrome_path()
if chrome_path:
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
else:
    print("⚠️ Chrome not found — using default browser.")

# # ✅ Register Chrome (default browser)
# chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
# if shutil.which(chrome_path):
#     webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))


# ----------------------------- BASIC SEARCH -----------------------------
def open_google_search(command, speak):
    query = command.lower().replace("search", "").replace("open", "").strip()
    if not query:
        speak("What do you want me to search for?")
        return
    url = f"https://www.google.com/search?q={query}"
    
    if chrome_path:
        webbrowser.get('chrome').open(url)
    else:
        webbrowser.open_new_tab(url)

    speak(f"Searching Google for {query}")


# ----------------------------- ENTERTAINMENT -----------------------------
def open_youtube(command, speak):
    webbrowser.get('chrome').open("https://www.youtube.com")
    speak("Opening YouTube")

def play_on_youtube(command, speak):
    query = command.lower().replace("play", "").strip()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.get('chrome').open(url)
    speak(f"Playing {query} on YouTube")

def open_spotify(command, speak):
    webbrowser.get('chrome').open("https://open.spotify.com")
    speak("Opening Spotify")

def play_song_spotify(command, speak):
    query = command.lower().replace("play", "").replace("on spotify", "").strip()
    url = f"https://open.spotify.com/search/{query}"
    webbrowser.get('chrome').open(url)
    speak(f"Searching {query} on Spotify")


# ----------------------------- SOCIAL MEDIA -----------------------------
def open_facebook(command, speak):
    webbrowser.get('chrome').open("https://www.facebook.com")
    speak("Opening Facebook")

def open_instagram(command, speak):
    webbrowser.get('chrome').open("https://www.instagram.com")
    speak("Opening Instagram")

def open_twitter(command, speak):
    webbrowser.get('chrome').open("https://x.com")
    speak("Opening Twitter")

def open_linkedin(command, speak):
    webbrowser.get('chrome').open("https://www.linkedin.com")
    speak("Opening LinkedIn")

def open_whatsapp_web(command, speak):
    webbrowser.get('chrome').open("https://web.whatsapp.com")
    speak("Opening WhatsApp Web")


# ----------------------------- GOOGLE SERVICES -----------------------------
def open_gmail(command, speak):
    webbrowser.get('chrome').open("https://mail.google.com")
    speak("Opening Gmail")

def open_google_drive(command, speak):
    webbrowser.get('chrome').open("https://drive.google.com")
    speak("Opening Google Drive")

def open_google_docs(command, speak):
    webbrowser.get('chrome').open("https://docs.google.com")
    speak("Opening Google Docs")

def open_google_meet(command, speak):
    webbrowser.get('chrome').open("https://meet.google.com")
    speak("Opening Google Meet")

def open_google_maps(command, speak):
    query = command.lower().replace("maps", "").strip()
    if query:
        url = f"https://www.google.com/maps/search/{query}"
    else:
        url = "https://www.google.com/maps"
    webbrowser.get('chrome').open(url)
    speak(f"Opening Google Maps for {query or 'you'}")


# ----------------------------- INFORMATION -----------------------------
def search_wikipedia(command, speak):
    query = command.lower().replace("wikipedia", "").replace("search", "").strip()
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except:
        speak("Sorry, I couldn't find that on Wikipedia.")

def check_weather(command, speak):
    query = command.lower().replace("weather", "").strip()
    if query:
        webbrowser.get('chrome').open(f"https://www.google.com/search?q=weather+{query}")
        speak(f"Showing weather for {query}")
    else:
        webbrowser.get('chrome').open("https://www.google.com/search?q=weather+near+me")
        speak("Showing local weather")

def open_news(command, speak):
    webbrowser.get('chrome').open("https://news.google.com")
    speak("Opening latest news")

def get_time_online(command, speak):
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")

def get_date_online(command, speak):
    today = datetime.date.today().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")


# ----------------------------- SHOPPING -----------------------------
def open_amazon(command, speak):
    query = command.lower().replace("amazon", "").replace("search", "").strip()
    if query:
        url = f"https://www.amazon.in/s?k={query}"
        webbrowser.get('chrome').open(url)
        speak(f"Searching {query} on Amazon")
    else:
        webbrowser.get('chrome').open("https://www.amazon.in")
        speak("Opening Amazon")

def open_flipkart(command, speak):
    query = command.lower().replace("flipkart", "").replace("search", "").strip()
    if query:
        url = f"https://www.flipkart.com/search?q={query}"
        webbrowser.get('chrome').open(url)
        speak(f"Searching {query} on Flipkart")
    else:
        webbrowser.get('chrome').open("https://www.flipkart.com")
        speak("Opening Flipkart")


# ----------------------------- STUDY / LEARNING -----------------------------
def open_google_scholar(command, speak):
    webbrowser.get('chrome').open("https://scholar.google.com")
    speak("Opening Google Scholar")

def open_chatgpt(command, speak):
    webbrowser.get('chrome').open("https://chat.openai.com")
    speak("Opening ChatGPT")

def open_stackoverflow(command, speak):
    webbrowser.get('chrome').open("https://stackoverflow.com")
    speak("Opening Stack Overflow")

def open_github(command, speak):
    webbrowser.get('chrome').open("https://github.com")
    speak("Opening GitHub")

def open_quora(command, speak):
    webbrowser.get('chrome').open("https://www.quora.com")
    speak("Opening Quora")


# ----------------------------- EMAIL / COMMUNICATION -----------------------------
def open_outlook(command, speak):
    webbrowser.get('chrome').open("https://outlook.live.com")
    speak("Opening Outlook Mail")

def open_zoom(command, speak):
    webbrowser.get('chrome').open("https://zoom.us")
    speak("Opening Zoom Meetings")

def open_teams(command, speak):
    webbrowser.get('chrome').open("https://teams.microsoft.com")
    speak("Opening Microsoft Teams")


# ----------------------------- OTHER UTILITIES -----------------------------
def open_translate(command, speak):
    webbrowser.get('chrome').open("https://translate.google.com")
    speak("Opening Google Translate")

def open_currency_converter(command, speak):
    webbrowser.get('chrome').open("https://www.google.com/search?q=currency+converter")
    speak("Opening currency converter")

def open_speed_test(command, speak):
    webbrowser.get('chrome').open("https://fast.com")
    speak("Checking your internet speed")

def open_calendar(command, speak):
    webbrowser.get('chrome').open("https://calendar.google.com")
    speak("Opening Google Calendar")


# ----------------------------- COMMAND MAPPING -----------------------------
def get_online_commands():
    return {
        # Search & Browsing
        "search": open_google_search,
        "open": open_google_search,

        # Media
        "youtube": open_youtube,
        "play": play_on_youtube,
        "spotify": open_spotify,
        "play song": play_song_spotify,

        # Social Media
        "facebook": open_facebook,
        "instagram": open_instagram,
        "twitter": open_twitter,
        "linkedin": open_linkedin,
        "whatsapp": open_whatsapp_web,

        # Google Services
        "gmail": open_gmail,
        "drive": open_google_drive,
        "docs": open_google_docs,
        "meet": open_google_meet,
        "maps": open_google_maps,

        # Info
        "wikipedia": search_wikipedia,
        "weather": check_weather,
        "news": open_news,
        "time": get_time_online,
        "date": get_date_online,

        # Shopping
        "amazon": open_amazon,
        "flipkart": open_flipkart,

        # Learning / Coding
        "scholar": open_google_scholar,
        "chatgpt": open_chatgpt,
        "stackoverflow": open_stackoverflow,
        "github": open_github,
        "quora": open_quora,

        # Communication
        "outlook": open_outlook,
        "zoom": open_zoom,
        "teams": open_teams,

        # Utilities
        "translate": open_translate,
        "currency": open_currency_converter,
        "speed test": open_speed_test,
        "calendar": open_calendar
    }
