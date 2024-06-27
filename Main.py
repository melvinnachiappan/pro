import numpy as np

from tkinter import *
import os
from tkinter import filedialog
import cv2
import time


def endprogram():
    print("\nProgram terminated!")
    sys.exit()


def cocr():
    import cv2 as cv

    import easyocr

    import win32com.client as wincl
    speak = wincl.Dispatch("SAPI.SpVoice")
    font = cv.FONT_HERSHEY_SIMPLEX
    reader = easyocr.Reader(['en'])

    cap = cv.VideoCapture(0)

    frame_count = 0
    while (cap.isOpened()):
        hasFrame, frame = cap.read()
        if hasFrame:
            frame_count += 1
            print(frame_count)
            if frame_count % 5 == 0:  # process every other frame to save time
                img = frame
                result = reader.readtext(img)
                for detection in result:
                    text = detection[1]
                    print(text)
                    speak.Speak(text)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

            cv.imshow('frame', frame)
        else:
            break

    cv.destroyAllWindows()
    cap.release()


def imgtraining():
    name1 = clicked.get()

    print(name1)

    import_file_path = filedialog.askopenfilename()
    import os
    s = import_file_path
    os.path.split(s)
    os.path.split(s)[1]
    splname = os.path.split(s)[1]

    image = cv2.imread(import_file_path)
    # filename = 'Test.jpg'
    filename = 'Data/' + name1 + '/' + splname

    cv2.imwrite(filename, image)
    print("After saving image:")
    image = cv2.resize(image, (780, 540))

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original image', image)
    cv2.imshow('Gray image', gray)
    # import_file_path = filedialog.askopenfilename()
    print(import_file_path)
    fnm = os.path.basename(import_file_path)
    print(os.path.basename(import_file_path))

    from PIL import Image, ImageOps

    im = Image.open(import_file_path)

    im_invert = ImageOps.invert(im)
    im_invert.save('lena_invert.jpg', quality=95)
    im = Image.open(import_file_path).convert('RGB')

    im_invert = ImageOps.invert(im)
    im_invert.save('tt.png')
    image2 = cv2.imread('tt.png')
    image2 = cv2.resize(image2, (780, 540))
    cv2.imshow("Invert", image2)

    """"-----------------------------------------------"""

    img = image

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original image', img)

    dst = cv2.medianBlur(img, 7)
    cv2.imshow("Nosie Removal", dst)


def main_account_screen():
    global main_screen
    main_screen = Tk()
    width = 600
    height = 600
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    main_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    main_screen.resizable(0, 0)
    # main_screen.geometry("300x250")
    main_screen.title(" Object Detection")

    Label(text="Object Detection", width="300", height="5", font=("Calibri", 16)).pack()

    Button(text="Object Detection", font=(
        'Verdana', 15), height="2", width="30", command=Object, highlightcolor="black").pack(side=TOP)

    Label(text="").pack()

    Label(text="").pack()

    main_screen.mainloop()


main_account_screen()
