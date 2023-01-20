import os
import cv2

from src.database.database import Database
from src.utils import get_project_root


class FaceData:
    def __init__(self, database: Database):
        self.database = database
        self.dataset_path = str(get_project_root()) + "/src/eyes/dataset"
        self.face_detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def register(self, input_name):
        self.database.insert_or_update(input_name)
        id = self.database.get_id_by_name(input_name)
        print(id)

        image_count = self.get_image_count(id) if id else 0

        cam = cv2.VideoCapture(0)

        sample_num = 0
        while sample_num < 30:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_detect.detectMultiScale(gray, 1.3, 5)

            for x, y, w, h in faces:
                sample_num += 1
                cv2.imwrite(self.dataset_path + f"/User.{id}.{sample_num + image_count}.jpg", gray[y:y+h, x:x+w])
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.waitKey(100)

            cv2.imshow("Face", img)
            cv2.waitKey(1)

        cam.release()
        cv2.destroyAllWindows()
        return

    def get_image_count(self, id):
        image_numbers = []
        for f in os.listdir(self.dataset_path):
            if ".DS_Store" in f:
                continue
            user_id, image_number = f.split(".")[1], int(f.split(".")[2])
            if user_id == str(id):
                image_numbers.append(image_number)

        return max(image_numbers)

