import speech_recognition as sr
import win32com.client as wincl
import os
import webbrowser


def say(text):
    # Setting the voice engine for the assistant to speak
    # Using the built in SAPI's SAPI.SpVoice class
    speak = wincl.Dispatch("SAPI.SpVoice")

    # Setting the voice type for the assistant, 0 for male voice, 1 for female voice
    speak.Voice = speak.GetVoices().Item(1)

    # Set the speech rate (speed)
    speak.Rate = 2

    speak.Speak(text)


say("Hello, I am your personal assistant. What can I do for you?")


def listen():
    # Object to recognize text from audio
    r = sr.Recognizer()

    # Using the microphone as source for input
    with sr.Microphone() as source:
        print("Listening...")
        # Pause for 1 second and create the audio source file
        r.pause_threshold = 0.5
        # Listening and storing speech in audio
        audio = r.listen(source)
        try:
            # Recognizing the text from audio
            print("Recognizing...")
            text = r.recognize_google(audio, language="en-in")
            print("You said: {}".format(text))
            return text
        except:
            print("Sorry, I didn't get that.")
            return "Sorry, I didn't get that."


def execute_system_command(command):
    os.system(command)


query = listen()
query = query.lower()
if "open youtube" in query:
    webbrowser.open("https://youtube.com")
