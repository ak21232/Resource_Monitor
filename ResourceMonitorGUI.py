
import os.path
import ResourceMonitor
import tkinter as tk
from tkinter import PhotoImage

import os.path

def launch_ResourceMonitor():
    os.system('ResourceMonitor.py')

def launch_ResourceMonitorAppend():
	os.system('ResourceMonitor_Append.py')

#def launch_ResourceMonitorMaintenance(): 
	#os.system('ResourceMonitor_Maintenance')
	
root = tk.Tk()
root.geometry("500x300")
root.title('Atmos Resource Monitor')

#Images
csv_image = PhotoImage(file="Images\icon_file-CSV_plano-512.png")

#Lauch Resource Monitor
button_launchmonitor = tk.Button(root, text="Launch CSV", image=csv_image, command=launch_ResourceMonitor)
button_launchmonitor.config(height = 70, width = 70)
button_launchmonitor.grid(row =0, column =1)

#Launch Resource Monitor Append
button_launchappend = tk.Button(root, text="Launch Append", image=csv_image, command=launch_ResourceMonitorAppend)
button_launchappend.config(height = 70, width = 70)
button_launchappend.grid(row =0, column =100)

#Overwrite file for Maintenance
button_maintenance = tk.Button(root, text="Perform Maintenance", image=csv_image, command=launch_ResourceMonitorAppend)
button_maintenance.config(height = 70, width = 70)
button_maintenance.grid(row =0, column =200)



root.mainloop()
