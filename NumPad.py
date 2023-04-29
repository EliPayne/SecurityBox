from tkinter import *

def btnClick(number):
    global operator
    operator=operator+str(number)
    text.set(operator)
    
def Enter(number):
    return number

def clear():
    text = 0

keypad=Tk()
keypad.title("keypad")
operator=""
text = StringVar()
display=Entry(keypad,font=('times new roman',30,'bold'),textvariable=text,justify='right',bg='black',fg='blue',bd=30).grid(columnspan=5)
btn1=Button(keypad,command= lambda:btnClick(1),padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='1').grid(row=1,column=0)
btn2=Button(keypad,command= lambda:btnClick(2),padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='2').grid(row=1,column=1)
btn3=Button(keypad,command= lambda:btnClick(3),padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='3').grid(row=1,column=2)
btn4=Button(keypad,command= lambda:btnClick(4),padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='4').grid(row=2,column=0)
btn5=Button(keypad,command= lambda:btnClick(5),padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='5').grid(row=2,column=1)
btn6=Button(keypad,command= lambda:btnClick(6),padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='6').grid(row=2,column=2)
btn7=Button(keypad,command= lambda:btnClick(7),padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='7').grid(row=3,column=0)
btn8=Button(keypad,command= lambda:btnClick(8),padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='8').grid(row=3,column=1)
btn9=Button(keypad,command= lambda:btnClick(9),padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='9').grid(row=3,column=2)
btnC=Button(keypad,command= lambda:clear,padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='clear').grid(row=4,column=0)
btnE=Button(keypad,command= lambda:Enter(operator),padx=16,pady=16,fg='blue',font=('times new roman',30,'bold'),text='enter').grid(row=4,column=2)
keypad.mainloop()

