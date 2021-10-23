import tkinter as tk
import json
import random


window = tk.Tk()
# window2 = tk.Toplevel()
window.title('JapanLesson')
window.geometry('600x400+500+200')
window.minsize(width=300, height=200)
window.config(background='skyblue')
def o():
    tl = tk.Toplevel()
    tl.title('123')
    tl.geometry('600x400')
    tl.minsize(width=300, height=200)
    tl.config(background='skyblue')
def o2():
    tl = tk.Toplevel()
    tl.title('6666666')
    tl.geometry('300x400')
    tl.minsize(width=300, height=200)
    tl.config(background='skyblue')
    
tk.Button(window,command=o ).pack()

tk.Button(window,command=o2 ).pack()

window.mainloop()