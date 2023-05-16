import tkinter
from tkinter import *

import PIL
from PIL import Image,ImageTk
from tkinter import filedialog
import cv2

from tkinter.filedialog import askopenfile

def start():
    global image1,path
    global panel

    path=filedialog.askopenfile()
    image1 = cv2.imread(str(path))
    image1= cv2.resize(image1,(200,100))
    image1=cv2.cvtColor(image1,cv2.COLOR_BRG2RGB)

    image =Image.fromarray(image1)
    image=ImageTk.PhotoImage(image)

    if panel is None:
        panel=Label(image=image)
        panel.image=image
        panel.pack(side='left',padx=20,pady=60)
    else:
        panel.configure(image=image)
        panel.image=image

def gray_img():
    global panelB
    gray=cv2.cvtColor(image1,cv2.COLOR_BRG2GRAY)
    image=Image.fromarray(gray)
    image=ImageTk.PhotoImage(image)
    if panelB is None:
        panelB=Label(image=image)
        panelB.image=image
        panelB.pack(side='left',padx=30,pady=60)
    else:
        panelB.configure(image=image)
        panelB.image=image

def black_img():
    global panelB
    gray=cv2.cvtColor(image1,cv2.COLOR_BRG2GRAY)
    black=cv2.Canny(gray,50,100)
    image=Image.fromarray(black)
    image=ImageTk.PhotoImage(image)
    if panelB is None:
        panelB=Label(image=image)
        panelB.image=image
        panelB.pack(side='left',padx=30,pady=60)
    else:
        panelB.configure(image=image)
        panelB.image=image

def negative_img():
    global panelB
    negative=cv2.cvtColor(image1,cv2.COLOR_BRG2GRAY)
    negative=cv2.bitwise_not(negative)
    image=Image.fromarray(negative)
    image=ImageTk.PhotoImage(image)
    if panelB is None:
        panelB=Label(image=image)
        panelB.image=image
        panelB.pack(side='left',padx=30,pady=60)
    else:
        panelB.configure(image=image)
        panelB.image=image


root= Tk()
root.title("Image Converter")
root.geometry('600x400')
panel=None
panelB=None
fm=Frame(root,width=300,height=200)
fm.pack(side=BOTTOM,fill=None,expand=NO)

btnStart=Button(root,text='Select Image',command=start)
btnStart.pack(side='top')

btnGray=Button(fm,text='Gray',command=gray_img)
btnGray.pack(side=LEFT,padx=10,pady=10)

btnEdge=Button(fm,text='black',command=black_img)
btnEdge.pack(side=LEFT,padx=10,pady=10)

btnNegative=Button(fm,text='Gray',command=negative_img)
btnNegative.pack(side=LEFT,padx=10,pady=10)



root.mainloop()



