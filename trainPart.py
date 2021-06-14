import detect_face_webcam
import detect_face_video
import train_detected_faces
import tkinter as tk
from tkinter import simpledialog


def GUI():
    application_window = tk.Tk()

    ret = simpledialog.askinteger("Input", "choose \n0 for live video\n1 for saved video\n'",
                                  parent=application_window,
                                  minvalue=0, maxvalue=1)

    return ret


if GUI():
    detect_face_video.detect_face()
else:
    detect_face_webcam.detect_face()
print('detecting is done')
train_detected_faces.Training()
print('training is done')
