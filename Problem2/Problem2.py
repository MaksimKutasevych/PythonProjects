import psutil
import os
import time
import json

def get_size(file):
    file.seek(0,2) # move the cursor to the end of the file
    size = file.tell()
    return size
  
  
try:
    #Clearing existing file and creating new if we need to
    with open("monitoring.txt", "w") as myfile:
        myfile.write("{'Measuring':[")
        myfile.close()
            
    while True:
        
        #Measuring statistics
        percent = psutil.cpu_percent()
        virtualmem = psutil.virtual_memory()[3]
        print(f'The CPU usage is {percent}%')
        print('RAM memory bytes used:',virtualmem )
        
        #Making json dump
        data = {'time':time.time(),'cpu' : percent,'memory' : virtualmem}
        
        #Writing data in file
        with open("monitoring.txt", "a") as myfile:
            json.dump(data, myfile)
            myfile.write(',')
            myfile.close()
        time.sleep(2)
        
finally:
    with open("monitoring.txt", "a") as myfile:
        fsize = get_size(myfile)
        myfile.truncate(fsize - 1)
        myfile.write("]}")
        myfile.close()
    
        
