#!/usr/bin/env python3
#import webbrowser
#from tkinter import *
#from tkinter import messagebox, ttk
from playsound import playsound
import os
import platform

def send_notification_alert(TITLE,SUBTITLE):

	if platform.system()=='Darwin':
		from pync import Notifier
	
		Notifier.notify(message='Click here to trade now', 
					title=TITLE, 
					subtitle= SUBTITLE, 
					open='http://www.icicidirect.com',
					sound='default'
					)					
		playsound('/Users/anandgupta/Desktop/Stock_Market/swiftly.mp3')

	elif platform.system()=='Windows':
		from plyer import notification

		notification.notify(
							title=TITLE,
							message = SUBTITLE + '\nClick here to trade now!!',
							timeout=10
							)
		playsound('/Users/anandgupta/Desktop/Stock_Market/swiftly.mp3')

	else:
		print("Platform not supported")

# def open_webpage():
# 	webbrowser.open('http://www.icicidirect.com', new=2)

# def call_me():
# 	messagebox.showinfo("Success", "Installation completed")

# root= Tk()
# root.title("Spike Detected!")

# style=ttk.Style()
# style.configure("TButton", foreground="white", background="blue")

# b=ttk.Button(root, text="Click here to redirect to ICICIDirect", command=open_webpage)
# b.pack()

# playsound('/Users/anandgupta/Desktop/Stock_Market/swiftly.mp3')

# root.geometry('400x400')
# root.mainloop()