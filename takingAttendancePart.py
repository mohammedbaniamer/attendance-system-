import csv
import datetime
import time

import cv2
import os
import pandas as pd
from PIL import Image


def Attendace(recognizer, faceCascade):
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Student No.', 'Name', 'Date', 'Time']
    start = time.time()
    last_reg_st = 'no one'

    image = Image.open('./system/all data/how to move/unknown.jpg')
    new_image = image.resize((100, 100))
    # frame[y:y + img_height, x:x + img_width] = img
    while True:
        df = pd.read_csv('./system/all data/RegisteredStudents.csv')
        ret, im = cam.read()
        img = im
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        flag = False
        for (x, y, w, h) in faces:
            rowNum, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            print(rowNum, confidence)
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y')
            timee = datetime.datetime.fromtimestamp(ts).strftime('%H;%M;%S')
            if confidence < 40:
                name = df.loc[df['Row'] == rowNum]['NAME'].values[0]
                ID = df.loc[df['Row'] == rowNum]['ID'].values[0]
                studentInfo = [str(ID), name, date, str(timee)]
                flag = True
            else:
                name = 'Unknown'
                ID = 'Unknown'
                studentInfo = [str(ID), name, date, str(timee)]
                flag = False
            string = name
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (x, y + h)
            fontScale = 1
            if flag:
                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                fontColor = (255, 255, 255)
            else:
                fontColor = (0, 0, 255)
                cv2.rectangle(im, (x, y), (x + w, y + h), fontColor, 2)

            lineType = 2

            cv2.putText(img, string,
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)
            img = img[y:y + h, x:x + w]
        # cv2.imshow('Taking Attendance', im)
        if (time.time() - start > 5 and len(faces) != 0) or flag:
            start = time.time()
            last_reg_st = name
            cv2.putText(im, last_reg_st + ' has been registered',
                        (10, 50),
                        font,
                        1,
                        (255, 255, 255),
                        3)
            cv2.imshow('Taking Attendance', im)

            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
            file = './system/all data\ ' + date
            exists = os.path.exists(file)
            path = './system/all data\ Present Students Images' + date
            csvFile = "./system/all data\ " + date + "\ Present Students.csv"
            if exists:
                df = pd.read_csv(csvFile, names=col_names)
                if str(ID) in list(df['Student No.']) and str(studentInfo[0]) != 'Unknown':
                    pass
                else:
                    if str(studentInfo[0]) == 'Unknown':
                        cv2.imwrite(
                            file + '\ Present Students Images\ UNKNOWN_STUDENTS\ ' + name + '_' + str(timee) + '.jpg',
                            img)
                    else:
                        cv2.imwrite(file + '\ Present Students Images\ ' + name + '.jpg', img)
                    with open(csvFile, 'a+') as csvFile1:
                        writer = csv.writer(csvFile1)
                        writer.writerow(studentInfo)
                    csvFile1.close()

            else:

                os.mkdir(file)
                with open(file + '\ Present Students.csv', 'a+') as csvFile1:
                    writer = csv.writer(csvFile1)
                    writer.writerow(col_names)
                    writer.writerow(studentInfo)
                os.mkdir(file + '\ Present Students Images')
                os.mkdir(file + '\ Present Students Images\ UNKNOWN_STUDENTS')
                if str(studentInfo[0]) == 'Unknown':
                    cv2.imwrite(
                        file + '\ Present Students Images\ UNKNOWN_STUDENTS\ ' + name + '_' + str(timee) + '.jpg', img)
                else:
                    cv2.imwrite(file + '\ Present Students Images\ ' + name + '.jpg', img)
                csvFile1.close()
            print(name, 'has been registered')
            if cv2.waitKey(50) & 0xFF == ord('q'):
                break
        elif len(faces) == 0 or name == 'Unknown':
            cv2.putText(im, last_reg_st + ' has been registered',
                        (10, 50),
                        font,
                        1,
                        (255, 255, 255),
                        3)
            im[200:300, :100] = new_image
            cv2.imshow('Taking Attendance', im)
            if cv2.waitKey(50) & 0xFF == ord('q'):
                break
    cam.release()
    cv2.destroyAllWindows()


recognize = cv2.face.LBPHFaceRecognizer_create()
recognize.read('./system/all data/Trained data.yaml')
faceCascad = cv2.CascadeClassifier('./system/all data/haarcascade_frontalface_default.xml')
Attendace(recognize, faceCascad)


ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
tim = datetime.datetime.fromtimestamp(ts).strftime('%H;%M;%S')
csvv = './system/all data\ ' + date + '\ Absent Students.csv'
if os.path.isfile(csvv):
    os.remove(csvv)
with open(csvv, 'a+') as csvFile1:
    writer = csv.writer(csvFile1)
    writer.writerow(['Student No.', 'Name', 'Date', 'Time'])
    df = pd.read_csv('./system/all data/RegisteredStudents.csv')
    ds = pd.read_csv('./system/all data/ ' + date + '/ Present Students.csv')
    for i in df['ID'].values:
        if i not in ds['Student No.'].values:
            writer.writerow([str(i), df.loc[df['ID'] == i]['NAME'].values[0], str(date), str(tim)])
csvFile1.close()
