import cv2
import os
import numpy as np
from PIL import Image


def Training():
    imagePaths = []
    path = './system/all data/StudentImages'
    for i in os.listdir(path):
        imagePaths.append(os.path.join(path, i))
    detected_images = []
    studentID = []

    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        detected_images.append(imageNp)
        studentID.append(ID)
    # print(detected_images, studentID)
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    recognizer.train(detected_images, np.array(studentID))
    recognizer.save('./system/all data/Trained data.yaml')
