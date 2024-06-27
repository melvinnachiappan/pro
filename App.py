import tkinter as tk
import pyttsx3
from tkinter import filedialog
#import cv2



def imgtraining():
    import_file_path = filedialog.askopenfilename()
    import cv2 as cv

    import easyocr

    import win32com.client as wincl
    speak = wincl.Dispatch("SAPI.SpVoice")
    font = cv.FONT_HERSHEY_SIMPLEX
    reader = easyocr.Reader(['en'])

    cap = cv.imread(import_file_path)
    img = cap
    result = reader.readtext(img)
    for detection in result:
        text = detection[1]
        print(text)
        speak.Speak(text)
    cv.imshow('frame', img)






def speak_text():
    text = text_entry.get("1.0", "end-1c")  # Get text from the entry widget
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

# Create the main window
root = tk.Tk()
root.title("Text to Speech")
root.geometry("500x500")

# Create a label and a multiline entry widget for text input
text_label = tk.Label(root, text="Enter text:")
text_label.pack()

text_entry = tk.Text(root, wrap="word", height=10, width=60)  # Multiline text entry
text_entry.pack(pady=10)

# Create a button to trigger text-to-speech
speak_button = tk.Button(root, text="Speak", command=speak_text)
speak_button.pack()

speak_button = tk.Button(root, text="Image", command=imgtraining)
speak_button.pack()

# Run the application
root.mainloop()