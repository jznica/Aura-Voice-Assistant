import pyttsx3
import webbrowser
import datetime
import os
import sys

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def respond_to_command(command):
    # Remove the wake word from the command if present
    command = command.replace("aura", "").strip()

    # Respond to Spotify
    if "spotify" in command:
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com")

    # Respond to ChatGPT
    elif "chat gpt" in command or "chatgpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    # Respond to YouTube
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Respond to Google
    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # Respond with the current time
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    # Respond with the current date
    elif "date" in command:
        date = datetime.datetime.now().strftime("%A, %B %d")
        speak(f"Today is {date}")

    # Give a motivational quote
    elif "quote" in command or "motivate" in command:
        speak("Believe in yourself. You are stronger than you think.")

    # Exit the assistant
    elif "exit" in command or "stop" in command or "goodbye" in command:
        speak("Goodbye, Jen.")
        sys.exit()

    # Fallback response
    else:
        speak("Sorry, I didn’t understand that.")
