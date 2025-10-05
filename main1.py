import pyttsx3
import tkinter as tk
from tkinter import scrolledtext
import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer
import datetime
import random
from nlp_module import get_intent
import threading
import os
import webbrowser
import datetime
import random


# ------------------ Text-to-Speech ------------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # female voice

# ------------------ Threading for Listening ------------------
def start_listening_thread():
    listener_thread = threading.Thread(target=start_listening)
    listener_thread.daemon = True  # Thread GUI ke close hone pe auto stop ho jaye
    listener_thread.start()

def speak(text):
    text_box.insert(tk.END, f"Assistant: {text}\n")
    text_box.see(tk.END)
    engine.say(text)
    engine.runAndWait()

# ------------------ Vosk Models ------------------
models = {
    "English": r"C:\Users\Niteesh\Desktop\python\Voice assistant\modelEng\vosk-model-small-en-us-0.15",
    "Hindi": r"C:\Users\Niteesh\Desktop\python\Voice assistant\modelHindi\vosk-model-small-hi-0.22"
}

current_model = None
recognizer = None
q = queue.Queue()
current_lang = "English"  # Default language

# ------------------ Load Model ------------------
def load_model(lang):
    global current_model, recognizer, current_lang
    model_path = models[lang]
    current_model = Model(model_path)
    recognizer = KaldiRecognizer(current_model, 16000)
    current_lang = lang
    text_box.insert(tk.END, f"🌐 Switched to {lang} model.\n")
    text_box.see(tk.END)


# ------------------ Audio Callback ------------------
def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    q.put(bytes(indata))
# ------------------ Command Functions ------------------
def show_time(command=None):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {now}")

def show_date(command=None):
    today = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

def tell_joke(command=None):
    jokes = [
        "Why did the computer go to the doctor? Because it caught a virus!",
        "Why was the computer cold? It left its Windows open!"
    ]
    speak(random.choice(jokes))

def calculate_expression(command):
    try:
        expr = command.lower().replace("calculate", "").replace("plus", "+").replace("minus", "-")
        expr = expr.replace("times", "*").replace("divided by", "/")
        result = eval(expr.strip())
        speak(f"The answer is {result}")
    except:
        speak("Sorry, I cannot calculate that.")

def switch_to_hindi(command=None):
    load_model("Hindi")
    speak("Language switched to Hindi")

def switch_to_english(command=None):
    load_model("English")
    speak("Language switched to English")

def open_notepad(command=None):
    os.system("notepad")
    speak("Opened Notepad")

def search_google(command):
    query = command.lower().replace("search", "").strip()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching Google for {query}")

commands = {
    "time": show_time,
    "date": show_date,
    "joke": tell_joke,
    "calculate": calculate_expression,
    "hindi": switch_to_hindi,
    "english": switch_to_english,
    "open_notepad": open_notepad,
    "search_google": search_google
}


# ------------------ Offline Task Performer ------------------

def perform_task(command):
    intent = get_intent(command)  # NLP se intent nikal
    if intent in commands:
        commands[intent](command)  # dictionary ke function ko call karo
    else:
        speak("Sorry, I didn't understand that command.")


# ------------------ Start Listening ------------------
def start_listening():
    if recognizer is None:
        load_model(current_lang)


    text_box.insert(tk.END, "🎙 Listening...\n")
    text_box.see(tk.END)

    with sd.RawInputStream(samplerate=16000, blocksize=4000, dtype='int16',
                           channels=1, callback=callback):
        while True:
            try:
                data = q.get(timeout=1)
            except queue.Empty:
                continue  # continue if no data

            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                text = json.loads(result).get("text", "")
                if text.strip():
                    text_box.insert(tk.END, f"✅ You said: {text}\n")
                    text_box.see(tk.END)
                    perform_task(text)


# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("🎤 Offline Voice Assistant")
root.geometry("550x450")

label = tk.Label(root, text="Press the button and speak:", font=("Arial", 14))
label.pack(pady=10)

btn = tk.Button(root, text="🎙 Start Listening", font=("Arial", 12),
                command=start_listening_thread, bg="lightblue")
btn.pack(pady=10)

text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=65, height=20, font=("Arial", 10))
text_box.pack(pady=10)

# ---- Assistant introduces itself automatically ----
load_model("English")  # Default model
speak("I am your offline voice assistant")

root.mainloop()
