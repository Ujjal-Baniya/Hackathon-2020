import speech_recognition as sr
import tkinter as tk
from tkinter import font as f
from tkinter import Text
from tkinter import*
from PIL import Image,ImageTk


def sresult():
    mic =sr.Microphone()
    r=sr.Recognizer()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    a= (r.recognize(audio))
    return a
s=sresult()
print(s)