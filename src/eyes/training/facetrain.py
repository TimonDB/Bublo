import os
import cv2
import numpy as np
from PIL import Image

from src.utils import get_project_root


class FaceTrainer:
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.dataset_path = str(get_project_root()) + "/src/eyes/dataset"
        self.recognizer_path = str(get_project_root()) + "/src/eyes/recognizer/trainingData.yml"

    def train(self):
        ids, faces = get_images_with_name(self.dataset_path)
        self.recognizer.train(faces, ids)
        self.recognizer.save(self.recognizer_path)


def get_images_with_name(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    ids = []
    for image_path in image_paths:
        if ".DS_Store" in image_path:
            pass
        else:
            face_img = Image.open(image_path).convert('L')
            face_np = np.array(face_img, 'uint8')
            id = int(os.path.split(image_path)[-1].split('.')[1])
            faces.append(face_np)
            ids.append(id)

    return np.array(ids), faces



