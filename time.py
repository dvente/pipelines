#!/usr/bin/env python
import sys
import pandas
import time
import numpy as np
import matplotlib.pyplot as plt

stamp = {}
for line in sys.stdin:
	input = line.split(' ')
	input[-1] = input[-1].rstrip() 
	if(input[-1] != "-"):# clear input of junk
		d = time.strptime(input[0], "%d/%b/%Y:%H:%M:%S")#get datetime object from string
		if(d.tm_yday in stamp):
			if(d.tm_hour in stamp[d.tm_yday]):# check if an entry exits if so append bytes
				stamp[d.tm_yday][d.tm_hour].append(int(input[-1]))
			else:
				stamp[d.tm_yday][d.tm_hour] = [int(input[-1])] # hour entry doesn't exist to create it
		else:
			stamp[d.tm_yday] = {}# new day entry so create the dicts for it
			stamp[d.tm_yday][d.tm_hour] = [int(input[-1])] #append bytes
			

for i in stamp:#data is now known so calculate average
	for j in stamp[i]:
		stamp[i][j] = sum(stamp[i][j])/len(stamp[i][j])
	plt.clf() #plot the data
	keys = map(int, stamp[i].keys())
	plt.plot(keys, stamp[i].values(), "-o")
	plt.xlabel('Hour')
	plt.ylabel('Average number of bytes transmited')
	plt.title("day " +str(i))
	plt.grid(True,  linewidth=1)
	plt.savefig("day" +str(i)+".pdf")