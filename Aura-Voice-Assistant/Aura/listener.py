import speech_recognition as sr

recognizer = sr.Recognizer()

def wait_for_wake_word():
    with sr.Microphone() as source:
        print("Waiting for wake word 'Aura'...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio).lower()
        print(f"You said: {text}")
        if "aura" in text:
            return True
    except sr.UnknownValueError:
        print("Didn't catch that.")
    return False

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn’t catch that.")
        return ""
