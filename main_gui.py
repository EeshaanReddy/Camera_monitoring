from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import sys
import cv2
import numpy as np
import face_recognition
import os
import time
import csv

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./main_assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def print_text():
    t_now = time.localtime()
    file_object_s = open('Time_Stamps.txt', 'a')
    file_object_s.write(f'\n-- SESSION HAS STARTED -- AT -- {time.strftime("%H:%M:%S", t_now)} --')
    print(time.strftime("%H:%M:%S", t_now))    
    

def helloCallBack():
    path = 'pics'
    images = []
    classNames = []
    time_stamp_list = []
    myList = os.listdir(path)

    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
        #print(classNames)
    
    encodeListKnown = findEncodings(images)
    cap = cv2.VideoCapture(0)
    
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)

            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)

        if not facesCurFrame:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            time_stamp_list.append(current_time)
        else: 
            if len(time_stamp_list)>40:
                start_ = time_stamp_list[0]
                stop_ = time_stamp_list[-1]
                file_object_ss = open('Time_Stamps.txt', 'a')
                file_object_ss.write(f'\n face not detected from -- {start_} -- to -- {stop_} --')
                print(start_)
                print(stop_)
                time_stamp_list = []
            else:
                time_stamp_list = []
        cv2.imshow('Webcam',img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            cv2.destroyAllWindows()
            break

window = Tk()

window.geometry("1512x982")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 982,
    width = 1512,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    756.0,
    491.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print_text(),helloCallBack()],
    relief="flat"
)
button_1.place(
    x=405.5,
    y=800.8970336914062,
    width=301.0,
    height=68.57296752929688
)

window.resizable(False, False)
window.mainloop()
