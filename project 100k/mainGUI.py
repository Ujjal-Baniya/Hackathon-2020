import tkinter as tk
from PIL import Image,ImageTk
HEIGHT = 500
WIDTH = 600

root = tk.Tk()
canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

def get_result():
    #main(keyword)
    #file = open('result.txt','r')
    #lst= file.readlines()
    stri="HELLO"
    label['text']=stri

img=Image.open("rt.jpg")
photo=ImageTk.PhotoImage(img)
lab=tk.Label(image=photo)
lab.place(relheight=1,relwidth=1)

frame = tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.75,anchor='n')

button =  tk.Button(frame, text="Search",command=lambda: get_result)
button.place(relx=0.7,relwidth=0.3,relheight=1)

entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

lower_frame = tk.Frame(root,bg="#80c1ff",bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label = tk.Label(lower_frame)
label.place(relx=1,rely=1)


root.mainloop()