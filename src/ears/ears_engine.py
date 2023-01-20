import speech_recognition as sr

from src.voice.voice_engine import VoiceEngine


class EarsEngine:
    def __init__(self, voice: VoiceEngine):
        self.recognizer = sr.Recognizer()
        self.voice = voice

    def listen(self):
        text = None
        while text is None:
            with sr.Microphone() as source:
                audio = self.recognizer.listen(source, phrase_time_limit=5)

            try:
                text = self.recognizer.recognize_google(audio, language='en-US')
            except:
                self.voice.say("Sorry, I didn't understand. Can you repeat?")

        return text
