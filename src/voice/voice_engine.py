import pyttsx3


class VoiceEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')
        self.engine.setProperty('rate', 155)

    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
