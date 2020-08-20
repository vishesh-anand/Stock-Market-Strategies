#!/usr/bin/env python

import time
from plyer import notification

if __name__=="__main__":
	while True:
		notification.notify(
			title="Please Drink Water",
			message = "An average adult should drink 2.6 l of water per day",
			
			)
		time.sleep(2)