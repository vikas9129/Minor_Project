# offline_module.py

import datetime
import os
import random

def show_time(speak):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {now}")

def show_date(speak):
    today = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

def tell_joke(speak):
    jokes = [
        "Why did the computer go to the doctor? Because it caught a virus!",
        "Why was the computer cold? It left its Windows open!"
    ]
    speak(random.choice(jokes))

def calculate_expression(command, speak):
    try:
        expr = command.lower().replace("calculate", "")
        expr = expr.replace("plus", "+").replace("minus", "-")
        expr = expr.replace("times", "*").replace("divided by", "/")
        result = eval(expr.strip())
        speak(f"The answer is {result}")
    except:
        speak("Sorry, I cannot calculate that.")

def open_notepad(speak):
    os.system("notepad")
    speak("Opened Notepad")

def open_calculator(speak):
    os.system("calc")
    speak("Opened Calculator")

def shutdown(speak):
    speak("Shutting down the system...")
    os.system("shutdown /s /t 1")

def get_offline_commands():
    return {
        "time": show_time,
        "date": show_date,
        "joke": tell_joke,
        "calculate": calculate_expression,
        "open_notepad": open_notepad,
        "open_calculator": open_calculator,
        "shutdown": shutdown
    }
