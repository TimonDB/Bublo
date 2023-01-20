import random

from chatgpt_wrapper import ChatGPT

from src.voice.voice_engine import VoiceEngine
from src.eyes.eyes_engine import EyesEngine
from src.database.sqlite_database import SQLiteDatabase
from src.eyes.training.facedata import FaceData
from src.eyes.training.facetrain import FaceTrainer
from src.ears.ears_engine import EarsEngine

import pyjokes


class Bublo:
    def __init__(self):
        self.database = SQLiteDatabase()
        self.voice = VoiceEngine()
        self.eyes = EyesEngine(self.database)
        self.ears = EarsEngine(self.voice)
        self.chatgpt = ChatGPT()

    def come_to_live(self):
        self.voice.say("Hi, I'm Bublo.")

        person = self.eyes.detect_face()

        if person:
            self.voice.say(f"Oh hi {person.name}, it's good to see you again")
        else:
            self.voice.say("Hi, I don't think we've met before. May I register you in my database?")
            answer = self.ears.listen()
            if answer.lower() == "yes":
                input_name = input('Enter Name')
                face_data = FaceData(self.database)
                face_data.register(input_name)

                face_trainer = FaceTrainer()
                face_trainer.train()

                self.eyes.reload_recognizer()
                person = self.eyes.detect_face()

                if person:
                    self.voice.say(f"Oh hi {person.name}, I'm able to recognize you.")
                else:
                    self.voice.say(
                        """
                        Dammit, still no matches in my database. Maybe your ugly face is to hard to capture!
                        """)
            else:
                self.voice.say("Okay no problem. I didn't like you anyway.")

        while True:
            self.voice.say("What can I do for you?")
            command = self.ears.listen()

            if "stop" in command.lower():
                break

            self.process_command(command)

    def process_command(self, command):
        if "joke" in command.lower():
            joke = pyjokes.get_joke()
            self.voice.say(joke)

        elif "hi to mama" in command.lower():
            self.voice.say("Hi mama, pleased to meet you.")

        elif "insult" in command.lower():
            self.voice.say("Charles is fat and ugly")

        else:
            response = self.chatgpt.ask(command)
            self.voice.say(response)


if __name__ == "__main__":
    bublo = Bublo()
    bublo.come_to_live()
