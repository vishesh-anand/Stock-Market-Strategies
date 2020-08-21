#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
# ax2=fig.add_subplot(2,2,2)
# ax3=fig.add_subplot(2,2,3)
# ax4=fig.add_subplot(2,2,4)
df=pd.read_csv('real time stock data.csv')
x_lowerlim=0
x_upperlim=60

def animate(i):
	df=pd.read_csv('real time stock data.csv')
	ys=df.iloc[1:, 3].values
	xs=[x for x in range(1, len(ys)+1)]
	ax1.clear()
	if len(ys)>=60:
		ax1.set_xlim([x_lowerlim+(len(ys)-60),len(ys)+5])
	else:
		ax1.set_xlim([x_lowerlim,x_upperlim])
	ax1.plot(xs,ys)
	ax1.set_title('RELIANCE INDUSTRIES', fontsize=12)

	# ys=df.iloc[1:, 3].values
	# ax2.clear()
	# ax2.plot(xs,ys)
	# ax2.set_title('INFOSYS', fontsize=12)

	# ys=df.iloc[1:, 4].values
	# ax3.clear()
	# ax3.plot(xs,ys)
	# ax3.set_title('ALPHABET Inc.', fontsize=12)

	# ys=df.iloc[1:, 5].values
	# ax4.clear()
	# ax4.plot(xs,ys)
	# ax4.set_title('TESLA', fontsize=12)



ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.tight_layout()
plt.show()



