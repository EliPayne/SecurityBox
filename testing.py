from tkinter import *
from getpass import getpass
from Face_Rec_lib import Pics, Model, Rec
from base_logic import create_connection, create_table, convertToBinaryData, insertBLOB, insert_DB
from add_remove import Add, Remove
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
# Create object
root = Tk()
root.title('testing')
# Adjust size
root.geometry('800x480')
root.config(bg='black')
root.attributes('-fullscreen', True)
db = create_connection('facebase.db')
id = 0
#VideoStream(src=0,framerate=10).start()
#insert_DB('facebase.db')

idt = False


def open():
    top = Tk()
    top.geometry('800x480')
    top.title('Admin Settings')
    top.config(bg= 'black')
    pswrd_entry = Entry(top, width=25, show="*").grid(row=0,column = 1,sticky="NSEW" )
    pswrd_tempt = Button(top,width= 25,height=2,text="Enter", command = passentry).grid(row=1,column = 1,sticky="NSEW")
    cls_btn = Button(top,text="Home",width=5,height=2, command= top.destroy).grid(row=0,column = 0,sticky="NSEW")
    numOne_btn =Button(top,text= "1",height=3,width=3,command= lambda:print("tapped 1")).grid(row=2,column = 2)
    numTwo_btn =Button(top,text= "2",height=3,width=3,command= lambda:print("tapped 2")).grid(row=2,column = 3)
    numThree_btn =Button(top,text= "3",height=3,width=3,command= lambda:print("tapped 3")).grid(row=2,column = 4)
    numFour_btn =Button(top,text= "4",height=3,width=3,command= lambda:print("tapped 4")).grid(row=3,column = 2)
    numFive_btn =Button(top,text= "5",height=3,width=3,command= lambda:print("tapped 5")).grid(row=3,column = 3)
    numtSix_btn =Button(top,text= "6",height=3,width=3,command= lambda:print("tapped 6")).grid(row=3,column = 4)
    numSeven_btn =Button(top,text= "7",height=3,width=3,command= lambda:print("tapped 7")).grid(row=4,column = 2)
    numEight_btn =Button(top,text= "8",height=3,width=3,command= lambda:print("tapped 8")).grid(row=4,column = 3)
    numNine_btn =Button(top,text= "9",height=3,width=3,command= lambda:print("tapped 9")).grid(row=4,column = 4)
    numSeven_btn =Button(top,text= "*",height=3,width=3,command= lambda:print("tapped *")).grid(row=5,column = 2)
    numEight_btn =Button(top,text= "0",height=3,width=3,command= lambda:print("tapped 0")).grid(row=5,column = 3)
    numNine_btn =Button(top,text= "#",height=3,width=3,command= lambda:print("tapped #")).grid(row=5,column = 4)


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
    top = Tk()
    top.geometry('800x480')
    top.title('New User Id')
    top.config(bg= 'black')
    pswrd_entry = Entry(top, width=25, show="*").grid(row=0,column = 1,sticky="NSEW" )
    pswrd_tempt = Button(top,width= 25,height=2,text="Enter", command = Pics(id,db)).grid(row=1,column = 1,sticky="NSEW")
    cls_btn = Button(top,text="Home",width=5,height=2, command= top.destroy).grid(row=0,column = 0,sticky="NSEW")
    numOne_btn =Button(top,text= "1",height=3,width=3,command= lambda:print("tapped 1")).grid(row=2,column = 2)
    numTwo_btn =Button(top,text= "2",height=3,width=3,command= lambda:print("tapped 2")).grid(row=2,column = 3)
    numThree_btn =Button(top,text= "3",height=3,width=3,command= lambda:print("tapped 3")).grid(row=2,column = 4)
    numFour_btn =Button(top,text= "4",height=3,width=3,command= lambda:print("tapped 4")).grid(row=3,column = 2)
    numFive_btn =Button(top,text= "5",height=3,width=3,command= lambda:print("tapped 5")).grid(row=3,column = 3)
    numtSix_btn =Button(top,text= "6",height=3,width=3,command= lambda:print("tapped 6")).grid(row=3,column = 4)
    numSeven_btn =Button(top,text= "7",height=3,width=3,command= lambda:print("tapped 7")).grid(row=4,column = 2)
    numEight_btn =Button(top,text= "8",height=3,width=3,command= lambda:print("tapped 8")).grid(row=4,column = 3)
    numNine_btn =Button(top,text= "9",height=3,width=3,command= lambda:print("tapped 9")).grid(row=4,column = 4)
    numSeven_btn =Button(top,text= "*",height=3,width=3,command= lambda:print("tapped *")).grid(row=5,column = 2)
    numEight_btn =Button(top,text= "0",height=3,width=3,command= lambda:print("tapped 0")).grid(row=5,column = 3)
    numNine_btn =Button(top,text= "#",height=3,width=3,command= lambda:print("tapped #")).grid(row=5,column = 4)
    #Pics()
    #Model()
    

def removeUser():
    top = Tk()
    top.geometry('800x480')
    top.title('New User Id')
    top.config(bg= 'black')
    pswrd_entry = Entry(top, width=25, show="*").grid(row=0,column = 1,sticky="NSEW" )
    pswrd_tempt = Button(top,width= 25,height=2,text="Enter", command = Remove('facebase.db',id)).grid(row=1,column = 1,sticky="NSEW")
    cls_btn = Button(top,text="Home",width=5,height=2, command= top.destroy).grid(row=0,column = 0,sticky="NSEW")
    numOne_btn =Button(top,text= "1",height=3,width=3,command= lambda:print("tapped 1")).grid(row=2,column = 2)
    numTwo_btn =Button(top,text= "2",height=3,width=3,command= lambda:print("tapped 2")).grid(row=2,column = 3)
    numThree_btn =Button(top,text= "3",height=3,width=3,command= lambda:print("tapped 3")).grid(row=2,column = 4)
    numFour_btn =Button(top,text= "4",height=3,width=3,command= lambda:print("tapped 4")).grid(row=3,column = 2)
    numFive_btn =Button(top,text= "5",height=3,width=3,command= lambda:print("tapped 5")).grid(row=3,column = 3)
    numtSix_btn =Button(top,text= "6",height=3,width=3,command= lambda:print("tapped 6")).grid(row=3,column = 4)
    numSeven_btn =Button(top,text= "7",height=3,width=3,command= lambda:print("tapped 7")).grid(row=4,column = 2)
    numEight_btn =Button(top,text= "8",height=3,width=3,command= lambda:print("tapped 8")).grid(row=4,column = 3)
    numNine_btn =Button(top,text= "9",height=3,width=3,command= lambda:print("tapped 9")).grid(row=4,column = 4)
    numSeven_btn =Button(top,text= "*",height=3,width=3,command= lambda:print("tapped *")).grid(row=5,column = 2)
    numEight_btn =Button(top,text= "0",height=3,width=3,command= lambda:print("tapped 0")).grid(row=5,column = 3)
    numNine_btn =Button(top,text= "#",height=3,width=3,command= lambda:print("tapped #")).grid(row=5,column = 4)
    


    
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