import wmi

# Initializing the wmi constructor
f = wmi.WMI()

# Printing the header for the later columns...
print("pid   Process name")

# Iterating through all the running processes...
for processes in f.Win32_Process():

	# displaying the P_ID and P_Name of the process...
	print(f"{processes.ProcessId:<10} {processes.ProcessName}")
