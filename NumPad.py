from tkinter import *

keypad=Tk()
keypad.title("keypad")
btn1=Button(keypad,padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='1').grid(row=1,column=0)
btn2=Button(keypad,padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='2').grid(row=1,column=1)
btn3=Button(keypad,padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='3').grid(row=1,column=2)
btn4=Button(keypad,padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='4').grid(row=2,column=0)
btn5=Button(keypad,padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='5').grid(row=2,column=1)
btn6=Button(keypad,padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='6').grid(row=2,column=2)
btn7=Button(keypad,padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='7').grid(row=3,column=0)
btn8=Button(keypad,padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='8').grid(row=3,column=1)
btn9=Button(keypad,padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='9').grid(row=3,column=2)
keypad.mainloop()

