import tkinter as tk
from PIL import Image, ImageTk

raj = tk.Tk()
raj.geometry("125x944")

image = Image.open("img.jpg")
photo = ImageTk.PhotoImage(image)

raj_label = tk.Label()
raj_label.pack()

raj.mainloop()
