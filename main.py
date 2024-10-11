import tkinter as tk
from tkinter import PhotoImage

root= tk.Tk()
root.title("Image")
image= PhotoImage("aeroplane.jpeg")
label= tk.Label(root, image=image)

label.pack()
root.mainloop()