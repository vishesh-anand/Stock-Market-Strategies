#!/usr/bin/env python3
import sys
import time
import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup
from scrap_stocks import real_time_price
from interpolate import interpolate_data
import webbrowser
from popup_notification import send_notification_alert

SPIKE_HEIGHT=3

filename1='real time stock data.csv'
filename2='interpolated_data.csv'
HSI=['SBIN.NS','TTM','TATASTEEL.NS','WOCKPHARMA.NS','AXISBANK.NS','INFY','ADANIENT.NS','BANKBARODA.NS','DLF.NS','LT.NS','LICHSGFIN.NS','HINDALCO.NS','ICICIBANK.NS','PVR.NS','ASHOKLEY.NS','BHARTIARTL.NS','MARUTI.NS']

def get_past_data(local_datetime,MINUTES=10):

	interpolated_data=pd.read_csv(filename2,index_col=0)

	time_diff=datetime.timedelta(minutes=MINUTES)
	five_minutes_beforetime=local_datetime - time_diff
	now=local_datetime.strftime('%Y-%m-%d %H:%M:%S')
	before=five_minutes_beforetime.strftime('%Y-%m-%d %H:%M:%S')

	conc_data=interpolated_data[before:now]
	return conc_data

def calc_percentage_change(df,local_datetime):

	minimum_data=df.min()
	maximum_data=df.max()

	now=local_datetime.strftime('%Y-%m-%d %H:%M:%S')
	now_data=df.loc[now]

	pchange={}
	percentage_increment=((now_data-minimum_data)/minimum_data)*100
	percentage_decrement=((now_data-maximum_data)/maximum_data)*100

	pchange['Increment']=percentage_increment
	pchange['Decrement']=percentage_decrement

	return pchange

def generate_message(spiked_up_stocks,up_or_down):
	message=''
	size=spiked_up_stocks.shape[0]
	for i in range(size):
		message = message + spiked_up_stocks.index[i] + 'has spurted' + up_or_down + 'by' + str(spiked_up_stocks.values[i]) + '\n'
	return message

# f=open(filename1,"w+")
# f.close()
try:
	DF=pd.read_csv(filename1,index_col=0)
	d=DF.to_dict('list')
except:
	d={'DateTime':[]}
	for stock_code in HSI:
		d[stock_code]=[]

while True:
	for stock_code in HSI:
		d[stock_code].append(real_time_price(stock_code))
	
	temp_local_datetime=datetime.datetime.now()
	local_datetime=temp_local_datetime.strftime("%Y-%m-%d %H:%M:%S")
	d['DateTime'].append(local_datetime)
	print("PARSING DATA at "+local_datetime)
	df=pd.DataFrame(data=d)
	df.to_csv(filename1, mode= 'w', header=True)

	interpolate_data(filename1,filename2)
	df1=get_past_data(temp_local_datetime,MINUTES=10)
	pchange=calc_percentage_change(df1,temp_local_datetime)
	# print(percentage_change)
	su_condition=pchange['Increment']>SPIKE_HEIGHT
	sd_condition=pchange['Decrement']<(-SPIKE_HEIGHT)

	spiked_up_stocks=(pchange['Increment'])[su_condition]
	spiked_down_stocks=(pchange['Decrement'])[sd_condition]

	if not(spiked_up_stocks.empty):
		print("Spiked up stocks - ")
		print(spiked_up_stocks)
		send_notification_alert("Spike detected!!", generate_message(spiked_up_stocks,"up"))
	if not(spiked_down_stocks.empty):
		print("Spiked down stocks - ")
		print(spiked_down_stocks)
		send_notification_alert("Spike detected!!", generate_message(spiked_down_stocks,"down"))

	time.sleep(3)