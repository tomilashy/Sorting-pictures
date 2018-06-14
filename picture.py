'''
Created on Jun 11, 2018

@author: Jesutomi
'''


import time
import pathlib
import glob
import os
import  datetime


files = glob.glob("*.jpg")
files.sort(key=os.path.getctime)
print("\n".join(files))

times=os.path.getmtime("AlertImage_ContactLow.jpg")


real=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(times))

folder=str(time.strftime("%B",time.localtime(times))) +" "+ str(time.strftime("%Y",time.localtime(times)))
print(folder)


pathlib.Path(folder).mkdir()
os.path.exists(folder)
