# nlp_module.py
from textblob import TextBlob

def get_intent(command):
    text = TextBlob(command.lower())
    cmd = " ".join(text.words)

    if "time" in cmd or "clock" in cmd:
        return "time"
    elif "date" in cmd or "day" in cmd:
        return "date"
    elif "calculate" in cmd or "plus" in cmd or "minus" in cmd or "divide" in cmd or "times" in cmd:
        return "calculate"
    elif "joke" in cmd or "funny" in cmd:
        return "joke"
    elif "hindi" in cmd:
        return "hindi"
    elif "english" in cmd:
        return "english"
    elif "notepad" in cmd:
        return "open_notepad"
    elif "calculator" in cmd:
        return "open_calculator"
    elif "search" in cmd or "google" in cmd:
        return "search_google"
    elif "music" in cmd or "song" in cmd:
        return "play_music"
    elif "youtube" in cmd:
        return "open_youtube"
    elif "shutdown" in cmd or "shut down" in cmd:
        return "shutdown"
    elif "weather" in cmd:
        return "weather"
    else:
        return "unknown"
