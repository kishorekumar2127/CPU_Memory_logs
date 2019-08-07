#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Kishore - 01/08/2019

# libraries included
import psutil
import time
import sys

# Creating log file for statistics and capturing standard output
old_stdout = sys.stdout
log_file = open("CPU_Memory.log","w")
sys.stdout = log_file

# Main code
try:
    while True:
    
        # Current time stamp
        print (time.ctime())

        # For CPU utilization
        print('CPU Utilization:', psutil.cpu_percent(),'%')

        # For Memory Utilization 
        print('Memory Stats:', dict(psutil.virtual_memory()._asdict()))

        # Sleep for next one sec 
        time.sleep(1)
       
except (KeyboardInterrupt, SystemExit):
    
    # Final message
    print('program interrupted!')
    
    # Writing the data to file and closing it
    sys.stdout = old_stdout
    log_file.close()

