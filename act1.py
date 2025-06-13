from tkinter import *
window=Tk()
window.title("demo project")
window.geometry("500x500")
def keypress(event):
    print(event.char)
window.bind("<Key>", keypress )
button=Button(window, text="Click Me", )
button.pack()
def click(event):
     print("button has been clicked")
button.bind("<Button-1>", click)

window.mainloop()