'''
Created on Jun 11, 2018

@author: Jesutomi
'''


import time
import pathlib
import glob
import os
import shutil


files = glob.glob("*.jpg")
files.sort(key=os.path.getctime)
#print("\n".join(files))
#printing out files in sorted form
for  x in files:
    times=os.path.getctime(x)
    real=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(times))
    print(f"{x}\t\t\t{real}")

for  x in files:
    times=os.path.getmtime(x)
    folder=str(time.strftime("%B",time.localtime(times))) +" "+ str(time.strftime("%Y",time.localtime(times)))
    #print(folder)

    if  os.path.exists(folder):
        pass
    else:
        pathlib.Path(folder).mkdir()
    shutil.move(x,folder)
