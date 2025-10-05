
    #     now = datetime.datetime.now().strftime("%H:%M:%S")
    #     speak(f"The current time is {now}")

    # elif intent == "date":
    #     today = datetime.datetime.now().strftime("%B %d, %Y")
    #     speak(f"Today's date is {today}")

    # elif intent == "calculate":
    #     try:
    #         expr = command.replace("calculate", "").replace("plus", "+").replace("minus", "-")
    #         expr = expr.replace("times", "*").replace("divided by", "/")
    #         result = eval(expr.strip())
    #         speak(f"The answer is {result}")
    #     except:
    #         speak("Sorry, I cannot calculate that.")

    # elif intent == "joke":
    #     jokes = [
    #         "Why did the computer go to the doctor? Because it caught a virus!",
    #         "Why was the computer cold? It left its Windows open!"
    #     ]
    #     speak(random.choice(jokes))

    # elif intent == "hindi":
    #     load_model("Hindi")
    #     speak("Language switched to Hindi")

    # elif intent == "english":
    #     load_model("English")
    #     speak("Language switched to English")

    # else:
    #     speak("Sorry, I didn't understand that command.")
