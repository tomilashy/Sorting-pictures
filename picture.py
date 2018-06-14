import os
import exifread
import pathlib
import shutil



path = os.getcwd()

print(path)

TTags = [('DateTimeOriginal', 'DateTime')]
for file in os.listdir(path):
   if file.endswith('.jpg'):
       pic = open(file,'rb')
       tags = exifread.process_file(pic)
       for tag in tags.keys():
           if tag == 'EXIF DateTimeOriginal':
               print(tags[tag])
               date = str(tags[tag])[0:4]
               if os.path.exists(date):
                   print('Folder already exists!')
               else:
                   pathlib.Path(date).mkdir()
               shutil.move(file,date)
