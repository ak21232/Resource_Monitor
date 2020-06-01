#Created by Abraar Khan
#This script creates a csv that will collect resource data

import psutil
import os.path
import csv
import datetime
import threading 


#Timestamp
currentDT = datetime.datetime.now()
timestamp = currentDT.strftime("%Y-%m-%d %H:%M:%S")



#Gather the various parameters and convert from Byte to Megabyte
total_memory= (psutil.virtual_memory().total/(10**6))
available_memory = (psutil.virtual_memory().available/(10**6))
percent_memory_used = (psutil.virtual_memory().percent)
used_disk_space = (psutil.virtual_memory().used/(10**6))
free_disk_space = (psutil.virtual_memory().free/(10**6))

#Combine the parameters into a row
resources = [timestamp,total_memory, available_memory, percent_memory_used, used_disk_space, free_disk_space]


         
#Write the header columns
with open('C:\Python37/ResourcesUsed.csv', mode='w+') as f:
	resource_writer = csv.writer(f, delimiter = ',')
	resource_reader = csv.reader(f, delimiter = ',')
	resource_writer.writerow(['TimeStamp', 'Total Memory (MB)', 'Available Memory (MB)', 'Percent Memory Used (MB)', 'Used Disk Space (MB)', 'Free Disk Space (MB)'])

