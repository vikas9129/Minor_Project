import json
import os
import subprocess
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def execute_offline_command(command):
    with open("commands.json", "r") as f:
        commands = json.load(f)

    for key in commands:
        if key in command:
            try:
                if "shutdown" in key:
                    os.system(commands[key])
                else:
                    subprocess.Popen(commands[key])
                speak(f"Executing {key}")
                return True
            except Exception as e:
                speak("Sorry, I couldn't execute the command")
                print(e)
                return False
    return False
