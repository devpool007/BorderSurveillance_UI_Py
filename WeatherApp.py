#!/usr/bin/python3
import tkinter as tk
#from tkinter import ttk
HEIGHT = 800
WIDTH = 800
root = tk.Tk()
root.title("XXX  PEACE KEEPER  XXX")
photo = tk.PhotoImage(file="camo.PPM")

l = tk.Label(root, image=photo)
l.pack()

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()


frame = tk.Frame(root,bg="#7B857B")
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

button = tk.Button(frame, text = "  ON  ", bg="red", fg="green")#highlightbackground="#7B857B")
button.grid()

label = tk.Label(frame,text="This is Label",bg="yellow")
label.grid()

entry = tk.Entry(frame,bg="green")
entry.grid()

root.mainloop()
