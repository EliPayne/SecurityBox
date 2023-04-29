from tkinter import *
from NumPad import *
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
    master_window = Tk()
    master_window.geometry("300x300")
    master_window.title("StringVar get() example")
 
    def print_data():
        var = string_variable.get()
        print(string_variable.get())
        if var == "1010":
            passentry()
            master_window.destroy()
 
    string_variable = StringVar(master_window)
 
    label = Label(master_window, text="Passcode: ")
    label.grid(row=0, column=0)
 
    entry = Entry(master_window, textvariable=string_variable)
    entry.grid(row=0, column=1)
    NumpadEntry(entry)
    button = Button(master_window, text="Enter", command=print_data)
    button.grid(row=1, column=0, columnspan=2)

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
    master_window = Tk()
    master_window.geometry("300x300")
    master_window.title("StringVar get() example")
 
    def print_data():
        id = string_variable.get()
        Pics(id)
        Model()
        master_window.destroy()
 
    string_variable = StringVar(master_window)
 
    label = Label(master_window, text="New User ID: ")
    label.grid(row=0, column=0)
 
    entry = Entry(master_window, textvariable=string_variable)
    entry.grid(row=0, column=1)
 
    button = Button(master_window, text="enter", command=print_data)
    button.grid(row=1, column=0, columnspan=2)
    #Pics()
    #Model()
    

def removeUser():
    master_window = Tk()
    master_window.geometry("800x480")
    master_window.config(bg='black')
    master_window.title("StringVar get() example")
 
    def print_data():
        root = 'dataset'
        id = string_variable.get()
        list = id.split(",")
        for i in list:
            path = os.path.join(root, i)
            shutil.rmtree(path)
        master_window.destroy()
        Model()
        
 
    string_variable = StringVar(master_window)
 
    label = Label(master_window, text="New User ID: ")
    label.grid(row=0, column=0)
 
    entry = Entry(master_window, textvariable=string_variable)
    entry.grid(row=0, column=1)
 
    button = Button(master_window, text="enter", command=print_data)
    button.grid(row=1, column=0, columnspan=2)


def passcheck(var):
    if var.get() == passcode:
        passentry()
        
#def UserR():
    #remove = Tk()
    #label = Label(remove, text="User Removed")
    #time.sleep(5)
    #remove.destroy()
    
#def UserA():
    #add = Tk()
    #label = Label(add, text="User Added")
    #time.sleep(5)
    #add.destroy()
    
#def lock():
    #if(idt == True):
        #Open()
        


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