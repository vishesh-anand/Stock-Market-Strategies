#!/usr/bin/env python3

from tkinter import *

def show(event):
	myLabel=Label(root, text=variable.get()).pack()
	
root = Tk()
root.title("Stock Market Strategies")
root.iconbitmap('/Users/anandgupta/Desktop/Stock_Market/stocks.png')
root.geometry('800x800')

label1=Label(root,text="Enter the stocks you want to track")
label1.grid(row=0,column=0)

stocks_names=['SBIN.NS','TTM','TATASTEEL.NS','WOCKPHARMA.NS','AXISBANK.NS','INFY','ADANIENT.NS','BANKBARODA.NS','DLF.NS','LT.NS','LICHSGFIN.NS','HINDALCO.NS','ICICIBANK.NS','PVR.NS','ASHOKLEY.NS','BHARTIARTL.NS','MARUTI.NS']

variable=StringVar(root)
variable.set(stocks_names[0])

drop=OptionMenu(root,variable, *stocks_names)
drop.pack(pady=20)

root.mainloop()
