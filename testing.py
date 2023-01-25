from tkinter import*

root =Tk()
root.minsize(height = 500, width = 900)
def tab1():
    def tab2():
        label1.destroy()
        button1.destroy()
        label2 = Label(root, text = "testing 2", font=('Times_New_Roman',25))
        label2.pack()
        button2 = Button(root, text = 'Back',font=('Times_New_Roman',25 ), command= tab1)
        button2.pack(side = CENTER)
    label1 = Label(root, text = "testing 1", font=('Times_New_Roman',25))
    label1.pack()
    button1 = Button(root, text = 'next',font=('Times_New_Roman',25 ), command =tab2)
    button1.pack(side = CENTER)
    root.mainloop()
