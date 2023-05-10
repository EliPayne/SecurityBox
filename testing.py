from tkinter import *
from NumPad import *
from PIL import Image, ImageTk
from getpass import getpass
from Face_Rec_lib import Pics, Model, Rec
from base_logic import create_connection, create_table, convertToBinaryData, insertBLOB, insert_DB
#from add_remove import Add, Remove
#from Lock_logic import Open, Close
import cv2
from imutils import paths
import face_recognition
import pickle
import os
import imutils
from imutils.video import VideoStream
from imutils.video import FPS
import time
import shutil
# Create object
root = Tk()
root.title('testing')
# Adjust size
root.geometry('800x480')
root.config(bg='black')
root.attributes('-fullscreen', True)
#db = create_connection('facebase.db')
id = 0
passcode = "1010"
#VideoStream(src=0,framerate=10).start()
#insert_DB('facebase.db')

idt = False


def open():
    root = Tk()
    root.geometry('800x480')
    root.title('Tkinter Hub')
    root.tk_setPalette('gray')
    
    def inser_number(number):
        dialer_entry.insert(INSERT, number)
    
    def delNum():
        index = int(dialer_entry.index(INSERT)) -1 
        dialer_entry.delete(index)
        print(index)
    
    def GetNum():
        num = dialer_entry.get()
        print(num)
        if num == passcode:
            passentry()
            root.destroy()
    
    def Exit():
        root.destroy()
 
    dialer_frame = Frame(root)
    dialer_frame.pack()
    
    dialer_input_fm = Frame(dialer_frame)

    dialer_entry = Entry(dialer_input_fm, font=('Bold',25), bd= 0, justify=(CENTER))

    dialer_entry.place(x=30, y=20, width=210)

    dialer_input_fm.pack(pady=10)
    dialer_input_fm.pack_propagate(False)
    dialer_input_fm.configure(width=290, height=80)

    delete_btn = Button(dialer_frame, text='delete', font=('Bold',20),bd=0, command=delNum)
    delete_btn.place(x=450, y=115, width=100, height=100)


    enter_btn = Button(dialer_frame, text='enter',font=('Bold',20), bd=0, command= GetNum)
    enter_btn.place(x=450, y=215,width=100, height=100)

    dialer_pad_fm = Frame(dialer_frame)

    one_btn = Button(dialer_pad_fm, text='1', font=('Bold', 20), bd=0, command=lambda: inser_number(1))
    one_btn.place(x=100, y=5, width=100, height=70)
    two_btn = Button(dialer_pad_fm, text='2', font=('Bold', 20), bd=0, command= lambda: inser_number(2))
    two_btn.place(x=200, y=5, width=100, height= 70)
    three_btn = Button(dialer_pad_fm, text='3', font=('Bold', 20), bd=0, command=lambda: inser_number(3))
    three_btn.place(x=300, y=5, width=100,height=70)
    four_btn = Button(dialer_pad_fm, text='4', font=('Bold', 20), bd=0, command=lambda: inser_number(4))
    four_btn.place(x=100, y=75, width=100,height=70)
    five_btn = Button(dialer_pad_fm, text='5', font=('Bold', 20), bd=0, command=lambda: inser_number(5))
    five_btn.place(x=200, y=75, width=100,height=70)
    six_btn = Button(dialer_pad_fm, text='6', font=('Bold', 20), bd=0, command=lambda: inser_number(6))
    six_btn.place(x=300, y=75, width=100 ,height=70)
    seven_btn = Button(dialer_pad_fm, text='7', font=('Bold', 20), bd=0, command=lambda: inser_number(7))
    seven_btn.place(x=100, y=145, width=100, height=70)
    eight_btn = Button(dialer_pad_fm, text='8', font=('Bold', 20), bd=0, command=lambda: inser_number(8))
    eight_btn.place(x=200, y=145, width=100,height=70)
    nine_btn = Button(dialer_pad_fm, text='9', font=('Bold', 20), bd=0, command=lambda: inser_number(9))
    nine_btn.place(x=300, y=145, width=100, height= 70)
    zero_btn = Button(dialer_pad_fm, text='0', font=('Bold', 20), bd=0, command= lambda: inser_number(0))
    zero_btn.place(x=200, y=215, width=100,height=70)

    close_btn = Button(dialer_frame, text='Back',font=('Bold', 20), bd = 0, command= Exit)
    close_btn.place(x=5, y= 5, width=100, height=100)



    dialer_pad_fm.place(x=35, y=100, width=400, height=480)

    dialer_frame.pack_propagate(False)
    dialer_frame.configure(width=800,height=480)

