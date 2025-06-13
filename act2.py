from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("demo project")
window.geometry("500x500")
def show():
           messagebox.showerror("error message", "Virus found!!!")

button=Button(window, text="Scan for viruses", command=show)
button.pack()
window.mainloop()
    
