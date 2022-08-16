# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/integra-dos/Descargas/bryan/pm1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!


# --- Requeriments ----
# pyqt5
# pyqt5-tools

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import datetime
from urllib.request import urlopen
import random
import requests


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget


from PyQt5.QtCore import QEvent
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
import sys


# ----------------------------------------------------------------
# ----------------------------------------------------------------
# --------- -------------------------------------------------------
global item

class Main_Window(QMainWindow):
    def __init__(self, MainWindow):
        super().__init__()
        
        MainWindow = MainWindow

        self.dic_personajes = {}

        self.setupUi()

    def setupUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 600)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lhora = QLabel(self.centralwidget)
        self.lhora.setGeometry(QRect(510, 230, 97, 17)) #(posx, posy, w, h)
        font = QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lhora.setFont(font)
        self.lhora.setLineWidth(1)
        self.lhora.setScaledContents(False)
        self.lhora.setObjectName("lhora")

        self.lfecha = QLabel(self.centralwidget)
        self.lfecha.setGeometry(QRect(510, 90, 130, 17)) #(posx, posy, w, h)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lfecha.setFont(font)
        self.lfecha.setObjectName("lfecha")

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(460, 370, 181, 71)) #(posx, posy, w, h)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        icon = QIcon()
        icon.addPixmap(QPixmap("tecni.ico"), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(self.solicitudes)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 885, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QRect(50, 50, 300, 500))
        self.listWidget.setObjectName("listWidget")
        #self.listWidget.installitem_clicked(self)
        self.listWidget.itemClicked.connect(self.item_clicked)



        #self.listWidget = QtWidgets.QPushButton(self)
        self.listWidget.installEventFilter(self)
        self.listWidget.itemClicked.connect(self.eventFilter)




        self.retranslateUi()
        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " Postulante para ROBOTILSA S.A"))
        self.lhora.setText(_translate("MainWindow", 'Hora'))
        self.lfecha.setText(_translate("MainWindow", 'Fecha'))
        self.pushButton.setText(_translate("MainWindow", "REQUEST"))


    def item_clicked(self, item):
#        if event.type() == QEvent.ContextMenu and source is self.listWidget:
    	#QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())
        dialog = QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog,item.text(),self.dic_personajes)
        dialog.exec_()
        dialog.show()
        return item


    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.listWidget:
            menu = QMenu()

            action1 = menu.addAction("Informacion del personaje")

            selected_action = menu.exec_(event.globalPos())

            if selected_action == action1:

                dialog = QDialog()
                dialog.ui = Ui_Dialog()
                dialog.ui.setupUi(dialog,item.text(),self.dic_personajes)
                dialog.exec_()
                dialog.show()
        return super().eventFilter(source, event)





    def displayTime(self):        
        now   = datetime.datetime.now()
        fecha = now.strftime('%d/%m/%Y')
        hora  = now.strftime('%H:%M:%S')
        self.lhora.setText(hora)
        self.lfecha.setText(fecha)


    def bucle(self):
        timer = QTimer(self)     
        timer.timeout.connect(self.displayTime)
        timer.start(10)     


    def solicitudes(self):

    	self.listWidget.clear()

    	url = 'https://swapi.dev/api/people/' 
    	self.dic_personajes = {}

    	cont = 0
    	randomicos = []

    	while cont < 10:
    		item = random.randrange(40)
    		if item not in randomicos: 
    			randomicos.append(item)
    			cont += 1

    	for i in randomicos:
    		try:
	    		res = requests.get(url+str(i))
	    		self.dic_personajes[res.json()['name']] = res.json()
	    		#print(res.json()['name'])   
	    		self.listWidget.addItem(res.json()['name']) # Add the value we got to the list
	    	except:
	    		print('ERROR: ',url+str(i))






# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
class Ui_Dialog(object):
    def setupUi(self, Dialog, item, dic_personajes):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 500)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # ---- KEYS

        self.lkey1 = QLabel(Dialog)
        self.lkey2 = QLabel(Dialog)
        self.lkey3 = QLabel(Dialog)
        self.lkey4 = QLabel(Dialog)
        self.lkey5 = QLabel(Dialog)
        self.lkey6 = QLabel(Dialog)
        self.lkey7 = QLabel(Dialog)


        font = QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(55)

        self.lkey1.setFont(font)
        self.lkey2.setFont(font)
        self.lkey3.setFont(font)
        self.lkey4.setFont(font)
        self.lkey5.setFont(font)
        self.lkey6.setFont(font)
        self.lkey7.setFont(font)
       

        keys = [self.lkey1, self.lkey2, self.lkey3, self.lkey4, self.lkey5,
        		self.lkey6, self.lkey7]

		# ---- VALUES

        self.lvalue1 = QLabel(Dialog)
        self.lvalue2 = QLabel(Dialog)
        self.lvalue3 = QLabel(Dialog)
        self.lvalue4 = QLabel(Dialog)
        self.lvalue5 = QLabel(Dialog)
        self.lvalue6 = QLabel(Dialog)
        self.lvalue7 = QLabel(Dialog)

                        
        font = QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(35)

        self.lvalue1.setFont(font)
        self.lvalue2.setFont(font)
        self.lvalue3.setFont(font)  
        self.lvalue4.setFont(font)
        self.lvalue5.setFont(font)
        self.lvalue6.setFont(font)
        self.lvalue7.setFont(font)


        values = [self.lvalue1, self.lvalue2, self.lvalue3, self.lvalue4, self.lvalue5,
					self.lvalue6, self.lvalue7]


		# -------------------------------------------------------

        dic_keys   = list(dic_personajes[item].keys())
        dic_values = list(dic_personajes[item].values())  

        for j, k in enumerate(keys): 

	        k.setGeometry(QRect(60, 50+(50*j), 120, 20)) #(posx, posy, w, h)
	        k.setText(dic_keys[j])        
	        values[j].setGeometry(QRect(200, 50+(50*j), 170, 25)) #(posx, posy, w, h)
	        values[j].setText(dic_values[j]) 

        #print(dic_personajes[item])


        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ventana Secundaria"))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui_1 = Main_Window(MainWindow)    
    ui_1.bucle()    
    MainWindow.show()
    sys.exit(app.exec_())


