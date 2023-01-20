import cv2

from src.database.database import Database
from src.database.tables import Person
from src.utils import get_project_root, most_frequent
from src.eyes.training.facetrain import FaceTrainer


class EyesEngine:

    def __init__(self, database: Database):
        self.database = database
        self.face_detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        try:
            self.recognizer = cv2.face.LBPHFaceRecognizer_create()
            self.recognizer.read(str(get_project_root()) + "/src/eyes/recognizer/trainingData.yml")
        except:
            self.recognizer = None

    def detect_face(self) -> Person:
        if self.recognizer is None:
            return None

        cam = cv2.VideoCapture(0)

        past_detections = []
        while len(past_detections) < 30:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_detect.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                id, conf = self.recognizer.predict(gray[y:y+h, x:x+w])

                person = self.database.get_person(id)
                if person and conf < 50:
                    past_detections.append(person.id)
                else:
                    past_detections.append(None)

        cam.release()

        print(past_detections)
        most_frequent_id = most_frequent(past_detections)
        person = self.database.get_person(most_frequent_id)

        return person

    def reload_recognizer(self):
        self.recognizer.read(str(get_project_root()) + "/src/eyes/recognizer/trainingData.yml")
