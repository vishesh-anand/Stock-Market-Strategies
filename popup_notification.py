#!/usr/bin/env python
import webbrowser
from tkinter import *
from tkinter import messagebox, ttk



def open_webpage():
	webbrowser.open('http://www.icicidirect.com', new=2)

def call_me():
	messagebox.showinfo("Success", "Installation completed")

root= Tk()
root.title("Spike Detected!")

style=ttk.Style()
style.configure("TButton", foreground="white", background="blue")

b=ttk.Button(root, text="Click here to redirect to ICICIDirect", command=open_webpage)
b.pack()

root.geometry('400x400')
root.mainloop()
# import notify2

# notify2.init('Alert')

# n=notify2.Notification(summary="Time to take rest", message="Relax your eyes now")
# n.show()