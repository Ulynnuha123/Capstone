# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hahaha.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import pandas as pd
import numpy as np
import pyqtgraph as pg
import time
import sys
from PyQt5.QtGui import QPixmap
from random import random

from PyQt5 import QtCore, QtGui, QtWidgets

pg.setConfigOption('background','w')
pg.setConfigOption('foreground','r')

sensor = pd.read_excel("C:\\Users\\BLACK\\Desktop\\numpy.xlsx")

class PlotThread(QtCore.QThread):

    update_range1 = QtCore.pyqtSignal(float, float)
    update_range2 = QtCore.pyqtSignal(float, float)
    update_range3 = QtCore.pyqtSignal(float, float)

    update_yval1 = QtCore.pyqtSignal(list, list)
    update_yval2 = QtCore.pyqtSignal(list, list)
    update_yval3 = QtCore.pyqtSignal(list,list)

    update_text1 = QtCore.pyqtSignal(str)
    update_text2 = QtCore.pyqtSignal(str)
    update_text3 = QtCore.pyqtSignal(str)

    update_stat = QtCore.pyqtSignal(str)
    update_stat1 = QtCore.pyqtSignal(bool)
    update_stat2 = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent=parent)
        self.isRunning = True        

    def run(self):
        self.sensor = pd.read_excel("C:\\Users\\BLACK\\Desktop\\numpy.xlsx")
        self.xval = self.sensor['time'].tolist()
        self.yval1 = self.sensor['arus'].tolist()
        self.yval2 = self.sensor['kecepatan'].tolist()
        self.yval3 = self.sensor['posisi'].tolist()
        self.yval4 = self.sensor['stat2'].tolist()
        
        window_size=50
        idx=0

        while self.isRunning and (idx + window_size) < len(self.xval):

            self.update_range1.emit(self.xval[idx],self.xval[idx+window_size])
            self.update_yval1.emit(self.xval[idx:idx+window_size], self.yval1[idx:idx+window_size])
            self.update_text1.emit(str(round(self.yval1[idx+window_size],4)))
            
            # self.update_stat.emit(str(self.yval4[idx+window_size]))
            if str(self.yval4[idx+window_size]) == "True" :
                self.update_stat1.emit(bool(True))
            else :
                self.update_stat2.emit(bool(True))
                        
            self.update_range2.emit(self.xval[idx],self.xval[idx+window_size])
            self.update_yval2.emit(self.xval[idx:idx+window_size], self.yval2[idx:idx+window_size])
            self.update_text2.emit(str(round(self.yval2[idx+window_size],4)))
            
            self.update_range3.emit(self.xval[idx],self.xval[idx+window_size])
            self.update_yval3.emit(self.xval[idx:idx+window_size], self.yval3[idx:idx+window_size])
            self.update_text3.emit(str(round(self.yval3[idx+window_size],4)))

            idx += 1
            time.sleep(1)
    
    def stop(self):
        self.isRunning = False
        self.quit()
        self.wait()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Setup UI
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        MainWindow.setSizePolicy(sizePolicy)

        #Setup MainFrame
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        self.mainframe.setObjectName("mainframe")
    
        # setup layout mainframe as formLayout
        self.frameLayout = QtWidgets.QVBoxLayout(self.mainframe)
        self.frameLayout.setObjectName("frameLayout")

        #setup frame in the top
        self.Frametop = QtWidgets.QFrame(self.mainframe)
        self.Frametop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frametop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frametop.setObjectName("Frametop")

        #setup frame in the top as horizontal layout
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Frametop)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #setup Title Lable
        self.Title_Label = QtWidgets.QLabel(self.Frametop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title_Label.sizePolicy().hasHeightForWidth())
        self.Title_Label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(24)
        self.Title_Label.setFont(font)
        self.Title_Label.setObjectName("Title_Label")
        self.horizontalLayout_2.addWidget(self.Title_Label)

        #setup spacer between title and logo
        spacer_title_logo = QtWidgets.QSpacerItem(396, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_title_logo)

        #setup label logo UGM
        # self.label = QtWidgets.QLabel(self.Frametop)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        #self.label.setSizePolicy(sizePolicy)
        #self.label.setMinimumSize(QtCore.QSize(191, 20))
        #self.pict= QPixmap("Logo Horizontal Stack-Up.png")
        #self.label.setText("")
        #self.label.setPixmap(self.pict)
        #self.label.setObjectName("label")
        #self.horizontalLayout_2.addWidget(self.label)       

        #spacer in right size label
        spacer_rightlabel = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_rightlabel)

        #setup vertical layout in frame top
        self.frameLayout.addWidget(self.Frametop)

        #setup frame sensor 1
        self.frame_sensor1 = QtWidgets.QHBoxLayout()
        self.frame_sensor1.setObjectName("frame_sensor1")

        #setup frame plot sensor 1
        self.frame_plot1 = QtWidgets.QFrame(self.mainframe)
        self.frame_plot1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plot1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plot1.setObjectName("frame_plot1")

        #setup layout frame_plot 1 as horizontalLayout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_plot1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #setup graphics View 1
        #self.graphicsView_1 = QtWidgets.QGraphicsView(self.frame_plot1)
        self.graphicsView_1 = pg.PlotWidget(self.frame_plot1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.graphicsView_1.setSizePolicy(sizePolicy)
        self.graphicsView_1.setMinimumSize(QtCore.QSize(0, 180))
        self.graphicsView_1.setMaximumSize(QtCore.QSize(1000, 200))
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.horizontalLayout.addWidget(self.graphicsView_1)
        self.frame_sensor1.addWidget(self.frame_plot1)

        #setup spacer between frame_plot1 and frame_group1 and add to frame sensor1
        plottobox_horizontalSpacer_1 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.frame_sensor1.addItem(plottobox_horizontalSpacer_1)

        #setup Frame group 1
        self.frame_group1 = QtWidgets.QFrame(self.mainframe)
        self.frame_group1.setMaximumSize(QtCore.QSize(270, 181))
        self.frame_group1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_group1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_group1.setObjectName("frame_group1")

        #setup frame group 1 into grid layout
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_group1)
        self.gridLayout_2.setObjectName("gridLayout_2")

        #spacer in frame gorup 1 grid layout
        #in gridlayout item dimension is (row,column,height(row),width(column))

        verticalSpacer_plot1_1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(verticalSpacer_plot1_1, 1, 1, 1, 1)

        verticalSpacer_plot1_2 = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(verticalSpacer_plot1_2, 3, 1, 1, 1)

        verticalSpacer_plot1_3= QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(verticalSpacer_plot1_3, 5, 1, 1, 1)

        horizontalSpacer_plot1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(horizontalSpacer_plot1, 2, 3, 1, 1)

        #setup Sensor label 1 & Positioning in grid
        self.Sensor1_label = QtWidgets.QLabel(self.frame_group1)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.Sensor1_label.setFont(font)
        self.Sensor1_label.setObjectName("Sensor1_label")
        self.gridLayout_2.addWidget(self.Sensor1_label, 0, 0, 1, 2)
       
        #Setup Radio Button Sensor 1 & Positioning in grid
        self.Normal_1 = QtWidgets.QRadioButton(self.frame_group1)
        self.Normal_1.setObjectName("Normal_1")
        self.Normal_1.setChecked(True)
        self.gridLayout_2.addWidget(self.Normal_1, 4, 0, 1, 1)

        self.Fault_1 = QtWidgets.QRadioButton(self.frame_group1)
        self.Fault_1.setObjectName("Fault_1")
        self.gridLayout_2.addWidget(self.Fault_1, 4, 1, 1, 1)

        #setup Unit sensor 1 & Positioning in grid
        self.unit_1 = QtWidgets.QLabel(self.frame_group1)
        self.unit_1.setMaximumSize(QtCore.QSize(30, 30))
        self.unit_1.setObjectName("unit_1")
        self.gridLayout_2.addWidget(self.unit_1, 2, 2, 1, 1)
        
        # Setup view 1 & Positioning in grid
        self.present_yval1 = QtWidgets.QTextEdit(self.frame_group1)
        self.present_yval1.setMaximumSize(QtCore.QSize(110, 30))
        self.present_yval1.setObjectName("present_yval1")
        self.gridLayout_2.addWidget(self.present_yval1, 2, 0, 1, 2)

        # add frame_group1 into frame_sensor1
        self.frame_sensor1.addWidget(self.frame_group1)

        # add frame_sensor1 into mainframe layout
        self.frameLayout.addLayout(self.frame_sensor1)
        
        #setup frame sensor 2
        self.frame_sensor2 = QtWidgets.QHBoxLayout()
        self.frame_sensor2.setObjectName("frame_sensor2")

        #setup frame plot sensor 2
        self.frame_plot2 = QtWidgets.QFrame(self.mainframe)
        self.frame_plot2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plot2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plot2.setObjectName("frame_plot2")

        #setup layout frame_plot2 as horizontalLayout_4
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_plot2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        #setup grahics view 2
        #self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame_plot2)
        self.graphicsView_2 = pg.PlotWidget(self.frame_plot2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setMinimumSize(QtCore.QSize(0, 180))
        self.graphicsView_2.setMaximumSize(QtCore.QSize(1000, 200))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_4.addWidget(self.graphicsView_2)
        self.frame_sensor2.addWidget(self.frame_plot2)

        #setup spacer between frame_plot2 and frame_group2 and add to frame sensor2
        plottobox_horizontalSpacer_2= QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.frame_sensor2.addItem(plottobox_horizontalSpacer_2)

        #setup frame group 2
        self.frame_group2 = QtWidgets.QFrame(self.mainframe)
        self.frame_group2.setMaximumSize(QtCore.QSize(270, 181))
        self.frame_group2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_group2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_group2.setObjectName("frame_group2")

        #setup frame group 1 into grid layout
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_group2)
        self.gridLayout_5.setObjectName("gridLayout_5")

        #spacer in frame gorup 2 grid layout
        #in gridlayout item dimension is (row,column,height(row),width(column))
        verticalSpacer_plot2_1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(verticalSpacer_plot2_1, 1, 1, 1, 1)

        verticalSpacer_plot2_2 = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(verticalSpacer_plot2_2, 3, 1, 1, 1)

        verticalSpacer_plot2_3 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(verticalSpacer_plot2_3, 5, 1, 1, 1)

        horizontalSpacer_plot2 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(horizontalSpacer_plot2, 2, 3, 1, 1)

        #setup sensor label 2 & Positioning in grid
        self.Sensor2_label = QtWidgets.QLabel(self.frame_group2)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.Sensor2_label.setFont(font)
        self.Sensor2_label.setObjectName("Sensor2_label")
        self.gridLayout_5.addWidget(self.Sensor2_label, 0, 0, 1, 2)

        #setup unit 2 & Positioning in grid
        self.unit_2 = QtWidgets.QLabel(self.frame_group2)
        self.unit_2.setMaximumSize(QtCore.QSize(30, 30))
        self.unit_2.setObjectName("unit_2")
        self.gridLayout_5.addWidget(self.unit_2, 2, 2, 1, 1)

        #setup view 2 & Positioning in grid
        self.present_yval2 = QtWidgets.QTextEdit(self.frame_group2)
        self.present_yval2.setMaximumSize(QtCore.QSize(110, 30))
        self.present_yval2.setObjectName("present_yval2")
        self.gridLayout_5.addWidget(self.present_yval2, 2, 0, 1, 2)

        #setup radio button 2 & Positioning in grid
        self.Normal_2 = QtWidgets.QRadioButton(self.frame_group2)
        self.Normal_2.setObjectName("Normal_2")
        self.gridLayout_5.addWidget(self.Normal_2, 4, 0, 1, 1)
        self.Fault_2 = QtWidgets.QRadioButton(self.frame_group2)
        self.Fault_2.setObjectName("Fault_2")
        self.gridLayout_5.addWidget(self.Fault_2, 4, 1, 1, 1)

        # add frame_group2 into frame_sensor2
        self.frame_sensor2.addWidget(self.frame_group2)

        # add frame_sensor2 into mainframe layout
        self.frameLayout.addLayout(self.frame_sensor2)
        
        #setup frame sensor 3
        self.frame_sensor3 = QtWidgets.QHBoxLayout()
        self.frame_sensor3.setObjectName("frame_sensor3")

        #setup frame plot 3
        self.frame_plot3 = QtWidgets.QFrame(self.mainframe)
        self.frame_plot3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plot3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plot3.setObjectName("frame_plot3")

        #setup layout frame_plot3 as horizontalLayout_6
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_plot3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        #setup graphics View 3
        #self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame_plot3)
        self.graphicsView_3 = pg.PlotWidget(self.frame_plot3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.graphicsView_3.setSizePolicy(sizePolicy)
        self.graphicsView_3.setMinimumSize(QtCore.QSize(0, 180))
        self.graphicsView_3.setMaximumSize(QtCore.QSize(1000, 200))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_6.addWidget(self.graphicsView_3)
        self.frame_sensor3.addWidget(self.frame_plot3)

        #setup spacer between frame_plot3 and frame_group3 and add to frame sensor3
        plottobox_horizontalSpacer_3 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.frame_sensor3.addItem(plottobox_horizontalSpacer_3)

        #setup frame group 3
        self.frame_group3 = QtWidgets.QFrame(self.mainframe)
        self.frame_group3.setMaximumSize(QtCore.QSize(270, 181))
        self.frame_group3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_group3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_group3.setObjectName("frame_group3")

        #setup layout frame_group3 as grid layout
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_group3)
        self.gridLayout_6.setObjectName("gridLayout_6")

        #spacer in frame gorup 3 grid layout
        #in gridlayout item dimension is (row,column,height(row),width(column))

        verticalSpacer_plot3_1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(verticalSpacer_plot3_1, 1, 1, 1, 1)

        verticalSpacer_plot3_1 = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(verticalSpacer_plot3_1, 3, 1, 1, 1)

        verticalSpacer_plot3_3 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(verticalSpacer_plot3_3, 5, 1, 1, 1)

        horizontalSpacer_plot3 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(horizontalSpacer_plot3, 2, 3, 1, 1)

        #setup label sensor 3 & Positioning in grid
        self.Sensor3_label = QtWidgets.QLabel(self.frame_group3)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.Sensor3_label.setFont(font)
        self.Sensor3_label.setObjectName("Sensor3_label")
        self.gridLayout_6.addWidget(self.Sensor3_label, 0, 0, 1, 2)

        #setup unit sensor 3 & Positioning in grid
        self.unit_3 = QtWidgets.QLabel(self.frame_group3)
        self.unit_3.setMaximumSize(QtCore.QSize(30, 30))
        self.unit_3.setObjectName("unit_3")
        self.gridLayout_6.addWidget(self.unit_3, 2, 2, 1, 1)

        #setup View sensor 3 & Positioning in grid
        self.present_yval3 = QtWidgets.QTextEdit(self.frame_group3)
        self.present_yval3.setMaximumSize(QtCore.QSize(110, 30))
        #self.present_yval3.setAlignment(QtCore.Qt.AlignRight)
        self.present_yval3.setObjectName("present_yval3")
        self.gridLayout_6.addWidget(self.present_yval3, 2, 0, 1, 2)

        #setup radio button 3 & Positioning in grid
        self.Normal_3 = QtWidgets.QRadioButton(self.frame_group3)
        self.Normal_3.setObjectName("Normal_3")
        self.gridLayout_6.addWidget(self.Normal_3, 4, 0, 1, 1)

        self.Fault_3 = QtWidgets.QRadioButton(self.frame_group3)
        self.Fault_3.setObjectName("Fault_3")
        self.gridLayout_6.addWidget(self.Fault_3, 4, 1, 1, 1)
        
        #setup frame_group 3 ini frame_sensor 3 layout
        self.frame_sensor3.addWidget(self.frame_group3)

        #setup frame_sensor3 in mainframe
        self.frameLayout.addLayout(self.frame_sensor3)

        #setup vertical layout in mainframe
        self.verticalLayout.addWidget(self.mainframe)

        MainWindow.setCentralWidget(self.centralwidget)

        #setup menubar and statusbar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")

        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionPrint)
        self.menuEdit.addAction(self.actionCopy)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #pyqtgraph
        self.plot_widget = pg.PlotWidget()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MICRON"))
        self.Title_Label.setText(_translate("MainWindow", "Monitoring Sensor"))
        
        self.Normal_1.setText(_translate("MainWindow", "Normal"))
        self.Fault_1.setText(_translate("MainWindow", "Fault"))

        self.Normal_2.setText(_translate("MainWindow", "Normal"))
        self.Fault_2.setText(_translate("MainWindow", "Fault"))
        
        self.Normal_3.setText(_translate("MainWindow", "Normal"))
        self.Fault_3.setText(_translate("MainWindow", "Fault"))

        self.Sensor1_label.setText(_translate("MainWindow", "Kecepatan"))
        self.Sensor2_label.setText(_translate("MainWindow", "Posisi"))
        self.Sensor3_label.setText(_translate("MainWindow", "Arus"))
        
        self.unit_1.setText(_translate("MainWindow", "rpm"))
        self.unit_2.setText(_translate("MainWindow", "rad"))
        self.unit_3.setText(_translate("MainWindow", "Amp"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))

        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))

        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))

        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))

    def startThread(self):
        
        #self.thr = threading.Thread(target=self.update)
        self.th = PlotThread()
        self.th.update_range1.connect(self.graphicsView_1.setXRange)
        self.th.update_yval1.connect(self.graphicsView_1.plot)
        self.th.update_text1.connect(self.present_yval1.setText)

        self.th.update_stat1.connect(self.Normal_1.setChecked)
        self.th.update_stat2.connect(self.Fault_1.setChecked)
        
        self.th.update_range2.connect(self.graphicsView_2.setXRange)
        self.th.update_yval2.connect(self.graphicsView_2.plot)
        self.th.update_text2.connect(self.present_yval2.setText)

        self.th.update_range3.connect(self.graphicsView_3.setXRange)
        self.th.update_yval3.connect(self.graphicsView_3.plot)
        self.th.update_text3.connect(self.present_yval3.setText)

        self.th.start()
        #self.thr.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.startThread()
    MainWindow.show()
    sys.exit(app.exec_())