import speech_recognition as sr


class Listener:
    def __init__(self):
        pass

    def listen(self):
        # Object to recognize text from audio
        r = sr.Recognizer()

        # Using the microphone as source for input
        with sr.Microphone() as source:
            # Pause for 1 second and create the audio source file
            r.pause_threshold = 1
            # Listening and storing speech in audio
            audio = r.listen(source)
            try:
                # Recognizing the text from audio
                print("Recognizing...")
                text = r.recognize_google(audio, language="en-in")
                return text
            except:
                return "Listener: Sorry, I didn't get that."
