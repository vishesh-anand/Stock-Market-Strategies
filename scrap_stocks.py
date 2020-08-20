#!/usr/bin/env python
import sys
import time
import random
import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup

filename='real time stock data.csv'


def get_openclosedata(stock_code):
	url=('https://in.finance.yahoo.com/quote/'+stock_code + '?p=' + stock_code + '&.tsrc=fin-tre-srch')
	response = requests.get(url)
	web_content = BeautifulSoup(response.text,'lxml')
	web_content = web_content.find('td',{'class' : 'Ta(end) Fw(600) Lh(14px)'})
	open_price = web_content.find('span').text
	return open_price

def real_time_price(stock_code):
	url=('https://in.finance.yahoo.com/quote/'+stock_code + '?p=' + stock_code + '&.tsrc=fin-tre-srch')
	# response = requests.get(url)
	response = ''
	while response=='':
		try:
			response = requests.get(url)
			break
		except:
			print("Connection refused by server...")
			print("Let me sleep for 3 seconds")
			time.sleep(3)
			continue

	web_content = BeautifulSoup(response.text,'lxml')
	web_content = web_content.find('div',{'class' : 'My(6px) Pos(r) smartphone_Mt(6px)'})
	web_content = web_content.find('span').text

	if web_content==[]:
		web_content='99999'
	web_content=web_content.replace(',','')

	return float(web_content)

# HSI=['RELIANCE.NS']
# today = datetime.date.today()
# frame=[]
# openp=[]
# frame=[today]
# for stock_code in HSI:
# 	openp.append(get_openclosedata(stock_code))
# frame.extend(openp)
# DF=pd.DataFrame(frame)
# DF=DF.T
# DF.to_csv('opening price data.csv',mode= 'a', header=False)
	


# # f=open(filename,"w+")
# # f.close()
# DF=pd.read_csv(filename,index_col=0)

# if DF.empty:
# 	d={'DateTime':[],'RELIANCE.NS':[]}
# else:
# 	d=DF.to_dict('list')

# # d={'DateTime':[],'RELIANCE.NS':[]}
# while True:
# 	for stock_code in HSI:
# 		d['RELIANCE.NS'].append(real_time_price(stock_code))

# 	temp_local_datetime=datetime.datetime.now()
# 	local_datetime=temp_local_datetime.strftime("%Y-%m-%d %H:%M:%S")
# 	d['DateTime'].append(local_datetime)
	
# 	df=pd.DataFrame(data=d)
# 	df.to_csv(filename,columns=['DateTime','RELIANCE.NS'], mode= 'w', header=True)
# 	print(df)
# 	time.sleep(19)

