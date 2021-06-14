import cv2
import csv
from PIL import Image
import tkinter as tk
from tkinter import simpledialog


def GUI():
    application_window = tk.Tk()

    name = simpledialog.askstring("Input", "enter student first and last name: ",
                                    parent=application_window)

    ID = simpledialog.askinteger("Input", "enter student ID number",
                                     parent=application_window,
                                     minvalue=100000, maxvalue=999999)

    ext = simpledialog.askstring("Input", "enter video extinsion: ",
                                   parent=application_window
                                   )
    return name, str(ID), ext


def detect_face():

    name, Id, videoExtinsion = GUI()
    # name = 'mohammed samarah'
    # Id = '128384'
    # videoExtinsion = 'mov'

    videoExtinsion = '.' + videoExtinsion
    nameV = name + '_' + Id
    nameV = nameV.lower()
    print(nameV)

    cam = cv2.VideoCapture('./system/all data/videos/' + nameV + videoExtinsion)
    i = 0
    detector = cv2.CascadeClassifier("./system/all data/haarcascade_frontalface_default.xml")
    sampleNum = 0
    with open("./system/all data/RegisteredStudents.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        serial = int(len(list(reader1)) / 2)
    csvFile1.close()
    path = './system/all data/how to move'
    s = 34
    while cam.isOpened() and i < 500:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        if s == 143:
            s = 35
        else:
            s += 1
        image = Image.open('./system/all data/how to move/' + str(s) + 'image.png')
        new_image = image.resize((150, 150))
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            sampleNum = sampleNum + 1
            cv2.imwrite("./system/all data/StudentImages/" + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                        gray[y:y + h, x:x + w])
            string = str(500 - sampleNum)
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (5, 250)
            fontScale = 1
            fontColor = (255, 255, 255)
            lineType = 2

            cv2.putText(img, string,
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)
            img[:150, :150] = new_image
            cv2.imshow('Taking Images', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif sampleNum > 500:
            break
    cam.release()
    cv2.destroyAllWindows()
    row = [serial, Id, name]
    with open('./system/all data/RegisteredStudents.csv', 'a+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