def scanning():
    print("scan tapped")
    Rec(idt) 

def passentry():
    userMod= Toplevel()
    userMod.geometry('800x480')
    userMod.title('User Modification')
    userMod.config(bg= 'black')
    addUser_btn = Button(userMod,text="Add User",height=25,width=40, command=newUser).grid(row=1,column = 0,sticky="NSEW")
    removeUser_btn = Button(userMod,text="Remove User",height=25,width=40, command= removeUser).grid(row=1,column = 1,sticky="NSEW")

def newUser():
    root = Tk()
    root.geometry('800x480')
    root.title('Tkinter Hub')
    root.tk_setPalette('gray')
 
    def inser_number(number):
        dialer_entry.insert(INSERT, number)
    
    def delNum():
        index = int(dialer_entry.index(INSERT)) -1 
        dialer_entry.delete(index)
        print(index)
    
    def GetNum():
        num = dialer_entry.get()
        print(num)
        root.destroy()
        Pics(num)
        Model()
        
    
    def Exit():
        root.destroy()
 
    dialer_frame = Frame(root)
    dialer_frame.pack()
    
    dialer_input_fm = Frame(dialer_frame)

    dialer_entry = Entry(dialer_input_fm, font=('Bold',25), bd= 0, justify=(CENTER))

    dialer_entry.place(x=30, y=20, width=210)

    dialer_input_fm.pack(pady=10)
    dialer_input_fm.pack_propagate(False)
    dialer_input_fm.configure(width=290, height=80)

    delete_btn = Button(dialer_frame, text='delete', font=('Bold',20),bd=0, command=delNum)
    delete_btn.place(x=450, y=115, width=100, height=100)


    enter_btn = Button(dialer_frame, text='enter',font=('Bold',20), bd=0, command= GetNum)
    enter_btn.place(x=450, y=215,width=100, height=100)

    dialer_pad_fm = Frame(dialer_frame)

    one_btn = Button(dialer_pad_fm, text='1', font=('Bold', 20), bd=0, command=lambda: inser_number(1))
    one_btn.place(x=100, y=5, width=100, height=70)
    two_btn = Button(dialer_pad_fm, text='2', font=('Bold', 20), bd=0, command= lambda: inser_number(2))
    two_btn.place(x=200, y=5, width=100, height= 70)
    three_btn = Button(dialer_pad_fm, text='3', font=('Bold', 20), bd=0, command=lambda: inser_number(3))
    three_btn.place(x=300, y=5, width=100,height=70)
    four_btn = Button(dialer_pad_fm, text='4', font=('Bold', 20), bd=0, command=lambda: inser_number(4))
    four_btn.place(x=100, y=75, width=100,height=70)
    five_btn = Button(dialer_pad_fm, text='5', font=('Bold', 20), bd=0, command=lambda: inser_number(5))
    five_btn.place(x=200, y=75, width=100,height=70)
    six_btn = Button(dialer_pad_fm, text='6', font=('Bold', 20), bd=0, command=lambda: inser_number(6))
    six_btn.place(x=300, y=75, width=100 ,height=70)
    seven_btn = Button(dialer_pad_fm, text='7', font=('Bold', 20), bd=0, command=lambda: inser_number(7))
    seven_btn.place(x=100, y=145, width=100, height=70)
    eight_btn = Button(dialer_pad_fm, text='8', font=('Bold', 20), bd=0, command=lambda: inser_number(8))
    eight_btn.place(x=200, y=145, width=100,height=70)
    nine_btn = Button(dialer_pad_fm, text='9', font=('Bold', 20), bd=0, command=lambda: inser_number(9))
    nine_btn.place(x=300, y=145, width=100, height= 70)
    zero_btn = Button(dialer_pad_fm, text='0', font=('Bold', 20), bd=0, command= lambda: inser_number(0))
    zero_btn.place(x=200, y=215, width=100,height=70)

    close_btn = Button(dialer_frame, text='Back',font=('Bold', 20), bd = 0, command= Exit)
    close_btn.place(x=5, y= 5, width=100, height=100)



    dialer_pad_fm.place(x=35, y=100, width=400, height=480)

    dialer_frame.pack_propagate(False)
    dialer_frame.configure(width=800,height=480)

