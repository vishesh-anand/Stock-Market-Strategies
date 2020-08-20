#!/usr/bin/env python

import pandas as pd
import requests
import datetime
import time
from bs4 import BeautifulSoup

def interpolate_data(filename1,filename2):
	df0=pd.read_csv(filename1,parse_dates=True,infer_datetime_format='%Y-%m-%d %H:%M:%S',index_col=1)
	df =df0.copy()
	df=df.drop('Unnamed: 0',axis=1)
	upsampled=df.resample('S')
	interpolated_data = upsampled.interpolate(method='linear')
	interpolated_data.to_csv(filename2,mode='w')
	return interpolate_data

