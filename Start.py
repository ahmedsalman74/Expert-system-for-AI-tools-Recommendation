from tkinter import *
from PIL import ImageTk, Image

import os
app = Tk()
app.title("aitools")
app.iconbitmap(r'Images\SoundKitAid.ico')
app.resizable(0, 0)
ws= app.winfo_screenwidth()
wh= app.winfo_screenheight()

def run():
    app.destroy()
    os.system('python aitools.py')
w = 650
h = 450
ws = app.winfo_screenwidth()
hs = app.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
app.geometry('%dx%d+%d+%d' % (w, h, x, y))
imgTemp = Image.open("images/wallpaper1.png")
img2 = imgTemp.resize((w,h))
img = ImageTk.PhotoImage(img2)
Background = Label(app,image=img)
Background.pack(side='top',fill=Y,expand=True)

Button=Button(app,text="Start",font=("jetbrains mono",30),relief='flat', highlightthickness=0, bd=0,bg="#350c35",fg="white",command=run)
Button.place(x=270,y=300)

app.mainloop()