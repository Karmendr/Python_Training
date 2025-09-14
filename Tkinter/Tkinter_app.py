import tkinter as tk

root = tk.Tk()
root.title("My First Tikinter App")
root.geometry("400x200")

def on_button_click():
  label.config(text="Hello, Tkinter!")

label = tk.Label(root,text="Welcome to Tkinter")
label.pack(pady=20)

button = tk.Button(root,text="Click Me",command=on_button_click)
button.pack()

root.mainloop()