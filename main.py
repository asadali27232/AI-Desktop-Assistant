import win32com.client as wincl


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
