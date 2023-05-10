# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import cv2

# Create an instance of TKinter Window or frame
win = Tk()
# Set the size of the window
win.geometry("800x480")

# Create a Label to capture the Video frames
label =Label(win)
label.grid(row=0, column=0)
cap= cv2.VideoCapture(0)
frame = cap.read()

def capture():
   img_name = "dataset/"+ id +"/image_{}.png".format(img_counter)
   cv2.imwrite(img_name, frame)
   print("{} written!".format(img_name))
   img_counter += 1
   
def exit():
   win.destroy()
   cap.release()
   cv2.destroyAllWindows()
   

Snap = Button(win, text = 'Snap!',font=('Bold',20),bd = 0, command= lambda: capture)
Snap.place(x=650, y=5, width=100,height=100)
cls = Button(win, text = 'Close',font=('Bold',20),bd = 0, command= lambda: exit)
cls.place(x=650, y=100, width=100,height=100)

# Define function to show frame
def show_frames():
# Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)
   
show_frames()
mainloop()