def removeUser(): 
    root = Tk()
    root.geometry('800x480')
    root.title('Tkinter Hub')
    root.tk_setPalette('gray')
    
    def inser_number(number):
        dialer_entry.insert(INSERT, number)
    
    def delNum():
        index = int(dialer_entry.index(INSERT)) -1 
        dialer_entry.delete(index)
        print(index)
    
    def GetNum():
        dir = 'dataset'
        num = dialer_entry.get()
        print(num)
        list = num.split(",")
        for i in list:
            path = os.path.join(dir, i)
            shutil.rmtree(path)
        root.destroy()
        Model()
        
    
    def Exit():
        root.destroy()
 
    dialer_frame = Frame(root)
    dialer_frame.pack()
    
    dialer_input_fm = Frame(dialer_frame)

    dialer_entry = Entry(dialer_input_fm, font=('Bold',25), bd= 0, justify=(CENTER))

    dialer_entry.place(x=30, y=20, width=210)

    dialer_input_fm.pack(pady=10)
    dialer_input_fm.pack_propagate(False)
    dialer_input_fm.configure(width=290, height=80)

    delete_btn = Button(dialer_frame, text='delete', font=('Bold',20),bd=0, command=delNum)
    delete_btn.place(x=450, y=115, width=100, height=100)


    enter_btn = Button(dialer_frame, text='enter',font=('Bold',20), bd=0, command= GetNum)
    enter_btn.place(x=450, y=215,width=100, height=100)

    dialer_pad_fm = Frame(dialer_frame)

    one_btn = Button(dialer_pad_fm, text='1', font=('Bold', 20), bd=0, command=lambda: inser_number(1))
    one_btn.place(x=100, y=5, width=100, height=70)
    two_btn = Button(dialer_pad_fm, text='2', font=('Bold', 20), bd=0, command= lambda: inser_number(2))
    two_btn.place(x=200, y=5, width=100, height= 70)
    three_btn = Button(dialer_pad_fm, text='3', font=('Bold', 20), bd=0, command=lambda: inser_number(3))
    three_btn.place(x=300, y=5, width=100,height=70)
    four_btn = Button(dialer_pad_fm, text='4', font=('Bold', 20), bd=0, command=lambda: inser_number(4))
    four_btn.place(x=100, y=75, width=100,height=70)
    five_btn = Button(dialer_pad_fm, text='5', font=('Bold', 20), bd=0, command=lambda: inser_number(5))
    five_btn.place(x=200, y=75, width=100,height=70)
    six_btn = Button(dialer_pad_fm, text='6', font=('Bold', 20), bd=0, command=lambda: inser_number(6))
    six_btn.place(x=300, y=75, width=100 ,height=70)
    seven_btn = Button(dialer_pad_fm, text='7', font=('Bold', 20), bd=0, command=lambda: inser_number(7))
    seven_btn.place(x=100, y=145, width=100, height=70)
    eight_btn = Button(dialer_pad_fm, text='8', font=('Bold', 20), bd=0, command=lambda: inser_number(8))
    eight_btn.place(x=200, y=145, width=100,height=70)
    nine_btn = Button(dialer_pad_fm, text='9', font=('Bold', 20), bd=0, command=lambda: inser_number(9))
    nine_btn.place(x=300, y=145, width=100, height= 70)
    zero_btn = Button(dialer_pad_fm, text='0', font=('Bold', 20), bd=0, command= lambda: inser_number(0))
    zero_btn.place(x=200, y=215, width=100,height=70)

    close_btn = Button(dialer_frame, text='Back',font=('Bold', 20), bd = 0, command= Exit)
    close_btn.place(x=5, y= 5, width=100, height=100)



    dialer_pad_fm.place(x=35, y=100, width=400, height=480)

    dialer_frame.pack_propagate(False)
    dialer_frame.configure(width=800,height=480)


def passcheck(var):
    if var.get() == passcode:
        passentry()
        


# Specify Grid
Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)
Grid.rowconfigure(root,1,weight=1)
Grid.columnconfigure(root,1,weight=1)
Grid.rowconfigure(root,2,weight=1)
 
# Create Buttons
button_1 = Button(root,text="Scan",fg= 'green',height= 25,width= 25,command= scanning)
button_2 = Button(root,text="Admin",fg='red',height= 25,width= 25,command= ((open)))

# Set grid
button_1.grid(row=0,column=0,)
button_2.grid(row=0,column=1)
 
# Execute tkinter
mainloop()