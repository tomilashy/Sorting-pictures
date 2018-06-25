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
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    
    def __init__(self):
        self.directory=""
    def _open_file_dialog(self):
        self.directory=str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit.setText(f'{self.directory}')
        
        
    def _get_text(self):
        return self.directory
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setMinimumSize(406, 297)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 361, 73))
        self.layoutWidget.setObjectName("layoutWidget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self._open_file_dialog)
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Picture Sorter"))
        self.label.setText(_translate("Dialog", "Folder location"))
        self.pushButton.setText(_translate("Dialog", "Select folder Directory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
    

direct = ui._get_text()+r"/"

files = glob.glob(direct +"*.jpg")
files2 = glob.glob(direct +"*.png")
files.extend(files2)
files.sort(key=os.path.getmtime)
#print("\n".join(files))
#printing out files in sorted form
for  x in files:
    times=os.path.getmtime(x)
    real=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(times))
    print(f"{x}\t\t\t{real}")

num=0
with open(direct+"Picture file.csv", "w") as file:
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
            
        if  os.path.exists(direct+folder):
            pass
        else:
            pathlib.Path(direct+folder).mkdir()
        shutil.move(x,direct+folder)
    

