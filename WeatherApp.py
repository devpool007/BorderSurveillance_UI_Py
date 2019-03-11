#!/usr/bin/python3
import tkinter as tk
#from tkinter import ttk
HEIGHT = 800
WIDTH = 800
root = tk.Tk()
root.title("XXX  PEACE KEEPER  XXX")
#photo = tk.PhotoImage(file="camo.PPM")

# l = tk.Label(root, image=photo)
# l.pack()
# label = tk.Label(frame,text="This is Label",bg="yellow")
# label.place(relx=0.3,rely=0,relwidth=0.45,relheight=0.25)

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

frame = tk.Frame(root,bg="#80c1ff")
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor="n")

entry = tk.Entry(frame ,font=40)
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame, text = "  ON  ", bg="red", fg="green",highlightbackground="#80c1ff",font=40)
button.place(relx=0.7,relwidth=0.35,relheight=1)


root.mainloop()
