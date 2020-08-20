import sys
import time
import random
import requests
import datetime
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

def real_time_price(stock_code):
	url=('https://finance.yahoo.com/quote/'+stock_code + '?p=' + stock_code + '&.tsrc=fin-srch')

	response= requests.get(url)
	web_content = BeautifulSoup(response.text,'lxml')
	web_content = web_content.find('div',{'class' : 'My(6px) Pos(r) smartphone_Mt(6px)'})
	web_content = web_content.find('span').text

	if web_content==[]:
		web_content='99999'

	return web_content


style.use('fivethirtyeight')
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

def animate(i):
	df=pd.read_csv('real time stock data.csv')
	ys=df.iloc[1:, 2].values
	xs=[x for x in range(1, len(ys)+1)]
	ax1.clear()
	ax1.plot(xs,ys)
	ax1.set_title('RELIANCE INDUSTRIES', fontsize=12)



ani = animation.FuncAnimation(fig, animate, interval = 1000)

plt.tight_layout()
plt.show()