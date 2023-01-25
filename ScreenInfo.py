import tkinter as tk

#User interface begins here
root = tk.Tk()

canvas = tk.Canvas(root, width = 720, height = 576)
canvas.grid(columnspan= 4,rowspan=4)

#defining function for action taking placed when the button(admin) is tapped
def adminWin():
    window = tk()
    canvas2 = tk.Canvas(root, width = 720, height = 576)
    canvas2.grid(columnspan= 4,rowspan=4)
    admin_text = tk.StringVar()
    admin_button = tk.Button(root,textvariable= admin_text, font= "Bold", foreground= "red", command= adminWin)
    admin_text.set("ADMIN")
    admin_button.grid(column=2, row =0)
    admin_button.config(height= 5, width=15) 


#Admin Button
admin_text = tk.StringVar()
admin_button = tk.Button(root,textvariable= admin_text, font= "Bold", foreground= "red", command= adminWin)
admin_text.set("ADMIN")
admin_button.grid(column=2, row =0)
admin_button.config(height= 5, width=15)


#defining function for action taking placed when the button(scan) is tapped
def ScanMess():
    print("Scanning button Clicked!")

#User Button
scan_text = tk.StringVar()
scan_button = tk.Button(root, textvariable= scan_text, font="Raleway", command= ScanMess)
scan_text.set("Scan")
scan_button.grid(column=0,row=1)
scan_button.config(height= 10, width=40)





#code after mainloop will not display
root.mainloop()
