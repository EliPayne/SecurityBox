import tkinter as tk

root = tk.Tk()
root.geometry('800x480')
root.title('Tkinter Hub')
root.tk_setPalette('gray')

def inser_number(number):
    dialer_entry.insert(tk.INSERT, number)
    
def delNum():
    index = int(dialer_entry.index(tk.INSERT)) -1 
    dialer_entry.delete(index)
    print(index)
    
def GetNum():
    num = dialer_entry.get()
    print(num)
    
def Exit():
    root.destroy()

dialer_frame = tk.Frame(root)
dialer_frame.pack()

dialer_input_fm = tk.Frame(dialer_frame)

dialer_entry = tk.Entry(dialer_input_fm, font=('Bold',25), bd= 0, justify=tk.CENTER)

dialer_entry.place(x=30, y=20, width=210)

dialer_input_fm.pack(pady=10)
dialer_input_fm.pack_propagate(False)
dialer_input_fm.configure(width=290, height=80)

delete_btn_img = tk.PhotoImage(file='btn.png')
delete_btn = tk.Button(dialer_frame, image=delete_btn_img, bd=0, command=delNum)
delete_btn.place(x=450, y=115)

enter_btn_img = tk.PhotoImage(file='enter.png')
enter_btn = tk.Button(dialer_frame, image=enter_btn_img, bd=0, command= GetNum)
enter_btn.place(x=430, y=185)

dialer_pad_fm = tk.Frame(dialer_frame)

one_btn = tk.Button(dialer_pad_fm, text='1', font=('Bold', 20), bd=0, command=lambda: inser_number(1))
one_btn.place(x=100, y=5, width=100, height=70)
two_btn = tk.Button(dialer_pad_fm, text='2', font=('Bold', 20), bd=0, command= lambda: inser_number(2))
two_btn.place(x=200, y=5, width=100, height= 70)
three_btn = tk.Button(dialer_pad_fm, text='3', font=('Bold', 20), bd=0, command=lambda: inser_number(3))
three_btn.place(x=300, y=5, width=100,height=70)
four_btn = tk.Button(dialer_pad_fm, text='4', font=('Bold', 20), bd=0, command=lambda: inser_number(4))
four_btn.place(x=100, y=75, width=100,height=70)
five_btn = tk.Button(dialer_pad_fm, text='5', font=('Bold', 20), bd=0, command=lambda: inser_number(5))
five_btn.place(x=200, y=75, width=100,height=70)
six_btn = tk.Button(dialer_pad_fm, text='6', font=('Bold', 20), bd=0, command=lambda: inser_number(6))
six_btn.place(x=300, y=75, width=100 ,height=70)
seven_btn = tk.Button(dialer_pad_fm, text='7', font=('Bold', 20), bd=0, command=lambda: inser_number(7))
seven_btn.place(x=100, y=145, width=100, height=70)
eight_btn = tk.Button(dialer_pad_fm, text='8', font=('Bold', 20), bd=0, command=lambda: inser_number(8))
eight_btn.place(x=200, y=145, width=100,height=70)
nine_btn = tk.Button(dialer_pad_fm, text='9', font=('Bold', 20), bd=0, command=lambda: inser_number(9))
nine_btn.place(x=300, y=145, width=100, height= 70)
zero_btn = tk.Button(dialer_pad_fm, text='0', font=('Bold', 20), bd=0, command= lambda: inser_number(0))
zero_btn.place(x=200, y=215, width=100,height=70)

close_btn = tk.Button(dialer_frame, text='Back',font=('Bold', 20), bd = 0, command= Exit)
close_btn.place(x=5, y= 5, width=100, height=100)



dialer_pad_fm.place(x=35, y=100, width=400, height=480)

dialer_frame.pack_propagate(False)
dialer_frame.configure(width=800,height=480)


root.mainloop()