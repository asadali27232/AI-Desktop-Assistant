import win32com.client as wincl


class Sayer:
    def __init__(self):
        pass

    def say(self, text):
        # Setting the voice engine for the assistant to speak
        # Using the built in SAPI's SAPI.SpVoice class
        speak = wincl.Dispatch("SAPI.SpVoice")

        # Setting the voice type for the assistant, 0 for male voice, 1 for female voice
        speak.Voice = speak.GetVoices().Item(1)

        # Set the speech rate (speed)
        speak.Rate = 2

        speak.Speak(text)
