import tkinter as tk
from tkinter import *
import pyttsx3
engine = pyttsx3.init()
def speaknow():
    text = textv.get()
    if text:  
        engine.say(text)
        engine.runAndWait()
    else:
        print("Please enter some text.")
root = Tk()
textv = StringVar()
obj = LabelFrame(root, text="Text To Speech", font=("Arial", 16), bd=1)
obj.grid(row=0, column=0, padx=20, pady=10)
lbl = Label(obj, text="Text", font=("Arial", 14))
lbl.grid(row=0, column=0, padx=5, pady=5)
text = Entry(obj, textvariable=textv, font=("Arial", 14), width=25, bd=5)
text.grid(row=0, column=1, padx=5, pady=5)
btn = Button(obj, text="Speak", font=("Arial", 12), bg="black", fg="white", command=speaknow)
btn.grid(row=1, column=1, padx=10, pady=5)
root.title("Text To Speech")
root.geometry("400x150")
root.resizable(False, False)
root.mainloop()



