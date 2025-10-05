import vosk, sys, sounddevice as sd, queue, json
from utils import check_internet
from offline_mode import execute_offline_command, speak
from online_mode import wikipedia_search, weather

# Setup Vosk model (download model and place in "model" folder)
models = {
    "English": r"Voice assistant\modelEng\vosk-model-small-en-us-0.15",
    "Hindi": r"Voice assistant\modelHindi\vosk-model-small-hi-0.22"   # <- apna Hindi model ka path daalna
}
language = "English"  # Change to "Hindi" for Hindi
model_path = models.get(language, models["English"])
q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def listen_command():
    rec = vosk.KaldiRecognizer(models, 16000)
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Listening...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if result.get("text"):
                    return result["text"]

def main():
    online = check_internet()
    speak("Hello, I am your assistant. Say a command.")
    while True:
        command = listen_command().lower()
        print("Heard:", command)

        # Try offline command first
        if execute_offline_command(command):
            continue

        # If online mode available
        if online:
            if "wikipedia" in command:
                query = command.replace("wikipedia", "")
                wikipedia_search(query.strip())
            elif "weather" in command:
                city = command.replace("weather", "").strip()
                weather(city)
            else:
                speak("Sorry, I didn't understand.")
        else:
            speak("Sorry, no internet connection for this request.")

if __name__ == "__main__":
    main()
