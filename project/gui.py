import tkinter as tk
from tkinter import font as f
from tkinter import Text
from tkinter import *
#from tkinter.ttk import *
from PIL import Image,ImageTk

window = Tk()
window.geometry("1100x600")
window.resizable(0,0)

mainLabel = Label(window, text="WELCOME TO DATA CRAWLER", fg="#00FF44",bg="black",relief=RAISED,font=("Scary",16,"bold"))
mainLabel.pack(fill = BOTH, padx = 2, pady = 2)

topFrame = Frame(window)
topFrame.pack(expand = True, fill = BOTH)
topFrame.configure(background = "#EFF0F1")
logo = Image.open("a.png")
image = logo.resize((250, 250), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
lab = Label(topFrame, image=photo)
lab.place(x=425,y=10)

searchKeyword = StringVar()
bottomFrame = Frame(window)
bottomFrame.pack(side = BOTTOM, expand = True, fill = BOTH)
searchEntry = Entry(bottomFrame, width = 35, font=10, textvariable = searchKeyword,bd=5)
searchEntry.place(x = 400, y = 30)
searchLabel = Label(bottomFrame, text = "Enter Keyword", font=("arial",13,"bold"))
searchLabel.place(x = 270,y = 27)
searchButton = Button(bottomFrame,text="Search",bg="#00FF44",relief=GROOVE,font=("Scary",13,"bold"))
searchButton.place(x = 740,y = 25)

#Voice Search
voice_image = PhotoImage(file = "microphone.png")
voice_button = Button(bottomFrame, image = voice_image, width = 30, height = 28, relief=GROOVE,bg="#00FF44")
voice_button.place(x = 830, y = 24)

loc_checkBox = Checkbutton(bottomFrame, text = "Search in my Location")
loc_checkBox.place(x = 500, y = 65)

window.mainloop()