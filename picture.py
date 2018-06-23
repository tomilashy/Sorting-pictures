'''
Created on Jun 11, 2018

@author: Jesutomi
'''


import time
import pathlib
import glob
import os
import shutil
from csv import reader, writer,DictWriter
    


files = glob.glob("*.jpg")
files2 = glob.glob("*.png")
files.extend(files2)
files.sort(key=os.path.getmtime)
#print("\n".join(files))
#printing out files in sorted form
for  x in files:
    times=os.path.getmtime(x)
    real=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(times))
    print(f"{x}\t\t\t{real}")

num=0
with open("Picture file.csv", "w") as file:
    headers = ["S/N","Name", "Time", "New folder"]
    csv_writer = DictWriter(file, fieldnames=headers,delimiter="|")
    csv_writer.writeheader()
    for  x in files:
        times=os.path.getmtime(x)
        folder=str(time.strftime("%B",time.localtime(times))) +" "+ str(time.strftime("%Y",time.localtime(times)))
        #print(folder) 
        
        num+=1
        if num:
          
            csv_writer.writerow({
                "S/N":f"{num}",
                "Name": f"{x}",
                "Time": f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(times))}",
                "New folder": f"{folder}"
            })
            
        if  os.path.exists(folder):
            pass
        else:
            pathlib.Path(folder).mkdir()
        shutil.move(x,folder)
    

