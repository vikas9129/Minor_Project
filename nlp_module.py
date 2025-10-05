from textblob import TextBlob

def get_intent(command):
    text = TextBlob(command.lower())

    if "time" in text.words:
        return "time"
    elif "date" in text.words:
        return "date"
    elif "calculate" in text.words:
        return "calculate"
    elif "joke" in text.words:
        return "joke"
    elif "hindi" in text.words:
        return "hindi"
    elif "english" in text.words:
        return "english"
    if "notepad" in text.words:
        return "open_notepad"
    elif "calculator" in text.words:
        return "open_calculator"
    elif "search" in text.words:
        return "search_google"
    elif "search" in text.words:
        return "search_google"
    elif "music" in text.words or "song" in text.words:
        return "play_music"
    elif "youtube" in text.words:
        return "open_youtube"
    else:
        return "unknown"
