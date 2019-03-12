from PIL import ImageTk, Image
import Tkinter as tk
import cv2
HEIGHT = 600
WIDTH = 600
root = tk.Tk()

def load_image(entry):
	original_img.paste(Image.open(entry))
		
root.title("XXX  PEACE KEEPER  XXX")

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()  

bg = Image.open("camo.jpg")
background_image = ImageTk.PhotoImage(bg)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

top_frame = tk.Frame(root,bg="#071F2D",bd=5)
top_frame.place(relx=0.5,rely=0.03,relwidth=0.9,relheight=0.1,anchor='n')

entry = tk.Entry(top_frame,font=("Courier", 20))
entry.place(relwidth=0.65,relheight=1)

load = tk.Button(top_frame,font=("Courier", 20),text=" LOAD ",bg="#394344",command=lambda:load_image(entry.get()))
load.place(relx=0.68,relwidth=0.32,relheight=1)

img_frame = tk.Frame(root,bg="#071F2D",bd=5)
img_frame.place(relx=0.5,rely=0.15,relwidth=0.9,relheight=0.6,anchor='n')

og = Image.open("camo.jpg")
original_img = ImageTk.PhotoImage(og)
orig_label = tk.Label(img_frame,image=original_img)
orig_label.place(relwidth=0.5,relheight=1)

pro = Image.open("camo.jpg")
pro_img = ImageTk.PhotoImage(pro)
pro_label = tk.Label(img_frame,image=pro_img,bg="red")
pro_label.place(relx=0.52,relwidth=0.48,relheight=1)

label1 = tk.Label(root,bg="#54625B",fg="white",text="Original",font=("Courier", 20))
label1.place(relx=0.05,rely=0.75,relwidth=0.45,relheight=0.05)

label2 = tk.Label(root,bg="#54625B",fg="white",text="Processed",font=("Courier", 20))
label2.place(relx=0.52,rely=0.75,relwidth=0.43,relheight=0.05)

result = tk.Label(root,text="Not Found",font=("Courier", 20),bg="#091823",fg="white")
result.place(relx=0.5,rely=0.85	,relwidth=0.5,relheight=0.05,anchor='n')

root.mainloop()