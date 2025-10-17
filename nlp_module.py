from textblob import TextBlob

def get_intent(command):
    # Convert command to lowercase and split into words
    text = TextBlob(command.lower())
    cmd = " ".join(text.words)  # plain string of words

    # ------------------ CORE INTENTS ------------------
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
        return "search"
    elif "music" in cmd or "song" in cmd:
        return "play song"
    elif "youtube" in cmd or "you do" in cmd:
        return "youtube"
    elif "spotify" in cmd:
        return "spotify"
    elif "shutdown" in cmd or "shut down" in cmd:
        return "shutdown"
    elif "weather" in cmd:
        return "weather"
    elif "mail" in cmd or "gmail" in cmd or "email" in cmd or "jimmy" in cmd:
        return "gmail"
    elif "map" in cmd or "location" in cmd or "directions" in cmd:
        return "maps"
    elif "facebook" in cmd:
        return "facebook"
    elif "instagram" in cmd:
        return "instagram"
    elif "twitter" in cmd or "x" in cmd:
        return "twitter"
    elif "github" in cmd:
        return "github"
    elif "linkedin" in cmd:
        return "linkedin"
    elif "news" in cmd:
        return "news"
    elif "wikipedia" in cmd:
        return "wikipedia"
    else:
        return "unknown"
