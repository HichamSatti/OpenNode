#! /usr/bin/ python3
#! -*- coding:utf-8 -*-
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QApplication, 
                             QTextEdit, QAction, QMenu, QMainWindow)
from PyQt5.QtGui import QIcon, QTextCursor, QKeySequence
from PyQt5.QtCore import Qt
import sys
import os
import os.path
from pathlib import Path
from multiprocessing import Queue
from PyQt5 import QtCore, QtGui, QtWidgets
from app.Designer import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import subprocess
import webbrowser
import numpy as np
import numpy 
from subprocess import Popen, STDOUT, PIPE
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import json
import math 
import matplotlib.patches as mpatch
from decimal import Decimal
import matplotlib.patches as mpatches
from matplotlib.patches import Ellipse, Arc
from matplotlib.patches import Circle, PathPatch
from matplotlib.transforms import Bbox
import matplotlib.colors as colors
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
from functools import partial
from matplotlib.widgets import Button
import matplotlib.pyplot
import time
import shlex
import shutil
import inspect

# The new Stream Object which replaces the default stream associated with sys.stdout
# This object just puts data in a queue!
class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)
 
    def write(self,text):
        self.textWritten.emit(str(text))
        pass

    def flush(self):
        pass

#%%%%%%%%%%%%%%       Asm_Div         %%%%%%%%%%%%%%
class Window1(QWidget):
    def __init__(self,nx,ny,nz,parent=None): 
        super(Window1, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)

        self.nx=nx
        self.ny=ny
        self.nz=nz
        
        self.lab4  = [0]*nx
        self.lineEdit8 = [0]*nx
        self.lab5  = [0]*ny
        self.lineEdit9 = [0]*ny
        self.lab6  = [0]*nz
        self.lineEdit10 = [0]*nz
 
        self.dx  = [0]*nx
        self.dy  = [0]*ny
        self.dz  = [0]*nz
        
        self.layout = QVBoxLayout(self)    
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []
        self.types2 =  []
        self.types3 =  []

        M01 = open('app/link/script01.py', "r" ).read() 

        self.lab4[0] = QLabel("<font color=blue > Assemblies Division </font>")
        self.layout.addWidget(self.lab4[0])

        for j in range(1):
            # if j == 0:
                self.types.append("X-Div")
            # elif j == 1:
                self.types2.append("Y-Div")
            # elif j == 2:
                self.types3.append("Z-Div")

        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            for i in range(nx):
                if M01 == 'Cartesian':
                    self.lab4[i] = QLabel("X%s" %(i+1))
                else:
                    self.lab4[i] = QLabel("R %s" %(i+1))
                self.lab4[i].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab4[i], 6, i+1)
                self.lineEdit8[nx*num+m] = QLineEdit()
                typetablayout.addWidget(self.lineEdit8[nx*num+m], j+7, i+1)
                self.lineEdit8[nx*num+m].insert(str(self.dx[nx*num+m]))
                m=m+1
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)
            # Créer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1

        num=0
        for name in self.types2:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout2 = QGridLayout(tab)
            m = 0
            for i in range(ny):
                if M01 == 'Cartesian':
                    self.lab5[i] = QLabel("Y%s" %(i+1))
                else:
                    self.lab5[i] = QLabel("R %s" %(i+1))
                self.lab5[i].setAlignment(Qt.AlignCenter)
                typetablayout2.addWidget(self.lab5[i], 6, i+1)
                self.lineEdit9[ny*num+m] = QLineEdit()
                typetablayout2.addWidget(self.lineEdit9[ny*num+m], j+7, i+1)
                self.lineEdit9[ny*num+m].insert(str(self.dy[ny*num+m]))
                m=m+1
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)
            # Créer un Bouton
            if num == (len(self.types2)-1):
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1

        num=0
        for name in self.types3:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout3 = QGridLayout(tab)
            m = 0
            for i in range(nz):
                if M01 == 'Cartesian':
                    self.lab6[i] = QLabel("Z%s" %(i+1))
                else:
                    self.lab6[i] = QLabel("R %s" %(i+1))
                self.lab6[i].setAlignment(Qt.AlignCenter)
                typetablayout3.addWidget(self.lab6[i], 6, i+1)
                self.lineEdit10[nz*num+m] = QLineEdit()
                typetablayout3.addWidget(self.lineEdit10[nz*num+m], j+7, i+1)
                self.lineEdit10[nz*num+m].insert(str(self.dz[nz*num+m]))
                m=m+1
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)
            # Créer un Bouton
            if num == (len(self.types3)-1):
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1

    def save7(self,num):
	#connexion avec la fenetre main
        del self.dx[:]
        for k in range(len(self.types)):
            self.dx.append([])
            for i in range(self.nx):
                self.dx[k].append(eval(self.lineEdit8[self.nx*k+i].text())) 
        if num == (len(self.types)-1):
            self.close() 
            
        del self.dy[:]
        for k in range(len(self.types2)):
            self.dy.append([])
            for i in range(self.ny):
                self.dy[k].append(eval(self.lineEdit9[self.ny*k+i].text()))   
        if num == (len(self.types2)-1):
            self.close() 
        
        del self.dz[:]
        for k in range(len(self.types3)):
            self.dz.append([])
            for i in range(self.nz):
                self.dz[k].append(eval(self.lineEdit10[self.nz*k+i].text()))   
        if num == (len(self.types3)-1):
            self.close() 
#%%%%%%%%%%%%%%       Asm_Size        %%%%%%%%%%%%%%
class Window111(QWidget):
    def __init__(self,nx,ny,nz,parent=None): 
        super(Window111, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)

        self.nx=nx
        self.ny=ny
        self.nz=nz
        
        self.lab4  = [0]*nx
        self.lineEdit8 = [0]*nx
        self.lab5  = [0]*ny
        self.lineEdit9 = [0]*ny
        self.lab6  = [0]*nz
        self.lineEdit10 = [0]*nz

        self.dx  = [0]*nx
        self.dy  = [0]*ny
        self.dz  = [0]*nz
        
        self.layout = QVBoxLayout(self)    
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []
        self.types2 =  []
        self.types3 =  []

        M01 = open('app/link/script01.py', "r" ).read() 

        self.lab4[0] = QLabel("<font color=blue > Assemblies Size [cm] </font>")
        self.layout.addWidget(self.lab4[0])

        for j in range(1):
            # if j == 0:
                self.types.append("X-Size")
            # elif j == 1:
                self.types2.append("Y-Size")
            # elif j == 2:
                self.types3.append("Z-Size")

        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            for i in range(nx):
                if M01 == 'Cartesian':
                    self.lab4[i] = QLabel("X%s" %(i+1))
                else:
                    self.lab4[i] = QLabel("R %s" %(i+1))
                self.lab4[i].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab4[i], 6, i+1)
                self.lineEdit8[nx*num+m] = QLineEdit()
                typetablayout.addWidget(self.lineEdit8[nx*num+m], j+7, i+1)
                self.lineEdit8[nx*num+m].insert(str(self.dx[nx*num+m]))
                m=m+1
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)
            # Créer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1

        num=0
        for name in self.types2:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout2 = QGridLayout(tab)
            m = 0
            for i in range(ny):
                if M01 == 'Cartesian':
                    self.lab5[i] = QLabel("Y%s" %(i+1))
                else:
                    self.lab5[i] = QLabel("R %s" %(i+1))
                self.lab5[i].setAlignment(Qt.AlignCenter)
                typetablayout2.addWidget(self.lab5[i], 6, i+1)
                self.lineEdit9[ny*num+m] = QLineEdit()
                typetablayout2.addWidget(self.lineEdit9[ny*num+m], j+7, i+1)
                self.lineEdit9[ny*num+m].insert(str(self.dy[ny*num+m]))
                m=m+1
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)
            # Créer un Bouton
            if num == (len(self.types2)-1):
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1

        num=0
        for name in self.types3:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout3 = QGridLayout(tab)
            m = 0
            for i in range(nz):
                if M01 == 'Cartesian':
                    self.lab6[i] = QLabel("Z%s" %(i+1))
                else:
                    self.lab6[i] = QLabel("R %s" %(i+1))
                self.lab6[i].setAlignment(Qt.AlignCenter)
                typetablayout3.addWidget(self.lab6[i], 6, i+1)
                self.lineEdit10[nz*num+m] = QLineEdit()
                typetablayout3.addWidget(self.lineEdit10[nz*num+m], j+7, i+1)
                self.lineEdit10[nz*num+m].insert(str(self.dz[nz*num+m]))
                m=m+1
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)
            # Créer un Bouton
            if num == (len(self.types3)-1):
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1

    def save7(self,num):
	#connexion avec la fenetre main
        del self.dx[:]
        for k in range(len(self.types)):
            self.dx.append([])
            for i in range(self.nx):
                self.dx[k].append(eval(self.lineEdit8[self.nx*k+i].text())) 
        if num == (len(self.types)-1):
            self.close() 
            
        del self.dy[:]
        for k in range(len(self.types2)):
            self.dy.append([])
            for i in range(self.ny):
                self.dy[k].append(eval(self.lineEdit9[self.ny*k+i].text()))   
        if num == (len(self.types2)-1):
            self.close() 
        
        del self.dz[:]
        for k in range(len(self.types3)):
            self.dz.append([])
            for i in range(self.nz):
                self.dz[k].append(eval(self.lineEdit10[self.nz*k+i].text()))   
        if num == (len(self.types3)-1):
            self.close() 
#%%%%%%%%%%%%%%       Z_planar        %%%%%%%%%%%%%%
class Window112(QWidget):
    def __init__(self,nz,parent=None): 
        super(Window112, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)

        self.nz=nz
        self.lab6  = [0]*nz
        self.lineEdit10 = [0]*nz
        self.Vect6  = [0]*nz
        self.zpln  = []


        self.layout = QVBoxLayout(self)    
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []

        self.lab6[0] = QLabel("<font color=blue > Planar Assignment to Z Direction (zpln)</font>")
        # self.lab6[1] = QLabel(" Values =", 1, "to", nz)
        self.layout.addWidget(self.lab6[0])
        
        for j in range(1):
            self.types.append("Z-Planar")
        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            for i in range(nz):
                self.lab6[i] = QLabel("Z%s" %(i+1))
                self.lab6[i].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab6[i], 6, i+1)
                self.lineEdit10[nz*num+m] = QLineEdit()
                typetablayout.addWidget(self.lineEdit10[nz*num+m], j+7, i+1)
                self.lineEdit10[nz*num+m].insert(str(self.Vect6[nz*num+m]))
                m=m+1

            self.layout.addWidget(typetab)
            self.setLayout(self.layout)
            
            #Créer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1


    def save7(self,num):
	#connexion avec la fenetre main
        del self.zpln[:]
        for k in range(len(self.types)):
            self.zpln.append([])
            for i in range(self.nz):
                self.zpln[k].append(eval(self.lineEdit10[self.nz*k+i].text()))   

        if num == (len(self.types)-1):
            self.close() 
#%%%%%%%%%%%%%%       RadialCore      %%%%%%%%%%%%%%
class Window114(QWidget):        
    def __init__(self,np,nx,ny,parent=None):
        super(Window114, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        # self.setMinimumSize(QtCore.QSize(100, 100))
        self.nx = nx
        self.ny = ny
        self.lab6  = [0]*nx*ny*np
        self.lineEdit10 = [0]*nx*ny*np
        self.Vect6 = [0]*nx*ny*np
        self.core_xy = [[[]]]
        self.layout = QVBoxLayout(self)
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []

        # palette = QtGui.QPalette()
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        # brush = QtGui.QBrush(QtGui.QColor(255, 255, 217))
        # typetab.setPalette(palette)

        self.lab6[0] = QLabel(" Material Assignement into Radial Assembly ")
        self.lab6[0].setStyleSheet("color: rgb(12,245,222)")
        self.lab6[0].setFont(QtGui.QFont("Comic Sans MS", 10,QtGui.QFont.Bold))
        self.layout.addWidget(self.lab6[0])
      
        # palette = QtGui.QPalette()
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.lab6[0], brush)
        # brush = QtGui.QBrush(QtGui.QColor(255, 255, 217))
        # brush.setStyle(QtCore.Qt.SolidPattern)

        for i in range(np):
            self.types.append("Planar%s" %(i+1))
        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            s = ny 
            for j in range(ny):
                self.lab6[j] = QLabel("Y%s" %(s))
                self.lab6[j].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab6[j], j+7, 0)
                for i in range(nx):
                    self.lab6[i] = QLabel("X%s" %(i+1))
                    self.lab6[i].setAlignment(Qt.AlignCenter)
                    typetablayout.addWidget(self.lab6[i], 6, i+1)
                    self.lineEdit10[nx*ny*num+m] = QLineEdit()
                    typetablayout.addWidget(self.lineEdit10[nx*ny*num+m], j+7, i+1)
                    self.lineEdit10[nx*ny*num+m].insert(str(self.Vect6[nx*ny*num+m]))
                    m+=1
                s-=1
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)
            #Créer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1
    def save7(self,num):
	#connexion avec la fenetre main
        del self.core_xy[:]
        for k in range(len(self.types)):
            m=0
            self.core_xy.append([])
            for j in range(self.ny):
                self.core_xy[k].append([])
                for i in range(self.nx):
                    self.core_xy[k][j].append(eval(self.lineEdit10[self.nx*self.ny*k+m].text()))
                    m+=1
        if num == (len(self.types)-1):
            self.close() #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%        AxialCore      %%%%%%%%%%%%%%
class Window115(QWidget):        
    def __init__(self,nx,nz,parent=None):
        super(Window115, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        # self.setMinimumSize(QtCore.QSize(100, 100))
        self.nx = nx
        self.nz = nz
        self.lab6  = [0]*nx*nz
        self.lineEdit10 = [0]*nx*nz
        self.Vect6 = [0]*nx*nz
        self.core_z = [[[]]]
        self.layout = QVBoxLayout(self)
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []

        # palette = QtGui.QPalette()
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        # brush = QtGui.QBrush(QtGui.QColor(255, 255, 217))
        # typetab.setPalette(palette)

        self.lab6[0] = QLabel(" Material Assignement into Axial Assembly ")
        self.lab6[0].setStyleSheet("color: rgb(12,245,222)")
        self.lab6[0].setFont(QtGui.QFont("Comic Sans MS", 10,QtGui.QFont.Bold))
        self.layout.addWidget(self.lab6[0])
      
        # palette = QtGui.QPalette()
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.lab6[0], brush)
        # brush = QtGui.QBrush(QtGui.QColor(255, 255, 217))
        # brush.setStyle(QtCore.Qt.SolidPattern)

        self.types.append("Axial Assembly")
        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:15])
            typetablayout = QGridLayout(tab)
            m = 0
            s = nz
            for j in range(nz):
                self.lab6[j] = QLabel("Z%s" %(s))
                self.lab6[j].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab6[j], j+7, 0)
                for i in range(nx):
                    self.lab6[i] = QLabel("X%s" %(i+1))
                    self.lab6[i].setAlignment(Qt.AlignCenter)
                    typetablayout.addWidget(self.lab6[i], 6, i+1)
                    self.lineEdit10[nx*nz*num+m] = QLineEdit()
                    typetablayout.addWidget(self.lineEdit10[nx*nz*num+m], j+7, i+1)
                    self.lineEdit10[nx*nz*num+m].insert(str(self.Vect6[nx*nz*num+m]))
                    m+=1
                s-=1
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)
            #Créer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1
    def save7(self,num):
	#connexion avec la fenetre main
        del self.core_z[:]
        for k in range(len(self.types)):
            m=0
            self.core_z.append([])
            for j in range(self.nz):
                self.core_z[k].append([])
                for i in range(self.nx):
                    self.core_z[k][j].append(eval(self.lineEdit10[self.nx*self.nz*k+m].text()))
                    m+=1
        if num == (len(self.types)-1):
            self.close() #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%     Absorption_XS     %%%%%%%%%%%%%%
class Window9(QWidget):
    def __init__(self,ng,nmat,parent=None):
        super(Window9, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        self.setMinimumSize(QtCore.QSize(100, 100))

        self.ng = ng
        self.lab4  = [0]*ng*nmat
        self.lineEdit4 = [0]*ng*nmat 
        self.Vect6  = [0]*ng*nmat
        self.SigA  = []

        self.layout = QVBoxLayout(self)    
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []
        
        #Main group box
        # box = QGroupBox()
        #self.main_group_box.setStyleSheet("QGroupBox{font-size: 10px}")
        # box.setTitle("Density Function for Neutrons (Chi)")
        # box.setStyleSheet('QGroupBox:title {color: blue;}')
        #self.main_group_box.setLayout(self.layout)

        self.lab4[0] = QLabel("<font color=blue > Absorption Cross Section (SigA)</font>")
        self.layout.addWidget(self.lab4[0])
        
        for j in range(nmat):
            self.types.append("Material %s" %(j+1))
        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            for i in range(ng):
                self.lab4[i] = QLabel("Group %s" %(i+1))
                self.lab4[i].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab4[i], 6, i+1)
                self.lineEdit4[ng*num+m] = QLineEdit()
                typetablayout.addWidget(self.lineEdit4[ng*num+m], j+7, i+1)
                self.lineEdit4[ng*num+m].insert(str(self.Vect6[ng*num+m]))
                m=m+1

            # box.setLayout(typetablayout)
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)

            #Créer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1

    def save7(self,num):
        del self.SigA[:]
        for k in range(len(self.types)):
            m=0
            self.SigA.append([])
            for i in range(self.ng):
                self.SigA[k].append(eval(self.lineEdit4[self.ng*k+m].text()))
                m+=1
        if num == (len(self.types)-1):
            self.close()        
#%%%%%%%%%%%%%%      Transport_XS     %%%%%%%%%%%%%%
class Window10(QWidget):
    def __init__(self,ng,nmat,parent=None):
        super(Window10, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        self.setMinimumSize(QtCore.QSize(100, 100))

        self.ng = ng
        self.lab4  = [0]*ng*nmat
        self.lineEdit4 = [0]*ng*nmat 
        self.Vect6  = [0]*ng*nmat
        self.SigTr  = []

        self.layout = QVBoxLayout(self)    
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []
        
        #Main group box
        # box = QGroupBox()
        #self.main_group_box.setStyleSheet("QGroupBox{font-size: 10px}")
        # box.setTitle("Density Function for Neutrons (Chi)")
        # box.setStyleSheet('QGroupBox:title {color: blue;}')
        #self.main_group_box.setLayout(self.layout)

        self.lab4[0] = QLabel("<font color=blue > Transport Cross Section (SigTr)</font>")
        self.layout.addWidget(self.lab4[0])
        
        for j in range(nmat):
            self.types.append("Material %s" %(j+1))
        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            for i in range(ng):
                self.lab4[i] = QLabel("Group %s" %(i+1))
                self.lab4[i].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab4[i], 6, i+1)
                self.lineEdit4[ng*num+m] = QLineEdit()
                typetablayout.addWidget(self.lineEdit4[ng*num+m], j+7, i+1)
                self.lineEdit4[ng*num+m].insert(str(self.Vect6[ng*num+m]))
                m=m+1

            # box.setLayout(typetablayout)
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)

            #Créer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1

    def save7(self,num):
        del self.SigTr[:]
        for k in range(len(self.types)):
            m=0
            self.SigTr.append([])
            for i in range(self.ng):
                self.SigTr[k].append(eval(self.lineEdit4[self.ng*k+m].text()))
                m+=1
        if num == (len(self.types)-1):
            self.close()        
#%%%%%%%%%%%%%%       Fission_XS      %%%%%%%%%%%%%%
class Window11(QWidget):
    def __init__(self,ng,nmat,parent=None):
        super(Window11, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        self.setMinimumSize(QtCore.QSize(100, 100))

        self.ng = ng
        self.lab4  = [0]*ng*nmat
        self.lineEdit4 = [0]*ng*nmat 
        self.Vect6  = [0]*ng*nmat
        self.SigF  = []

        self.layout = QVBoxLayout(self)    
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []
        
        #Main group box
        # box = QGroupBox()
        #self.main_group_box.setStyleSheet("QGroupBox{font-size: 10px}")
        # box.setTitle("Density Function for Neutrons (Chi)")
        # box.setStyleSheet('QGroupBox:title {color: blue;}')
        #self.main_group_box.setLayout(self.layout)

        self.lab4[0] = QLabel("<font color=blue > Fission Cross Section (SigF)</font>")
        self.layout.addWidget(self.lab4[0])
        
        for j in range(nmat):
            self.types.append("Material %s" %(j+1))
        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            for i in range(ng):
                self.lab4[i] = QLabel("Group %s" %(i+1))
                self.lab4[i].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab4[i], 6, i+1)
                self.lineEdit4[ng*num+m] = QLineEdit()
                typetablayout.addWidget(self.lineEdit4[ng*num+m], j+7, i+1)
                self.lineEdit4[ng*num+m].insert(str(self.Vect6[ng*num+m]))
                m=m+1

            # box.setLayout(typetablayout)
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)

            #Créer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1

    def save7(self,num):
        del self.SigF[:]
        for k in range(len(self.types)):
            m=0
            self.SigF.append([])
            for i in range(self.ng):
                self.SigF[k].append(eval(self.lineEdit4[self.ng*k+m].text()))
                m+=1
        if num == (len(self.types)-1):
            self.close()        
#%%%%%%%%%%%%%%     Nu*Fission_XS     %%%%%%%%%%%%%%
class Window12(QWidget):
    def __init__(self,ng,nmat,parent=None):
        super(Window12, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        self.setMinimumSize(QtCore.QSize(100, 100))

        self.ng = ng
        self.lab4  = [0]*ng*nmat
        self.lineEdit4 = [0]*ng*nmat 
        self.Vect6  = [0]*ng*nmat
        self.NuSigF  = []

        self.layout = QVBoxLayout(self)    
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []
        
        #Main group box
        # box = QGroupBox()
        #self.main_group_box.setStyleSheet("QGroupBox{font-size: 10px}")
        # box.setTitle("Density Function for Neutrons (Chi)")
        # box.setStyleSheet('QGroupBox:title {color: blue;}')
        #self.main_group_box.setLayout(self.layout)

        self.lab4[0] = QLabel("<font color=blue > Nu*Fission Cross Section (NuSigF)</font>")
        self.layout.addWidget(self.lab4[0])
        
        for j in range(nmat):
            self.types.append("Material %s" %(j+1))
        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            for i in range(ng):
                self.lab4[i] = QLabel("Group %s" %(i+1))
                self.lab4[i].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab4[i], 6, i+1)
                self.lineEdit4[ng*num+m] = QLineEdit()
                typetablayout.addWidget(self.lineEdit4[ng*num+m], j+7, i+1)
                self.lineEdit4[ng*num+m].insert(str(self.Vect6[ng*num+m]))
                m=m+1

            # box.setLayout(typetablayout)
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)

            #Créer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1

    def save7(self,num):
        del self.NuSigF[:]
        for k in range(len(self.types)):
            m=0
            self.NuSigF.append([])
            for i in range(self.ng):
                self.NuSigF[k].append(eval(self.lineEdit4[self.ng*k+m].text()))
                m+=1
        if num == (len(self.types)-1):
            self.close()        
#%%%%%%%%%%%%%%         Chi           %%%%%%%%%%%%%%
class Window13(QWidget):
    def __init__(self,ng,nmat,parent=None):
        super(Window13, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        self.setMinimumSize(QtCore.QSize(100, 100))

        self.ng = ng
        self.lab4  = [0]*ng*nmat
        self.lineEdit4 = [0]*ng*nmat 
        self.Vect6  = [0]*ng*nmat
        self.Chi  = []

        self.layout = QVBoxLayout(self)    
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []
        
        #Main group box
        # box = QGroupBox()
        #self.main_group_box.setStyleSheet("QGroupBox{font-size: 10px}")
        # box.setTitle("Density Function for Neutrons (Chi)")
        # box.setStyleSheet('QGroupBox:title {color: blue;}')
        #self.main_group_box.setLayout(self.layout)

        self.lab4[0] = QLabel("<font color=blue > Density Function for Neutrons (Chi)</font>")
        self.layout.addWidget(self.lab4[0])
        
        for j in range(nmat):
            self.types.append("Material %s" %(j+1))
        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            for i in range(ng):
                self.lab4[i] = QLabel("Group %s" %(i+1))
                self.lab4[i].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab4[i], 6, i+1)
                self.lineEdit4[ng*num+m] = QLineEdit()
                typetablayout.addWidget(self.lineEdit4[ng*num+m], j+7, i+1)
                self.lineEdit4[ng*num+m].insert(str(self.Vect6[ng*num+m]))
                m=m+1

            # box.setLayout(typetablayout)
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)

            #Créer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1

    def save7(self,num):
        del self.Chi[:]
        for k in range(len(self.types)):
            m=0
            self.Chi.append([])
            for i in range(self.ng):
                self.Chi[k].append(eval(self.lineEdit4[self.ng*k+m].text()))
                m+=1
        if num == (len(self.types)-1):
            self.close()        
#%%%%%%%%%%%%%%     Scattering_XS     %%%%%%%%%%%%%%
class Window14(QWidget):
    def __init__(self,ng,nmat,parent=None):
        super(Window14, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        self.setMinimumSize(QtCore.QSize(100, 100))
        self.ng = ng
        self.nmat = nmat
        self.lab6  = [0]*ng*ng*nmat
        self.lineEdit10 = [0]*ng*ng*nmat
        self.SigS = [0]*ng*ng*nmat
        self.layout = QVBoxLayout(self)
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []

        self.lab6[0] = QLabel("<font color=blue > Scattering Matrix Cross Section (SigS)</font>")
        self.layout.addWidget(self.lab6[0])

        for i in range(nmat):
            self.types.append("Material %s" %(i+1))
        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            for j in range(ng):
                self.lab6[j] = QLabel("G %s" %(j+1))
                self.lab6[j].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab6[j], j+7, 0)
                for i in range(ng):
                    self.lab6[i] = QLabel("G %s" %(i+1))
                    self.lab6[i].setAlignment(Qt.AlignCenter)
                    typetablayout.addWidget(self.lab6[i], 6, i+1)
                    self.lineEdit10[ng*ng*num+m] = QLineEdit()
                    typetablayout.addWidget(self.lineEdit10[ng*ng*num+m], j+7, i+1)
                    self.lineEdit10[ng*ng*num+m].insert(str(self.SigS[ng*ng*num+m]))
                    m+=1

            self.layout.addWidget(typetab)
            self.setLayout(self.layout)
            #réer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1
    def save7(self,num):
	#connexion avec la fenetre main
        del self.SigS[:]
        for k in range(len(self.types)):
            m=0
            self.SigS.append([])
            for j in range(self.ng):
                self.SigS[k].append([])
                for i in range(self.ng):
                    self.SigS[k][j].append(eval(self.lineEdit10[self.ng*self.ng*k+m].text()))
                    m+=1
        if num == (len(self.types)-1):
            self.close() 

#%%%%%%%%%%%%%%    Energie_Spectrum   %%%%%%%%%%%%%%
class Window16(QWidget):
    def __init__(self,ng,ns,parent=None):
        super(Window16, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        self.setMinimumSize(QtCore.QSize(100, 100))

        self.ng = ng
        self.lab4  = [0]*ng*ns
        self.lineEdit4 = [0]*ng*ns
        self.Vect6  = [0]*ng*ns
        self.sps  = []

        self.layout = QVBoxLayout(self)    
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []
        
        #Main group box
        # box = QGroupBox()
        #self.main_group_box.setStyleSheet("QGroupBox{font-size: 10px}")
        # box.setTitle("Density Function for Neutrons (Chi)")
        # box.setStyleSheet('QGroupBox:title {color: blue;}')
        #self.main_group_box.setLayout(self.layout)

        self.lab4[0] = QLabel("<font color=blue > Source Energie Spectrum (SpS)</font>")
        self.layout.addWidget(self.lab4[0])
        
        for j in range(ns):
            self.types.append("Source %s" %(j+1))
        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            for i in range(ng):
                self.lab4[i] = QLabel("Group %s" %(i+1))
                self.lab4[i].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab4[i], 6, i+1)
                self.lineEdit4[ng*num+m] = QLineEdit()
                typetablayout.addWidget(self.lineEdit4[ng*num+m], j+7, i+1)
                self.lineEdit4[ng*num+m].insert(str(self.Vect6[ng*num+m]))
                m=m+1

            # box.setLayout(typetablayout)
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)

            #Créer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1

    def save7(self,num):
        del self.sps[:]
        for k in range(len(self.types)):
            m=0
            self.sps.append([])
            for i in range(self.ng):
                self.sps[k].append(eval(self.lineEdit4[self.ng*k+m].text()))
                m+=1
        if num == (len(self.types)-1):
            self.close()        
#%%%%%%%%%%%%%%    Source_Density   %%%%%%%%%%%%%%
class Window18(QWidget):
    def __init__(self,ns,parent=None): 
        super(Window18, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        self.setMinimumSize(QtCore.QSize(100, 100))

        self.ns=ns
        self.lab4  = [0]*ns
        self.lineEdit8 = [0]*ns 
        self.ds  = [0]*ns
        
        self.layout = QVBoxLayout(self)    
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []

        self.lab4[0] = QLabel("<font color=blue > Source Density </font>")
        self.layout.addWidget(self.lab4[0])

        for j in range(ns):
            self.types.append("Source %s" %(j+1))
        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            for i in range(1):
                self.lab4[i] = QLabel(" ")
                self.lab4[i].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab4[i], 6, i+1)
                self.lineEdit8[num+m] = QLineEdit()
                typetablayout.addWidget(self.lineEdit8[num+m], j+7, i+1)
                self.lineEdit8[num+m].insert(str(self.ds[num+m]))
                m=m+1

            self.layout.addWidget(typetab)
            self.setLayout(self.layout)
            # Créer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1


    def save7(self,num):
	#connexion avec la fenetre main
        del self.ds[:]
        for k in range(len(self.types)):
            self.ds.append([])
            for i in range(1):
                self.ds[k].append(eval(self.lineEdit8[k+i].text())) 
        if num == (len(self.types)-1):
            self.close()        

#%%%%%%%%%%%%%%       Radial_pos      %%%%%%%%%%%%%%
class Window15(QWidget):
    def __init__(self,ns,npor,parent=None):
        super(Window15, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        self.setMinimumSize(QtCore.QSize(100, 100))
        self.npor = npor
        self.ns = ns
        self.lab6  = [0]*npor*ns
        self.lab7  = [0]*npor*ns
        self.lineEdit10 = [0]*npor*ns
        self.lineEdit11 = [0]*npor*ns
        self.xpos = [0]*npor*ns
        self.ypos = [0]*npor*ns
        self.layout = QVBoxLayout(self)
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []

        self.lab6[0] = QLabel("<font color=blue > Radial X-Y Position of Fixed Sources </font>")
        self.layout.addWidget(self.lab6[0])

        for j in range(ns):
            self.types.append("Source %s" %(j+1))
        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            for i in range(npor):
                    self.lab6[i] = QLabel("X %s" %(i+1))
                    self.lab6[i].setAlignment(Qt.AlignCenter)
                    typetablayout.addWidget(self.lab6[i], i+7, 0)
                    self.lineEdit10[npor*num+m] = QLineEdit()
                    typetablayout.addWidget(self.lineEdit10[npor*num+m], i+7, j+1)
                    self.lineEdit10[npor*num+m].insert(str(self.xpos[npor*num+m]))
                    m+=1
            n = 0
            for i in range(npor):
                    self.lab6[i] = QLabel("Y %s" %(i+1))
                    self.lab6[i].setAlignment(Qt.AlignCenter)
                    typetablayout.addWidget(self.lab6[i], i+7, 6)
                    self.lineEdit11[npor*num+n] = QLineEdit()
                    typetablayout.addWidget(self.lineEdit11[npor*num+n], i+7, j+7)
                    self.lineEdit11[npor*num+n].insert(str(self.ypos[npor*num+n]))
                    n+=1


            self.layout.addWidget(typetab)
            self.setLayout(self.layout)
            #réer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1
    def save7(self,num):
	#connexion avec la fenetre main
        del self.xpos[:]
        del self.ypos[:]
        for k in range(len(self.types)):
            m=0
            self.xpos.append([])
            self.ypos.append([])
            for i in range(self.npor):
                self.xpos[k].append(eval(self.lineEdit10[self.npor*k+m].text()))
                m+=1
            n=0
            for i in range(self.npor):
                self.ypos[k].append(eval(self.lineEdit11[self.npor*k+n].text()))
                n+=1
        if num == (len(self.types)-1):
            self.close() 

#%%%%%%%%%%%%%%        Axial_pos      %%%%%%%%%%%%%%
class Window17(QWidget):
    def __init__(self,npox,ns,parent=None):
        super(Window17, self).__init__(parent)
        self.setWindowTitle("Insert Input Parameters")
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint)
        self.setMinimumSize(QtCore.QSize(100, 100))
        self.npox = npox
        self.ns = ns
        self.lab4  = [0]*npox*ns
        self.lineEdit4 = [0]*npox*ns
        self.zpos = [0]*npox*ns
        self.layout = QVBoxLayout(self)
        typetab = QTabWidget(self)  
        typetab.setFont(QtGui.QFont("Comic Sans MS", 10)) 
        self.types =  []

        #Main group box
        # box = QGroupBox()
        #self.main_group_box.setStyleSheet("QGroupBox{font-size: 10px}")
        # box.setTitle("Density Function for Neutrons (Chi)")
        # box.setStyleSheet('QGroupBox:title {color: blue;}')
        #self.main_group_box.setLayout(self.layout)

        self.lab4[0] = QLabel("<font color=blue > Axial Position of Fixed Sources (Zpos)</font>")
        self.layout.addWidget(self.lab4[0])
        
        for j in range(ns):
            self.types.append("Source %s" %(j+1))
        num=0
        for name in self.types:
            tab =  QWidget()
            typetab.addTab(tab, name[0:10])
            typetablayout = QGridLayout(tab)
            m = 0
            for i in range(npox):
                self.lab4[i] = QLabel("Z %s" %(i+1))
                self.lab4[i].setAlignment(Qt.AlignCenter)
                typetablayout.addWidget(self.lab4[i], i+7, 0)
                self.lineEdit4[npox*num+m] = QLineEdit()
                typetablayout.addWidget(self.lineEdit4[npox*num+m], i+7, j+1)
                self.lineEdit4[npox*num+m].insert(str(self.zpos[npox*num+m]))
                m=m+1

            # box.setLayout(typetablayout)
            self.layout.addWidget(typetab)
            self.setLayout(self.layout)

            #Créer un Bouton
            if num == (len(self.types)-1):
                self.bouton = QPushButton(u"Save and Colse")
                self.bouton.clicked.connect(partial(self.save7,num))
                self.layout.addWidget(self.bouton)
            num+=1

    def save7(self,num):
        del self.zpos[:]
        for k in range(len(self.types)):
            m=0
            self.zpos.append([])
            for i in range(self.npox):
                self.zpos[k].append(eval(self.lineEdit4[self.npox*k+m].text()))
                m+=1
        if num == (len(self.types)-1):
            self.close()        


class Application(QtWidgets.QMainWindow):
    from app.Func import RdPower, AxPower1, AxPower2, Flux, Visualization2D, AxiGeo2D
    def __init__(self, title= "Default", parent=None):
        super(Application, self).__init__(parent)
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)

        self.editor = QTextEdit() 
        self.editor.setTabStopWidth(20)
 
        self.title = title
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(self.title)
        self._initButtons()
        self.isFileOpen = False
        self.isFileCreate = False
        self.initUI()
        widget = QWidget()
        topFiller = QWidget()
        topFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.infoLabel = QLabel(
                "<i>Choose a menu option, or right-click to invoke a context menu</i>",
                alignment=Qt.AlignCenter)
        self.infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        bottomFiller = QWidget()
        bottomFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        vbox = QVBoxLayout()
        vbox.setContentsMargins(5, 5, 5, 5)
        vbox.addWidget(topFiller)
        vbox.addWidget(self.infoLabel)
        vbox.addWidget(bottomFiller)
        widget.setLayout(vbox)

    def _initButtons(self):

        self.ui.radioButton_1.toggled.connect(lambda:self.Method_For(self.ui.radioButton_1))
        self.ui.radioButton_2.toggled.connect(lambda:self.Method_Adj(self.ui.radioButton_2))
        self.ui.radioButton_3.toggled.connect(lambda:self.Method_FxSrc(self.ui.radioButton_3))
#       ---------   Forward   ---------
        self.ui.pushButton_1.clicked.connect(self.new1)
#       ---------
        self.ui.pushButton_2.clicked.connect(self.new2)
#       ---------
        self.ui.pushButton_3.clicked.connect(self.new3)
#       ---------
        self.ui.pushButton_4.clicked.connect(self.UpData_For)
#       ---------
        self.ui.pushButton_5.clicked.connect(self.Compile)
        self.ui.pushButton_5.clicked.connect(self.Progress1)
#       ---------
        self.ui.pushButton_6.clicked.connect(self.Run)
        self.ui.pushButton_6.clicked.connect(self.Progress2)
#       ---------
        self.ui.pushButton_7.clicked.connect(self.RdPower)
        self.ui.pushButton_8.clicked.connect(self.AxPower2)
        self.ui.pushButton_8.clicked.connect(self.AxPower1)
        self.ui.pushButton_9.clicked.connect(self.Flux)
        self.ui.pushButton_10.clicked.connect(self.Comp_Geo)
        self.ui.pushButton_11.clicked.connect(self.Run_Geo)
        self.ui.pushButton_36.clicked.connect(self.Visualization2D)
        self.ui.pushButton_37.clicked.connect(self.AxiGeo2D)

#       ---------
#       ---------   Adjoint   ---------
        self.ui.pushButton_12.clicked.connect(self.new11)
#       ---------
        self.ui.pushButton_13.clicked.connect(self.new12)
#       ---------
        self.ui.pushButton_14.clicked.connect(self.new13)
#       ---------
        self.ui.pushButton_15.clicked.connect(self.UpData_Adj)
#       ---------
        self.ui.pushButton_16.clicked.connect(self.Compile)
        self.ui.pushButton_16.clicked.connect(self.Progress3)
#       ---------
        self.ui.pushButton_17.clicked.connect(self.Run)
        self.ui.pushButton_17.clicked.connect(self.Progress4)
#       ---------
        self.ui.pushButton_18.clicked.connect(self.RdPower)
        self.ui.pushButton_19.clicked.connect(self.AxPower2)
        self.ui.pushButton_19.clicked.connect(self.AxPower1)
        self.ui.pushButton_20.clicked.connect(self.Flux)
        # self.ui.pushButton_21.clicked.connect(self.Plot3D)
        # self.ui.pushButton_22.clicked.connect(self.Plot3D)
#       ---------

#       ---------   Fixed Sources   ---------
        self.ui.pushButton_23.clicked.connect(self.new21)
#       ---------
        self.ui.pushButton_24.clicked.connect(self.new22)
#       ---------
        self.ui.pushButton_25.clicked.connect(self.new23)
#       ---------
        self.ui.pushButton_26.clicked.connect(self.new24)
#       ---------
        self.ui.pushButton_27.clicked.connect(self.new25)
#       ---------
        self.ui.pushButton_28.clicked.connect(self.UpData_FxSrc)
#       ---------
        self.ui.pushButton_29.clicked.connect(self.Compile)
        self.ui.pushButton_29.clicked.connect(self.Progress5)
#       ---------
        self.ui.pushButton_30.clicked.connect(self.Run)
        self.ui.pushButton_30.clicked.connect(self.Progress6)
#       ---------
        self.ui.pushButton_31.clicked.connect(self.RdPower)
        self.ui.pushButton_32.clicked.connect(self.AxPower2)
        self.ui.pushButton_32.clicked.connect(self.AxPower1)
        self.ui.pushButton_33.clicked.connect(self.Flux)
        # self.ui.pushButton_21.clicked.connect(self.Plot3D)
        # self.ui.pushButton_22.clicked.connect(self.Plot3D)
#       ---------

        self.ui.textEdit_1.cursorPositionChanged.connect(self.cursorPosition)
        self.ui.textEdit_2.cursorPositionChanged.connect(self.cursorPosition_2)
#       ---------
        # self.statusbar = self.statusBar()
#       ---------
        self.toolbar = self.ui.toolBar
        
        self.pbar1 = self.ui.progressBar_1
        self.pbar2 = self.ui.progressBar_2
        self.pbar3 = self.ui.progressBar_3
        self.pbar4 = self.ui.progressBar_4
        self.pbar5 = self.ui.progressBar_5
        self.pbar6 = self.ui.progressBar_6
        self.pbar1.setValue(25)
        self.pbar2.setValue(25)
        self.pbar3.setValue(25)
        self.pbar4.setValue(25)
        self.pbar5.setValue(25)
        self.pbar6.setValue(25)
#       ---------
        self.ui.actionNew.triggered.connect(self.NewFile)
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionSave.triggered.connect(self.SaveFile)
        self.ui.actionSave_as.triggered.connect(self.Save_AsFile)
        self.ui.actionCut.setEnabled(False)
        self.ui.actionCut.triggered.connect(self.ui.textEdit_1.cut)
        self.ui.textEdit_1.copyAvailable.connect(self.ui.actionCut.setEnabled)
        self.ui.actionCopy.setEnabled(False)
        self.ui.actionCopy.triggered.connect(self.ui.textEdit_1.copy)
        self.ui.textEdit_1.copyAvailable.connect(self.ui.actionCopy.setEnabled)
        self.ui.actionPaste.triggered.connect(self.ui.textEdit_1.paste)
        self.ui.actionUndo.triggered.connect(self.ui.textEdit_1.undo)
        self.ui.actionRedo.triggered.connect(self.ui.textEdit_1.redo)
        # self.ui.textEdit_1.document().undoAvailable.connect(
                # self.ui.actionUndo.setEnabled)
        # self.ui.textEdit_1.document().redoAvailable.connect(
                # self.ui.actionRedo.setEnabled)
        # self.setWindowModified(self.ui.textEdit_1.document().isModified())
        # self.actionSave.setEnabled(self.textEdit.document().isModified())
        # self.actionUndo.setEnabled(self.textEdit.document().isUndoAvailable())
        # self.actionRedo.setEnabled(self.textEdit.document().isRedoAvailable())

        self.ui.textEdit_1.currentCharFormatChanged.connect(
                self.currentCharFormatChanged)
        # self.ui.actionDelete.triggered.connect(self.Delete)
        # self.ui.actionSelect_All.triggered.connect(self.Select_All)
        # self.ui.actionFind.triggered.connect(self.Find)
        self.ui.actionCompile.triggered.connect(self.Compile)
        self.ui.actionRun.triggered.connect(self.Run)
        self.ui.actionHelp.triggered.connect(self.Help)
        self.ui.actionAbout.triggered.connect(self.About)
        self.ui.actionAbout_Qt.triggered.connect(QApplication.instance().aboutQt)

        # self.ui.actionClose.triggered.connect(self.CloseFile)
        self.ui.actionQuit.triggered.connect(self.Quit)

        # self.ui.action_New.triggered.connect(self.NewFile)

#       ---------------------------
        self.ui.spinBox_3.setRange(2,4)
        self.ui.spinBox_3.setSingleStep(2)
        self.ui.spinBox_4.setRange(1,3)
#       ---------
        self.ui.spinBox_11.setRange(2,4)
        self.ui.spinBox_11.setSingleStep(2)
        self.ui.spinBox_12.setRange(1,3)
#       ---------
        self.ui.spinBox_19.setRange(2,4)
        self.ui.spinBox_19.setSingleStep(2)
        self.ui.spinBox_20.setRange(1,3)
#       ---------


        # Select Active Method
        M00 = open('app/link/script00.py', "r" ).read() 
        if M00 == 'NEM':
            self.ui.radioButton_1.setChecked(True) 
            self.ui.radioButton_2.setChecked(True) 
            self.ui.radioButton_3.setChecked(True) 
            
        # Multi-Group Cross Sections Forward
        self.ui.comboBox_1.currentIndexChanged.connect(self.XS_For)
        M12 = open('app/link/script13.py', "r" ).read() 
        if M12 == 'Absorption_XS':
            self.ui.comboBox_1.setCurrentText('Absorption_XS') 
        elif M12 == 'Transport_XS':
            self.ui.comboBox_1.setCurrentText('Transport_XS')
        elif M12 == 'Fission_XS':
            self.ui.comboBox_1.setCurrentText('Fission_XS')
        elif M12 == 'Nu*Fission_XS':
            self.ui.comboBox_1.setCurrentText('Nu*Fission_XS')
        elif M12 == 'Chi':
            self.ui.comboBox_1.setCurrentText('ChiXS')
        elif M12 == 'Scattering_XS':
            self.ui.comboBox_1.setCurrentText('Scattering_XS')

        # Multi-Group Cross Sections Adjoint
        self.ui.comboBox_11.currentIndexChanged.connect(self.XS_Adj)
        M12 = open('app/link/script13.py', "r" ).read() 
        if M12 == 'Absorption_XS':
            self.ui.comboBox_11.setCurrentText('Absorption_XS') 
        elif M12 == 'Transport_XS':
            self.ui.comboBox_11.setCurrentText('Transport_XS')
        elif M12 == 'Fission_XS':
            self.ui.comboBox_11.setCurrentText('Fission_XS')
        elif M12 == 'Nu*Fission_XS':
            self.ui.comboBox_11.setCurrentText('Nu*Fission_XS')
        elif M12 == 'Chi':
            self.ui.comboBox_11.setCurrentText('ChiXS')
        elif M12 == 'Scattering_XS':
            self.ui.comboBox_11.setCurrentText('Scattering_XS')

        # Multi-Group Cross Sections Fixed Sources
        self.ui.comboBox_21.currentIndexChanged.connect(self.XS_FxSrc)
        M12 = open('app/link/script13.py', "r" ).read() 
        if M12 == 'Absorption_XS':
            self.ui.comboBox_21.setCurrentText('Absorption_XS') 
        elif M12 == 'Transport_XS':
            self.ui.comboBox_21.setCurrentText('Transport_XS')
        elif M12 == 'Fission_XS':
            self.ui.comboBox_21.setCurrentText('Fission_XS')
        elif M12 == 'Nu*Fission_XS':
            self.ui.comboBox_21.setCurrentText('Nu*Fission_XS')
        elif M12 == 'Chi':
            self.ui.comboBox_21.setCurrentText('ChiXS')
        elif M12 == 'Scattering_XS':
            self.ui.comboBox_21.setCurrentText('Scattering_XS')


        # Geometry
        self.ui.comboBox_2.currentIndexChanged.connect(self.Geometry_For)
        M01 = open('app/link/script01.py', "r" ).read() 
        if M01 == 'Cartesian':
            self.ui.comboBox_2.setCurrentText('Cartesian') 

        self.ui.comboBox_12.currentIndexChanged.connect(self.Geometry_Adj)
        M01 = open('app/link/script01.py', "r" ).read() 
        if M01 == 'Cartesian':
            self.ui.comboBox_12.setCurrentText('Cartesian') 

        self.ui.comboBox_22.currentIndexChanged.connect(self.Geometry_FxSrc)
        M01 = open('app/link/script01.py', "r" ).read() 
        if M01 == 'Cartesian':
            self.ui.comboBox_22.setCurrentText('Cartesian') 


        # Constructive Geometry Forward
        self.ui.comboBox_3.currentIndexChanged.connect(self.Geo_For)
        M12 = open('app/link/script17.py', "r" ).read() 
        if M12 == 'Assembly Division':
            self.ui.comboBox_3.setCurrentText('Assembly Division') 
        elif M12 == 'Assembly Size':
            self.ui.comboBox_3.setCurrentText('Assembly Size')
        self.ui.comboBox_4.currentIndexChanged.connect(self.Geo_For)
        M12 = open('app/link/script15.py', "r" ).read() 
        if M12 == 'Planar to Z':
            self.ui.comboBox_4.setCurrentText('Planar to Z')
        elif M12 == 'Material to Assembly':
            self.ui.comboBox_4.setCurrentText('Material to Assembly')

        # Constructive Geometry Adjoint
        self.ui.comboBox_13.currentIndexChanged.connect(self.Geo_Adj)
        M12 = open('app/link/script17.py', "r" ).read() 
        if M12 == 'Assembly Division':
            self.ui.comboBox_13.setCurrentText('Assembly Division') 
        elif M12 == 'Assembly Size':
            self.ui.comboBox_13.setCurrentText('Assembly Size')
        self.ui.comboBox_14.currentIndexChanged.connect(self.Geo_Adj)
        M12 = open('app/link/script15.py', "r" ).read() 
        if M12 == 'Planar to Z':
            self.ui.comboBox_14.setCurrentText('Planar to Z')
        elif M12 == 'Material to Assembly':
            self.ui.comboBox_14.setCurrentText('Material to Assembly')

        # Constructive Geometry Fixed Sources
        self.ui.comboBox_23.currentIndexChanged.connect(self.Geo_FxSrc)
        M12 = open('app/link/script17.py', "r" ).read() 
        if M12 == 'Assembly Division':
            self.ui.comboBox_23.setCurrentText('Assembly Division') 
        elif M12 == 'Assembly Size':
            self.ui.comboBox_23.setCurrentText('Assembly Size')
        self.ui.comboBox_24.currentIndexChanged.connect(self.Geo_FxSrc)
        M12 = open('app/link/script15.py', "r" ).read() 
        if M12 == 'Planar to Z':
            self.ui.comboBox_24.setCurrentText('Planar to Z')
        elif M12 == 'Material to Assembly':
            self.ui.comboBox_24.setCurrentText('Material to Assembly')


        # Forward Boundary Conditions
        self.ui.comboBox_5.currentIndexChanged.connect(self.bc1)
        M00 = open('app/link/script06.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_5.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_5.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_5.setCurrentText('Reflective')

        self.ui.comboBox_6.currentIndexChanged.connect(self.bc2)
        M00 = open('app/link/script07.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_6.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_6.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_6.setCurrentText('Reflective')

        self.ui.comboBox_7.currentIndexChanged.connect(self.bc3)
        M00 = open('app/link/script08.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_7.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_7.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_7.setCurrentText('Reflective')

        self.ui.comboBox_8.currentIndexChanged.connect(self.bc4)
        M00 = open('app/link/script09.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_8.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_8.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_8.setCurrentText('Reflective')

        self.ui.comboBox_9.currentIndexChanged.connect(self.bc5)
        M00 = open('app/link/script10.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_9.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_9.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_9.setCurrentText('Reflective')

        self.ui.comboBox_10.currentIndexChanged.connect(self.bc6)
        M00 = open('app/link/script12.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_10.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_10.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_10.setCurrentText('Reflective')


        # Adjoint Boundary Conditions
        self.ui.comboBox_15.currentIndexChanged.connect(self.bc1)
        M00 = open('app/link/script16.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_15.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_15.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_15.setCurrentText('Reflective')

        self.ui.comboBox_16.currentIndexChanged.connect(self.bc2)
        M00 = open('app/link/script17.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_16.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_16.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_16.setCurrentText('Reflective')

        self.ui.comboBox_17.currentIndexChanged.connect(self.bc3)
        M00 = open('app/link/script18.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_17.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_17.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_17.setCurrentText('Reflective')

        self.ui.comboBox_18.currentIndexChanged.connect(self.bc4)
        M00 = open('app/link/script19.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_18.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_18.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_18.setCurrentText('Reflective')

        self.ui.comboBox_19.currentIndexChanged.connect(self.bc5)
        M00 = open('app/link/script20.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_19.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_19.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_19.setCurrentText('Reflective')

        self.ui.comboBox_20.currentIndexChanged.connect(self.bc6)
        M00 = open('app/link/script22.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_20.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_20.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_20.setCurrentText('Reflective')


        # Fixed Sources Boundary Conditions
        self.ui.comboBox_25.currentIndexChanged.connect(self.bc1)
        M00 = open('app/link/script26.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_25.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_25.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_25.setCurrentText('Reflective')

        self.ui.comboBox_26.currentIndexChanged.connect(self.bc2)
        M00 = open('app/link/script27.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_26.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_26.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_26.setCurrentText('Reflective')

        self.ui.comboBox_27.currentIndexChanged.connect(self.bc3)
        M00 = open('app/link/script28.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_27.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_27.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_27.setCurrentText('Reflective')

        self.ui.comboBox_28.currentIndexChanged.connect(self.bc4)
        M00 = open('app/link/script29.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_28.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_28.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_28.setCurrentText('Reflective')

        self.ui.comboBox_29.currentIndexChanged.connect(self.bc5)
        M00 = open('app/link/script30.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_29.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_29.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_29.setCurrentText('Reflective')

        self.ui.comboBox_30.currentIndexChanged.connect(self.bc6)
        M00 = open('app/link/script32.py', "r" ).read()
        if M00 == 'Vacuum Flux':
            self.ui.comboBox_30.setCurrentText('Vacuum Flux') 
        elif M00 == 'Vacuum Current':
            self.ui.comboBox_30.setCurrentText('Vacuum Current')
        elif M00 == 'Reflective':
            self.ui.comboBox_30.setCurrentText('Reflective')


        # Fixed Source Options
        self.ui.comboBox_31.currentIndexChanged.connect(self.FxSrc_Pos)
        M01 = open('app/link/script24.py', "r" ).read() 
        if M01 == 'Source Density':
            self.ui.comboBox_31.setCurrentText('Source Density') 
        elif M01 == 'Source Spectrum':
            self.ui.comboBox_31.setCurrentText('Source Spectrum')

        self.ui.comboBox_32.currentIndexChanged.connect(self.FxSrc_Pos)
        M01 = open('app/link/script24.py', "r" ).read() 
        if M01 == 'Radial Position':
            self.ui.comboBox_32.setCurrentText('Radial Position') 
        elif M01 == 'Axial Position':
            self.ui.comboBox_32.setCurrentText('Axial Position')


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%     Writing Options Functions    %%%%%%%%%%%%%%
    def Geo_For(self,b):
        open('app/link/script17.py', "w" ).write(self.ui.comboBox_3.currentText())
        open('app/link/script15.py', "w" ).write(self.ui.comboBox_4.currentText())
    def Geo_Adj(self,b):
        open('app/link/script17.py', "w" ).write(self.ui.comboBox_13.currentText())
        open('app/link/script15.py', "w" ).write(self.ui.comboBox_14.currentText())
    def Geo_FxSrc(self,b):
        open('app/link/script17.py', "w" ).write(self.ui.comboBox_23.currentText())
        open('app/link/script15.py', "w" ).write(self.ui.comboBox_24.currentText())

    def XS_For(self,b):
        open('app/link/script13.py', "w" ).write(self.ui.comboBox_1.currentText())
    def XS_Adj(self,b):
        open('app/link/script13.py', "w" ).write(self.ui.comboBox_11.currentText())
    def XS_FxSrc(self,b):
        open('app/link/script13.py', "w" ).write(self.ui.comboBox_21.currentText())

    def Method_For(self,b):
        if b.isChecked() == True:
            self.ui.radioButton_2.setChecked(False)
            self.ui.radioButton_3.setChecked(False)
            open('app/link/script00.py', "w" ).write(b.text()) 
        else:
            open('app/link/script00.py', "w" ).close()
    def Method_Adj(self,b):
        if b.isChecked() == True:
            self.ui.radioButton_1.setChecked(False)
            self.ui.radioButton_3.setChecked(False)
            open('app/link/script00.py', "w" ).write(b.text()) 
        else:
            open('app/link/script00.py', "w" ).close()
    def Method_FxSrc(self,b):
        if b.isChecked() == True:
            self.ui.radioButton_1.setChecked(False)
            self.ui.radioButton_2.setChecked(False)
            open('app/link/script00.py', "w" ).write(b.text()) 
        else:
            open('app/link/script00.py', "w" ).close()

    def Geometry_For(self,b):
        open('app/link/script01.py', "w" ).write(self.ui.comboBox_2.currentText()) 
    def Geometry_Adj(self,b):
        open('app/link/script01.py', "w" ).write(self.ui.comboBox_12.currentText()) 
    def Geometry_FxSrc(self,b):
        open('app/link/script01.py', "w" ).write(self.ui.comboBox_22.currentText()) 

    def bc1(self,b):	
        open('app/link/script06.py', "w" ).write(self.ui.comboBox_5.currentText())
        open('app/link/script16.py', "w" ).write(self.ui.comboBox_15.currentText())
        open('app/link/script26.py', "w" ).write(self.ui.comboBox_25.currentText())
    def bc2(self,b):	
        open('app/link/script07.py', "w" ).write(self.ui.comboBox_6.currentText())
        open('app/link/script17.py', "w" ).write(self.ui.comboBox_16.currentText())
        open('app/link/script27.py', "w" ).write(self.ui.comboBox_26.currentText())
    def bc3(self,b):	
        open('app/link/script08.py', "w" ).write(self.ui.comboBox_7.currentText())
        open('app/link/script18.py', "w" ).write(self.ui.comboBox_17.currentText())
        open('app/link/script28.py', "w" ).write(self.ui.comboBox_27.currentText())
    def bc4(self,b):	
        open('app/link/script09.py', "w" ).write(self.ui.comboBox_8.currentText())
        open('app/link/script19.py', "w" ).write(self.ui.comboBox_18.currentText())
        open('app/link/script29.py', "w" ).write(self.ui.comboBox_28.currentText())
    def bc5(self,b):	
        open('app/link/script10.py', "w" ).write(self.ui.comboBox_9.currentText())
        open('app/link/script20.py', "w" ).write(self.ui.comboBox_19.currentText())
        open('app/link/script30.py', "w" ).write(self.ui.comboBox_29.currentText())
    def bc6(self,b):	
        open('app/link/script12.py', "w" ).write(self.ui.comboBox_10.currentText())
        open('app/link/script22.py', "w" ).write(self.ui.comboBox_20.currentText())
        open('app/link/script32.py', "w" ).write(self.ui.comboBox_30.currentText())

    def FxSrc_Pos(self,b):
        open('app/link/script21.py', "w" ).write(self.ui.comboBox_31.currentText()) 
        open('app/link/script24.py', "w" ).write(self.ui.comboBox_32.currentText()) 
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%     Reading Options Functions     %%%%%%%%%%%%%%
#%%%%%%%%%%%%%%    X-Sections    %%%%%%%%%%%%%%
    def new1(self):
        M06 = open('app/link/script13.py', "r" ).read() 
        ng  = self.ui.spinBox_1.value()
        nmat    = self.ui.spinBox_2.value()
        if  ng == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Energy Groups")
        elif nmat == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Materials")
        else:          
            if M06 == 'Absorption_XS':
                self.wind9 = Window9(ng,nmat)
                self.wind9.show()
            elif M06 == 'Transport_XS':
                self.wind10 = Window10(ng,nmat)
                self.wind10.show()
            elif M06 == 'Fission_XS':
                self.wind11 = Window11(ng,nmat)
                self.wind11.show()
            elif M06 == 'Nu*Fission_XS':
                self.wind12 = Window12(ng,nmat) 
                self.wind12.show()
            elif M06 == 'Chi':
                self.wind13 = Window13(ng,nmat)
                self.wind13.show()
            elif M06 == 'Scattering_XS':
                self.wind14 = Window14(ng,nmat)
                self.wind14.show()
            else:
                QMessageBox.warning(self, "Warning", "Choose Cross Sections Options")
    def new11(self):
        M06 = open('app/link/script13.py', "r" ).read() 
        ng  = self.ui.spinBox_9.value()
        nmat    = self.ui.spinBox_10.value()
        if  ng == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Energy Groups")
        elif nmat == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Materials")
        else:          
            if M06 == 'Absorption_XS':
                self.wind9 = Window9(ng,nmat)
                self.wind9.show()
            elif M06 == 'Transport_XS':
                self.wind10 = Window10(ng,nmat)
                self.wind10.show()
            elif M06 == 'Fission_XS':
                self.wind11 = Window11(ng,nmat)
                self.wind11.show()
            elif M06 == 'Nu*Fission_XS':
                self.wind12 = Window12(ng,nmat) 
                self.wind12.show()
            elif M06 == 'Chi':
                self.wind13 = Window13(ng,nmat)
                self.wind13.show()
            elif M06 == 'Scattering_XS':
                self.wind14 = Window14(ng,nmat)
                self.wind14.show()
            else:
                QMessageBox.warning(self, "Warning", "Choose Cross Sections Options")
    def new21(self):
        M06 = open('app/link/script13.py', "r" ).read() 
        ng  = self.ui.spinBox_17.value()
        nmat    = self.ui.spinBox_18.value()
        if  ng == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Energy Groups")
        elif nmat == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Materials")
        else:          
            if M06 == 'Absorption_XS':
                self.wind9 = Window9(ng,nmat)
                self.wind9.show()
            elif M06 == 'Transport_XS':
                self.wind10 = Window10(ng,nmat)
                self.wind10.show()
            elif M06 == 'Fission_XS':
                self.wind11 = Window11(ng,nmat)
                self.wind11.show()
            elif M06 == 'Nu*Fission_XS':
                self.wind12 = Window12(ng,nmat) 
                self.wind12.show()
            elif M06 == 'Chi':
                self.wind13 = Window13(ng,nmat)
                self.wind13.show()
            elif M06 == 'Scattering_XS':
                self.wind14 = Window14(ng,nmat)
                self.wind14.show()
            else:
                QMessageBox.warning(self, "Warning", "Choose Cross Sections Options")

#%%%%%%%%%%%%%%     Geometry     %%%%%%%%%%%%%%
    def new2(self):
        M06 = open('app/link/script17.py', "r" ).read() 
        dim   = self.ui.spinBox_4.value()
        nx    = self.ui.spinBox_5.value()
        ny    = self.ui.spinBox_6.value()
        nz    = self.ui.spinBox_7.value()
        if   nx == 0:
            QMessageBox.warning(self, "Warning", "Enter X-Assembly Number")
        elif ny == 0:
            QMessageBox.warning(self, "Warning", "Enter Y-Assembly Number")
        elif nz == 0:
            QMessageBox.warning(self, "Warning", "Enter Z-Assembly Number")
        elif dim == 1 and nx < 1 and nz < 1 :
            QMessageBox.warning(self, "Warning", "X-Z-Assembly Number Shall Be at Least Equal 1")
        elif dim == 2 and nz < 1:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be at Least Equal 1")
        elif nx  < 1:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be at Least Equal 1")
        elif ny  < 1:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be at Least Equal 1")
        elif nz  < 1:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be at Least Equal 1")
        elif nx  > 33:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be Maximum Equal 33")
        elif ny  > 33:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be Maximum Equal 33")
        elif nz  > 40:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be Maximum Equal 40")
        else:          
            if M06 == 'Assembly Division':
                self.wind1 = Window1(nx,ny,nz)
                self.wind1.show()
            elif M06 == 'Assembly Size':
                self.wind111 = Window111(nx,ny,nz)
                self.wind111.show()
            else:
                QMessageBox.warning(self, "Warning", "Choose Assembly Options")
    def new3(self):
        M06 = open('app/link/script15.py', "r" ).read() 
        dim = self.ui.spinBox_4.value()
        nx  = self.ui.spinBox_5.value()
        ny  = self.ui.spinBox_6.value()
        nz  = self.ui.spinBox_7.value()
        np  = self.ui.spinBox_8.value()
        if   nx  == 0:
            QMessageBox.warning(self, "Warning", "Enter X-Assembly Number")
        elif ny  == 0:
            QMessageBox.warning(self, "Warning", "Enter Y-Assembly Number")
        elif nz  == 0:
            QMessageBox.warning(self, "Warning", "Enter Z-Assembly Number")
        elif np  == 0:
            QMessageBox.warning(self, "Warning", "Enter Planar Number")
        elif dim == 1 and nx < 1 and nz < 1 :
            QMessageBox.warning(self, "Warning", "X-Z-Assembly Number Shall Be at Least Equal 2")
        elif dim == 2 and nz < 1:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Must Be Equal 1")
        elif dim == 1 and np != 1:
            QMessageBox.warning(self, "Warning", "Planar Number Must Be Equal 1")
        elif dim == 2 and np != 1:
            QMessageBox.warning(self, "Warning", "Planar Number Must Be Equal 1")
        elif nx   < 1:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be at Least Equal 1")
        elif ny   < 1:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be at Least Equal 1")
        elif nz   < 1:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be at Least Equal 1")
        elif nx   > 33:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be Maximum Equal 33")
        elif ny   > 33:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be Maximum Equal 33")
        elif nz   > 40:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be Maximum Equal 40")
        else:          
            if M06 == 'Planar to Z':
                self.wind112 = Window112(nz)
                self.wind112.show()
            elif M06 == 'Material to XY':
                self.wind114 = Window114(np,nx,ny)
                self.wind114.show()
            elif M06 == 'Material to Z':
                self.wind115 = Window115(nx,nz)
                self.wind115.show()
            else:
                QMessageBox.warning(self, "Warning", "Choose Assignement Options")

    def new12(self):
        M06 = open('app/link/script17.py', "r" ).read() 
        dim   = self.ui.spinBox_12.value()
        nx    = self.ui.spinBox_13.value()
        ny    = self.ui.spinBox_14.value()
        nz    = self.ui.spinBox_15.value()
        if   nx == 0:
            QMessageBox.warning(self, "Warning", "Enter X-Assembly Number")
        elif ny == 0:
            QMessageBox.warning(self, "Warning", "Enter Y-Assembly Number")
        elif nz == 0:
            QMessageBox.warning(self, "Warning", "Enter Z-Assembly Number")
        elif dim == 1 and nx < 2 or nz < 2 :
            QMessageBox.warning(self, "Warning", "X-Z-Assembly Number Shall Be at Least Equal 2")
        elif dim == 2 and nz < 2:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Must Be Equal 2")
        elif nx  < 2:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be at Least Equal 2")
        elif ny  < 2:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be at Least Equal 2")
        elif nz  < 2:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be at Least Equal 2")
        elif nx  > 33:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be Maximum Equal 33")
        elif ny  > 33:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be Maximum Equal 33")
        elif nz  > 40:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be Maximum Equal 40")
        else:          
            if M06 == 'Assembly Division':
                self.wind1 = Window1(nx,ny,nz)
                self.wind1.show()
            elif M06 == 'Assembly Size':
                self.wind111 = Window111(nx,ny,nz)
                self.wind111.show()
            else:
                QMessageBox.warning(self, "Warning", "Choose Assembly Options")
    def new13(self):
        M06 = open('app/link/script15.py', "r" ).read() 
        dim = self.ui.spinBox_12.value()
        nx  = self.ui.spinBox_13.value()
        ny  = self.ui.spinBox_14.value()
        nz  = self.ui.spinBox_15.value()
        np  = self.ui.spinBox_16.value()
        if   nx  == 0:
            QMessageBox.warning(self, "Warning", "Enter X-Assembly Number")
        elif ny  == 0:
            QMessageBox.warning(self, "Warning", "Enter Y-Assembly Number")
        elif nz  == 0:
            QMessageBox.warning(self, "Warning", "Enter Z-Assembly Number")
        elif np  == 0:
            QMessageBox.warning(self, "Warning", "Enter Planar Number")
        elif dim == 1 and nx < 2 or nz < 2 :
            QMessageBox.warning(self, "Warning", "X-Z-Assembly Number Shall Be at Least Equal 2")
        elif dim == 2 and nz < 2:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Must Be Equal 2")
        elif dim == 1 and np != 1:
            QMessageBox.warning(self, "Warning", "Planar Number Must Be Equal 1")
        elif dim == 2 and np != 1:
            QMessageBox.warning(self, "Warning", "Planar Number Must Be Equal 1")
        elif nx   < 2:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be at Least Equal 2")
        elif ny   < 2:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be at Least Equal 2")
        elif nz   < 2:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be at Least Equal 2")
        elif nx   > 33:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be Maximum Equal 33")
        elif ny   > 33:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be Maximum Equal 33")
        elif nz   > 40:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be Maximum Equal 40")
        else:       

        
            if M06 == 'Planar to Z':
                self.wind112 = Window112(nz)
                self.wind112.show()
            elif M06 == 'Material to XY':
                self.wind114 = Window114(np,nx,ny)
                self.wind114.show()
            elif M06 == 'Material to Z':
                self.wind115 = Window115(nx,nz)
                self.wind115.show()
            else:
                QMessageBox.warning(self, "Warning", "Choose Assignement Options")

    def new22(self):
        M06 = open('app/link/script17.py', "r" ).read() 
        dim   = self.ui.spinBox_20.value()
        nx    = self.ui.spinBox_21.value()
        ny    = self.ui.spinBox_22.value()
        nz    = self.ui.spinBox_23.value()
        if   nx == 0:
            QMessageBox.warning(self, "Warning", "Enter X-Assembly Number")
        elif ny == 0:
            QMessageBox.warning(self, "Warning", "Enter Y-Assembly Number")
        elif nz == 0:
            QMessageBox.warning(self, "Warning", "Enter Z-Assembly Number")
        elif dim == 2 and nz != 2:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Must Be Equal 2")
        elif nx  < 2:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be at Least Equal 2")
        elif ny  < 2:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be at Least Equal 2")
        elif nz  < 2:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be at Least Equal 2")
        elif nx  > 33:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be Maximum Equal 33")
        elif ny  > 33:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be Maximum Equal 33")
        elif nz  > 40:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be Maximum Equal 40")
        else:          
            if M06 == 'Assembly Division':
                self.wind1 = Window1(nx,ny,nz)
                self.wind1.show()
            elif M06 == 'Assembly Size':
                self.wind111 = Window111(nx,ny,nz)
                self.wind111.show()
            else:
                QMessageBox.warning(self, "Warning", "Choose Assembly Options")
    def new23(self):
        M06 = open('app/link/script15.py', "r" ).read() 
        dim   = self.ui.spinBox_20.value()
        nx    = self.ui.spinBox_21.value()
        ny    = self.ui.spinBox_22.value()
        nz    = self.ui.spinBox_23.value()
        np    = self.ui.spinBox_24.value()
        if   nx  == 0:
            QMessageBox.warning(self, "Warning", "Enter X-Assembly Number")
        elif ny  == 0:
            QMessageBox.warning(self, "Warning", "Enter Y-Assembly Number")
        elif nz  == 0:
            QMessageBox.warning(self, "Warning", "Enter Z-Assembly Number")
        elif np  == 0:
            QMessageBox.warning(self, "Warning", "Enter Planar Number")
        elif dim == 2 and nz != 2:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Must Be Equal 2")
        elif dim == 2 and np != 1:
            QMessageBox.warning(self, "Warning", "Planar Number Must Be Equal 1")
        elif nx   < 2:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be at Least Equal 2")
        elif ny   < 2:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be at Least Equal 2")
        elif nz   < 2:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be at Least Equal 2")
        elif nx   > 33:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be Maximum Equal 33")
        elif ny   > 33:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be Maximum Equal 33")
        elif nz   > 40:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be Maximum Equal 40")
        else:          
            if M06 == 'Planar to Z':
                self.wind112 = Window112(nz)
                self.wind112.show()
            elif M06 == 'Material to XY':
                self.wind114 = Window114(np,nx,ny)
                self.wind114.show()
            elif M06 == 'Material to Z':
                self.wind115 = Window115(nx,nz)
                self.wind115.show()
            else:
                QMessageBox.warning(self, "Warning", "Choose Assignement Options")

    def new24(self):
        M06 = open('app/link/script21.py', "r" ).read() 
        ng = self.ui.spinBox_17.value()
        ns = self.ui.spinBox_25.value()
        if   ng  == 0:
            QMessageBox.warning(self, "Warning", "Enter The Energy Groups")
        elif ns  == 0:
            QMessageBox.warning(self, "Warning", "Enter The Source Number")
        # elif ds  == 0:
            # QMessageBox.warning(self, "Warning", "Enter The Source Density")
        # elif ds   < 0 or ds   == 0 :
            # QMessageBox.warning(self, "Warning", "Source Density Shall Be Greater Than Zero")
        else:          
            if M06 == 'Source Density':
                self.wind18 = Window18(ns)
                self.wind18.show()
            elif M06 == 'Source Spectrum':
                self.wind16 = Window16(ng,ns)
                self.wind16.show()
            else:
                QMessageBox.warning(self, "Warning", "Choose Density/Spectrum Options")

    def new25(self):
        M06 = open('app/link/script24.py', "r" ).read() 
        ns = self.ui.spinBox_25.value()
        npor = self.ui.spinBox_26.value()
        npox = self.ui.spinBox_27.value()
        if   ns  == 0:
            QMessageBox.warning(self, "Warning", "Enter The Source Number")
        # elif ds  == 0:
            # QMessageBox.warning(self, "Warning", "Enter The Source Density")
        elif npor  == 0:
            QMessageBox.warning(self, "Warning", "Enter Radial Fixed Source Number")
        elif npox  == 0:
            QMessageBox.warning(self, "Warning", "Enter Axial Fixed Source Number")
        # elif ds   < 0 or ds   == 0 :
            # QMessageBox.warning(self, "Warning", "Source Density Shall Be Greater Than Zero")
        else:          
            if M06 == 'Radial Position':
                self.wind15 = Window15(ns,npor)
                self.wind15.show()
            elif M06 == 'Axial Position':
                self.wind17 = Window17(npox,ns)
                self.wind17.show()
            else:
                QMessageBox.warning(self, "Warning", "Choose Fixed Sources Position")

#%%%%%%%%%%%%%%    Upload Data   %%%%%%%%%%%%%%
    def UpData_For(self):
        Geometry_type = open('app/link/script01.py', "r" ).read()
        ng    = self.ui.spinBox_1.value()
        nmat  = self.ui.spinBox_2.value()
        order = self.ui.spinBox_3.value()
        dim   = self.ui.spinBox_4.value()
        nx    = self.ui.spinBox_5.value()
        ny    = self.ui.spinBox_6.value()
        nz    = self.ui.spinBox_7.value()
        np    = self.ui.spinBox_8.value()

        if   ng    == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Energy Groups")
        elif nmat  == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Materials")
        elif order == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Polynomial Order")
        elif dim   == 0:
            QMessageBox.warning(self, "Warning", "Enter Dimension Number")
        elif nx    == 0:
            QMessageBox.warning(self, "Warning", "Enter X-Assembly Number")
        elif ny    == 0:
            QMessageBox.warning(self, "Warning", "Enter Y-Assembly Number")
        elif nz    == 0:
            QMessageBox.warning(self, "Warning", "Enter Z-Assembly Number")
        elif np    == 0:
            QMessageBox.warning(self, "Warning", "Enter Planar Number")
        elif dim == 1 and nx < 1 or nz < 1 :
            QMessageBox.warning(self, "Warning", "X-Z-Assembly Number Shall Be at Least Equal 1")
        elif dim == 2   and    nz < 1:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Must Be Equal 1")
        elif dim   == 1 and    np != 1:
            QMessageBox.warning(self, "Warning", "Planar Number Must Be Equal 1")
        elif dim   == 2 and    np != 1:
            QMessageBox.warning(self, "Warning", "Planar Number Must Be Equal 1")
        elif order != 2 and order != 4:
            QMessageBox.warning(self, "Warning", "Polynomial Order Shall Be 2 Or 4")
        elif nx     < 1:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be at Least Equal 1")
        elif ny     < 1:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be at Least Equal 1")
        elif nz     < 1:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be at Least Equal 1")
        elif nx     > 33:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be Maximum Equal 33")
        elif ny     > 33:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be Maximum Equal 33")
        elif nz     > 40:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be Maximum Equal 40")
        elif self.ui.comboBox_1.currentText() == '                X-S':
            QMessageBox.warning(self, "Warning", "Choose X-S Option")
        elif self.ui.comboBox_3.currentText() == '       Division/Size':
            QMessageBox.warning(self, "Warning", "Choose Constructive Geometry Option")
        elif self.ui.comboBox_4.currentText() == '        Assignement':
            QMessageBox.warning(self, "Warning", "Choose Assignement Option")
        elif self.ui.comboBox_5.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose East BC Option")
        elif self.ui.comboBox_6.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose West BC Option")
        elif self.ui.comboBox_7.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose North BC Option")
        elif self.ui.comboBox_8.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose South BC Option")
        elif self.ui.comboBox_9.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose Top BC Option")
        elif self.ui.comboBox_10.currentText()== '             BC':
            QMessageBox.warning(self, "Warning", "Choose Bottom BC Option")
        # elif self.ui.pushButton_3.isChecked():
            # QMessageBox.warning(self, "Warning", "Choose Z-Planar Option")
        else:
            if   self.ui.tabWidget_1.currentIndex()== 0:
                Mode = 'Forward'
            if   self.ui.tabWidget_1.currentIndex()== 1:
                Mode = 'Adjoint'
            if   self.ui.tabWidget_1.currentIndex()== 2:
                Mode = 'Fixed Source'

            if   self.ui.comboBox_5.currentText()== 'Vacuum Flux':
                x_east= 0
            elif self.ui.comboBox_5.currentText()== 'Vacuum Current':
                x_east= 1
            elif self.ui.comboBox_5.currentText()== 'Reflective':
                x_east= 2

            if   self.ui.comboBox_6.currentText()== 'Vacuum Flux':
                x_west= 0
            elif self.ui.comboBox_6.currentText()== 'Vacuum Current':
                x_west= 1
            elif self.ui.comboBox_6.currentText()== 'Reflective':
                x_west= 2

            if   self.ui.comboBox_7.currentText()== 'Vacuum Flux':
                y_north= 0
            elif self.ui.comboBox_7.currentText()== 'Vacuum Current':
                y_north= 1
            elif self.ui.comboBox_7.currentText()== 'Reflective':
                y_north= 2

            if   self.ui.comboBox_8.currentText()== 'Vacuum Flux':
                y_south= 0
            elif self.ui.comboBox_8.currentText()== 'Vacuum Current':
                y_south= 1
            elif self.ui.comboBox_8.currentText()== 'Reflective':
                y_south= 2

            if   self.ui.comboBox_9.currentText()== 'Vacuum Flux':
                z_top= 0
            elif self.ui.comboBox_9.currentText()== 'Vacuum Current':
                z_top= 1
            elif self.ui.comboBox_9.currentText()== 'Reflective':
                z_top= 2

            if   self.ui.comboBox_10.currentText()== 'Vacuum Flux':
                z_bott= 0
            elif self.ui.comboBox_10.currentText()== 'Vacuum Current':
                z_bott= 1
            elif self.ui.comboBox_10.currentText()== 'Reflective':
                z_bott= 2

            wind1    = Window1(nx,ny,nz)
            wind111  = Window111(nx,ny,nz)
            wind112  = Window112(nz)
            wind114  = Window114(np,nx,ny)
            wind115  = Window115(nx,nz)
            wind9    = Window9(ng,nmat)
            wind10   = Window10(ng,nmat)
            wind11   = Window11(ng,nmat)
            wind12   = Window12(ng,nmat)
            wind13   = Window13(ng,nmat)
            wind14   = Window14(ng,nmat)
            # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Forward"))
            # self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_1), _translate("MainWindow", "Forward"))


            filename = open("app/input/input.json",'w')
            open('app/link/script.dir', "w" ).write(os.path.abspath(os.path.dirname( __file__)) +'/input/input.json')
            filename.write('{\n   "Data": \n   { \n      "Parameters": \n      { \n         "ID": 100,')
            filename.write('\n         "Calculation Mode": '+'"'+str(Mode)+'"' +',')
            # filename.write('\n         "Number of Energy Groups": '+ str(ng) +',')
            # filename.write('\n         "Number of Materials": '+ str(nmat) +',')
            # filename.write('\n         "Polynomial Order": '+ str(order)+',')
            filename.write('\n         "Dimensions": '+ str(dim)+',')
            filename.write('\n         "Number of X-Assembly": '+ str(nx) +',')
            filename.write('\n         "Number of Y-Assembly": '+ str(ny) +',')
            filename.write('\n         "Number of Z-Assembly": '+ str(nz) +',')
            # filename.write('\n         "X-Assembly Division": '+ str(self.wind1.dx[0]) +',')
            # filename.write('\n         "Y-Assembly Division": '+ str(self.wind1.dy[0]) +',')
            # filename.write('\n         "Z-Assembly Division": '+ str(self.wind1.dz[0]) +',')
            filename.write('\n         "X-Assembly Size": '+ str(self.wind111.dx[0]) +',')
            filename.write('\n         "Y-Assembly Size": '+ str(self.wind111.dy[0]) +',')
            filename.write('\n         "Z-Assembly Size": '+ str(self.wind111.dz[0]) +',')
            filename.write('\n         "Number of Planar": '+ str(np) +',')
            filename.write('\n         "Planar Assignement to Z": '+ str(self.wind112.zpln[0]))


            filename.write('\n      }, \n      "Materials": \n      [')
            # Boucle sur les Matériaux
            # for i in range(nmat):
                # filename.write('{ \n         "ID": '+ str(i+1) +', \n        "Name": "Material '+ str(i+1) +'",') 
                # filename.write('\n        "Absorption_XS": ' + str(self.wind9.SigA[i][:]) +','
                                   # + '\n        "Transport_XS": '+ str(self.wind10.SigTr[i][:])+','
                                   # + '\n        "Fission_XS": '+ str(self.wind11.SigF[i][:])+','
                                   # + '\n        "Nu*Fission_XS": '+ str(self.wind12.NuSigF[i][:])+','
                                   # + '\n        "Chi": '+ str(self.wind13.Chi[i][:])+',')
                # filename.write('\n        "Scattering_XS":'+str(self.wind14.SigS[i][:]))
                # if i == nmat-1:
                    # filename.write('\n       }],')
                # else:
                    # filename.write('\n       },\n       ')  

            filename.write('\n      "Assemblies": \n      [')
            # Boucle sur Core
            for i in range(np):
                filename.write('{ \n         "ID": '+ str(i+1) +', \n         "Name": "Planar '+ str(i+1) +'",') 
                filename.write('\n         "Assembly": ' + str(self.wind114.core_xy[i]))
                if i == np-1:
                    filename.write('\n       }],')
                else:
                    filename.write('\n       },\n       ')  
            filename.write('\n      "XY_Assembly": ' + str(self.wind114.core_xy)+',') 
            filename.write('\n      "Z_Assembly": ' + str(self.wind115.core_z)+',') 

            # filename.write('\n      "Boundary Condition": \n      { ')
            # filename.write('\n         "X_East": '+ str(x_east)+',')
            # filename.write('\n         "X_West": '+ str(x_west)+',')
            # filename.write('\n         "Y_North": '+ str(y_north)+',')
            # filename.write('\n         "Y_South": '+ str(y_south)+',')
            # filename.write('\n         "Z_Top": '+ str(z_top)+',')
            # filename.write('\n         "Z_Bottom": '+ str(z_bott))
            # filename.write('\n      }')

            # Fin Boucle
            filename.write('\n   } \n}') 
            filename.close() 
            fh = open("app/input/input.json","r")  
            self.ui.textEdit_1.setText(fh.read())    
            fh.close()  
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def UpData_Adj(self):
        Geometry_type = open('app/link/script01.py', "r" ).read()
        ng    = self.ui.spinBox_9.value()
        nmat  = self.ui.spinBox_10.value()
        order = self.ui.spinBox_11.value()
        dim   = self.ui.spinBox_12.value()
        nx    = self.ui.spinBox_13.value()
        ny    = self.ui.spinBox_14.value()
        nz    = self.ui.spinBox_15.value()
        np    = self.ui.spinBox_16.value()

        if   ng    == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Energy Groups")
        elif nmat  == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Materials")
        elif order == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Polynomial Order")
        elif dim   == 0:
            QMessageBox.warning(self, "Warning", "Enter Dimension Number")
        elif nx    == 0:
            QMessageBox.warning(self, "Warning", "Enter X-Assembly Number")
        elif ny    == 0:
            QMessageBox.warning(self, "Warning", "Enter Y-Assembly Number")
        elif nz    == 0:
            QMessageBox.warning(self, "Warning", "Enter Z-Assembly Number")
        elif np    == 0:
            QMessageBox.warning(self, "Warning", "Enter Planar Number")
        elif dim == 1 and nx < 2 or nz < 2 :
            QMessageBox.warning(self, "Warning", "X-Z-Assembly Number Shall Be at Least Equal 2")
        elif dim == 2   and    nz < 2:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Must Be Equal 2")
        elif dim   == 1 and    np != 1:
            QMessageBox.warning(self, "Warning", "Planar Number Must Be Equal 1")
        elif dim   == 2 and    np != 1:
            QMessageBox.warning(self, "Warning", "Planar Number Must Be Equal 1")
        elif order != 2 and order != 4:
            QMessageBox.warning(self, "Warning", "Polynomial Order Shall Be 2 Or 4")
        elif nx     < 2:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be at Least Equal 2")
        elif ny     < 2:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be at Least Equal 2")
        elif nz     < 2:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be at Least Equal 2")
        elif nx     > 33:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be Maximum Equal 33")
        elif ny     > 33:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be Maximum Equal 33")
        elif nz     > 40:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be Maximum Equal 40")
        elif self.ui.comboBox_11.currentText() == '                X-S':
            QMessageBox.warning(self, "Warning", "Choose X-S Option")
        elif self.ui.comboBox_13.currentText() == '       Division/Size':
            QMessageBox.warning(self, "Warning", "Choose Constructive Geometry Option")
        elif self.ui.comboBox_14.currentText() == '        Assignement':
            QMessageBox.warning(self, "Warning", "Choose Assignement Option")
        elif self.ui.comboBox_15.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose East BC Option")
        elif self.ui.comboBox_16.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose West BC Option")
        elif self.ui.comboBox_17.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose North BC Option")
        elif self.ui.comboBox_18.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose South BC Option")
        elif self.ui.comboBox_19.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose Top BC Option")
        elif self.ui.comboBox_20.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose Bottom BC Option")
        # elif self.ui.pushButton_3.isChecked():
            # QMessageBox.warning(self, "Warning", "Choose Z-Planar Option")
        else:
            if   self.ui.tabWidget_1.currentIndex()== 0:
                Mode = 'Forward'
            if   self.ui.tabWidget_1.currentIndex()== 1:
                Mode = 'Adjoint'
            if   self.ui.tabWidget_1.currentIndex()== 2:
                Mode = 'Fixed Source'

            if   self.ui.comboBox_15.currentText()== 'Vacuum Flux':
                x_east= 0
            elif self.ui.comboBox_15.currentText()== 'Vacuum Current':
                x_east= 1
            elif self.ui.comboBox_15.currentText()== 'Reflective':
                x_east= 2

            if   self.ui.comboBox_16.currentText()== 'Vacuum Flux':
                x_west= 0
            elif self.ui.comboBox_16.currentText()== 'Vacuum Current':
                x_west= 1
            elif self.ui.comboBox_16.currentText()== 'Reflective':
                x_west= 2

            if   self.ui.comboBox_17.currentText()== 'Vacuum Flux':
                y_north= 0
            elif self.ui.comboBox_17.currentText()== 'Vacuum Current':
                y_north= 1
            elif self.ui.comboBox_17.currentText()== 'Reflective':
                y_north= 2

            if   self.ui.comboBox_18.currentText()== 'Vacuum Flux':
                y_south= 0
            elif self.ui.comboBox_18.currentText()== 'Vacuum Current':
                y_south= 1
            elif self.ui.comboBox_18.currentText()== 'Reflective':
                y_south= 2

            if   self.ui.comboBox_19.currentText()== 'Vacuum Flux':
                z_top= 0
            elif self.ui.comboBox_19.currentText()== 'Vacuum Current':
                z_top= 1
            elif self.ui.comboBox_19.currentText()== 'Reflective':
                z_top= 2

            if   self.ui.comboBox_20.currentText()== 'Vacuum Flux':
                z_bott= 0
            elif self.ui.comboBox_20.currentText()== 'Vacuum Current':
                z_bott= 1
            elif self.ui.comboBox_20.currentText()== 'Reflective':
                z_bott= 2

            wind1    = Window1(nx,ny,nz)
            wind111  = Window111(nx,ny,nz)
            wind112  = Window112(nz)
            wind114  = Window114(np,nx,ny)
            wind115  = Window115(nx,nz)
            wind9    = Window9(ng,nmat)
            wind10   = Window10(ng,nmat)
            wind11   = Window11(ng,nmat)
            wind12   = Window12(ng,nmat)
            wind13   = Window13(ng,nmat)
            wind14   = Window14(ng,nmat)
            # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Forward"))
            # self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_1), _translate("MainWindow", "Forward"))


            filename = open("app/input/input.json",'w')
            open('app/link/script.dir', "w" ).write(os.path.abspath(os.path.dirname( __file__)) +'/app/input/input.json')
            filename.write('{\n   "Data": \n   { \n      "Parameters": \n      { \n         "ID": 100,')
            filename.write('\n         "Calculation Mode": '+'"'+str(Mode)+'"' +',')
            filename.write('\n         "Number of Energy Groups": '+ str(ng) +',')
            filename.write('\n         "Number of Materials": '+ str(nmat) +',')
            filename.write('\n         "Polynomial Order": '+ str(order)+',')
            filename.write('\n         "Dimensions": '+ str(dim)+',')
            filename.write('\n         "Number of X-Assembly": '+ str(nx) +',')
            filename.write('\n         "Number of Y-Assembly": '+ str(ny) +',')
            filename.write('\n         "Number of Z-Assembly": '+ str(nz) +',')
            filename.write('\n         "X-Assembly Division": '+ str(self.wind1.dx[0]) +',')
            filename.write('\n         "Y-Assembly Division": '+ str(self.wind1.dy[0]) +',')
            filename.write('\n         "Z-Assembly Division": '+ str(self.wind1.dz[0]) +',')
            filename.write('\n         "X-Assembly Size": '+ str(self.wind111.dx[0]) +',')
            filename.write('\n         "Y-Assembly Size": '+ str(self.wind111.dy[0]) +',')
            filename.write('\n         "Z-Assembly Size": '+ str(self.wind111.dz[0]) +',')
            filename.write('\n         "Number of Planar": '+ str(np) +',')
            filename.write('\n         "Planar Assignement to Z": '+ str(self.wind112.zpln[0]))


            filename.write('\n      }, \n      "Materials": \n      [')
            # Boucle sur les Matériaux
            for i in range(nmat):
                filename.write('{ \n         "ID": '+ str(i+1) +', \n        "Name": "Material '+ str(i+1) +'",') 
                filename.write('\n        "Absorption_XS": ' + str(self.wind9.SigA[i][:]) +','
                                   + '\n        "Transport_XS": '+ str(self.wind10.SigTr[i][:])+','
                                   + '\n        "Fission_XS": '+ str(self.wind11.SigF[i][:])+','
                                   + '\n        "Nu*Fission_XS": '+ str(self.wind12.NuSigF[i][:])+','
                                   + '\n        "Chi": '+ str(self.wind13.Chi[i][:])+',')
                filename.write('\n        "Scattering_XS":'+str(self.wind14.SigS[i][:]))
                if i == nmat-1:
                    filename.write('\n       }],')
                else:
                    filename.write('\n       },\n       ')  

            filename.write('\n      "Assemblies": \n      [')
            # Boucle sur Core
            for i in range(np):
                filename.write('{ \n         "ID": '+ str(i+1) +', \n         "Name": "Planar '+ str(i+1) +'",') 
                filename.write('\n         "Assembly": ' + str(self.wind114.core_xy[i][:]))
                if i == np-1:
                    filename.write('\n       }],')
                else:
                    filename.write('\n       },\n       ')  
            filename.write('\n      "XY_Assembly": ' + str(self.wind114.core_xy)+',') 
            filename.write('\n      "Z_Assembly": ' + str(self.wind114.core_z)+',') 

            filename.write('\n      "Boundary Condition": \n      { ')
            filename.write('\n         "X_East": '+ str(x_east)+',')
            filename.write('\n         "X_West": '+ str(x_west)+',')
            filename.write('\n         "Y_North": '+ str(y_north)+',')
            filename.write('\n         "Y_South": '+ str(y_south)+',')
            filename.write('\n         "Z_Top": '+ str(z_top)+',')
            filename.write('\n         "Z_Bottom": '+ str(z_bott))
            filename.write('\n      }')

            # Fin Boucle
            filename.write('\n   } \n}') 
            filename.close() 
            fh = open("app/input/input.json","r")  
            self.ui.textEdit_1.setText(fh.read())    
            fh.close()  
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def UpData_FxSrc(self):
        Geometry_type = open('app/link/script01.py', "r" ).read()
        ng    = self.ui.spinBox_17.value()
        nmat  = self.ui.spinBox_18.value()
        order = self.ui.spinBox_19.value()
        dim   = self.ui.spinBox_20.value()
        nx    = self.ui.spinBox_21.value()
        ny    = self.ui.spinBox_22.value()
        nz    = self.ui.spinBox_23.value()
        np    = self.ui.spinBox_24.value()
        ns    = self.ui.spinBox_25.value()
        npor  = self.ui.spinBox_26.value()
        npox  = self.ui.spinBox_27.value()

        if   ng    == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Energy Groups")
        elif nmat  == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Materials")
        elif order == 0:
            QMessageBox.warning(self, "Warning", "Enter the Number of Polynomial Order")
        elif dim   == 0:
            QMessageBox.warning(self, "Warning", "Enter Dimension Number")
        elif nx    == 0:
            QMessageBox.warning(self, "Warning", "Enter X-Assembly Number")
        elif ny    == 0:
            QMessageBox.warning(self, "Warning", "Enter Y-Assembly Number")
        elif nz    == 0:
            QMessageBox.warning(self, "Warning", "Enter Z-Assembly Number")
        elif np    == 0:
            QMessageBox.warning(self, "Warning", "Enter Planar Number")
        elif dim == 1 and nx < 2 or nz < 2 :
            QMessageBox.warning(self, "Warning", "X-Z-Assembly Number Shall Be at Least Equal 2")
        elif dim == 2   and    nz < 2:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Must Be Equal 2")
        elif dim   == 1 and    np != 1:
            QMessageBox.warning(self, "Warning", "Planar Number Must Be Equal 1")
        elif dim   == 2 and    np != 1:
            QMessageBox.warning(self, "Warning", "Planar Number Must Be Equal 1")
        elif order != 2 and order != 4:
            QMessageBox.warning(self, "Warning", "Polynomial Order Shall Be 2 Or 4")
        elif nx     < 2:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be at Least Equal 2")
        elif ny     < 2:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be at Least Equal 2")
        elif nz     < 2:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be at Least Equal 2")
        elif nx     > 33:
            QMessageBox.warning(self, "Warning", "X-Assembly Number Shall Be Maximum Equal 33")
        elif ny     > 33:
            QMessageBox.warning(self, "Warning", "Y-Assembly Number Shall Be Maximum Equal 33")
        elif nz     > 40:
            QMessageBox.warning(self, "Warning", "Z-Assembly Number Shall Be Maximum Equal 40")
        elif self.ui.comboBox_21.currentText() == '                X-S':
            QMessageBox.warning(self, "Warning", "Choose X-S Option")
        elif self.ui.comboBox_23.currentText() == '       Division/Size':
            QMessageBox.warning(self, "Warning", "Choose Constructive Geometry Option")
        elif self.ui.comboBox_24.currentText() == '        Assignement':
            QMessageBox.warning(self, "Warning", "Choose Assignement Options")
        elif self.ui.comboBox_25.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose East BC Options")
        elif self.ui.comboBox_26.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose West BC Options")
        elif self.ui.comboBox_27.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose North BC Options")
        elif self.ui.comboBox_28.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose South BC Options")
        elif self.ui.comboBox_29.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose Top BC Options")
        elif self.ui.comboBox_30.currentText() == '             BC':
            QMessageBox.warning(self, "Warning", "Choose Bottom BC Options")
        elif self.ui.comboBox_31.currentText() == '    Density/Spectrum':
            QMessageBox.warning(self, "Warning", "Choose Density/Spectrum Options")
        elif self.ui.comboBox_32.currentText() == '     FS Position (xyz)':
            QMessageBox.warning(self, "Warning", "Choose Fixed Source Options")
        # elif self.ui.pushButton_3.isChecked():
            # QMessageBox.warning(self, "Warning", "Choose Z-Planar Option")
        elif   ns  == 0:
            QMessageBox.warning(self, "Warning", "Enter The Source Number")
        elif npor  == 0:
            QMessageBox.warning(self, "Warning", "Enter Radial Fixed Source Number")
        elif npox  == 0:
            QMessageBox.warning(self, "Warning", "Enter Axial Fixed Source Number")
        # elif ds   < 0 or ds   == 0 :
            # QMessageBox.warning(self, "Warning", "Source Density Shall Be Greater Than Zero")

        else:
            if   self.ui.tabWidget_1.currentIndex()== 0:
                Mode = 'Forward'
            if   self.ui.tabWidget_1.currentIndex()== 1:
                Mode = 'Adjoint'
            if   self.ui.tabWidget_1.currentIndex()== 2:
                Mode = 'Fixed Source'

            if   self.ui.comboBox_25.currentText()== 'Vacuum Flux':
                x_east= 0
            elif self.ui.comboBox_25.currentText()== 'Vacuum Current':
                x_east= 1
            elif self.ui.comboBox_25.currentText()== 'Reflective':
                x_east= 2

            if   self.ui.comboBox_26.currentText()== 'Vacuum Flux':
                x_west= 0
            elif self.ui.comboBox_26.currentText()== 'Vacuum Current':
                x_west= 1
            elif self.ui.comboBox_26.currentText()== 'Reflective':
                x_west= 2

            if   self.ui.comboBox_27.currentText()== 'Vacuum Flux':
                y_north= 0
            elif self.ui.comboBox_27.currentText()== 'Vacuum Current':
                y_north= 1
            elif self.ui.comboBox_27.currentText()== 'Reflective':
                y_north= 2

            if   self.ui.comboBox_28.currentText()== 'Vacuum Flux':
                y_south= 0
            elif self.ui.comboBox_28.currentText()== 'Vacuum Current':
                y_south= 1
            elif self.ui.comboBox_28.currentText()== 'Reflective':
                y_south= 2

            if   self.ui.comboBox_29.currentText()== 'Vacuum Flux':
                z_top= 0
            elif self.ui.comboBox_29.currentText()== 'Vacuum Current':
                z_top= 1
            elif self.ui.comboBox_29.currentText()== 'Reflective':
                z_top= 2

            if   self.ui.comboBox_30.currentText()== 'Vacuum Flux':
                z_bott= 0
            elif self.ui.comboBox_30.currentText()== 'Vacuum Current':
                z_bott= 1
            elif self.ui.comboBox_30.currentText()== 'Reflective':
                z_bott= 2

            wind1    = Window1(nx,ny,nz)
            wind111  = Window111(nx,ny,nz)
            wind112  = Window112(nz)
            wind114  = Window114(np,nx,ny)
            wind115  = Window115(nx,nz)
            wind15   = Window15(ns,npor)
            wind16   = Window16(ng,ns)
            wind18   = Window18(ns)
            wind17   = Window17(npox,ns)
            wind9    = Window9(ng,nmat)
            wind10   = Window10(ng,nmat)
            wind11   = Window11(ng,nmat)
            wind12   = Window12(ng,nmat)
            wind13   = Window13(ng,nmat)
            wind14   = Window14(ng,nmat)
            # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Forward"))
            # self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_1), _translate("MainWindow", "Forward"))

            filename = open("app/input/input.json",'w')
            open('app/link/script.dir', "w" ).write(os.path.abspath(os.path.dirname( __file__)) +'/app/input/input.json')
            filename.write('{\n   "Data": \n   { \n      "Parameters": \n      { \n         "ID": 100,')
            filename.write('\n         "Calculation Mode": '+'"'+str(Mode)+'"' +',')
            filename.write('\n         "Number of Energy Groups": '+ str(ng) +',')
            filename.write('\n         "Number of Materials": '+ str(nmat) +',')
            filename.write('\n         "Polynomial Order": '+ str(order)+',')
            filename.write('\n         "Dimensions": '+ str(dim)+',')
            filename.write('\n         "Number of X-Assembly": '+ str(nx) +',')
            filename.write('\n         "Number of Y-Assembly": '+ str(ny) +',')
            filename.write('\n         "Number of Z-Assembly": '+ str(nz) +',')
            filename.write('\n         "X-Assembly Division": '+ str(self.wind1.dx[0]) +',')
            filename.write('\n         "Y-Assembly Division": '+ str(self.wind1.dy[0]) +',')
            filename.write('\n         "Z-Assembly Division": '+ str(self.wind1.dz[0]) +',')
            filename.write('\n         "X-Assembly Size": '+ str(self.wind111.dx[0]) +',')
            filename.write('\n         "Y-Assembly Size": '+ str(self.wind111.dy[0]) +',')
            filename.write('\n         "Z-Assembly Size": '+ str(self.wind111.dz[0]) +',')
            filename.write('\n         "Number of Planar": '+ str(np) +',')
            filename.write('\n         "Planar Assignement to Z": '+ str(self.wind112.zpln[0]))

            filename.write('\n      }, \n      "Materials": \n      [')
            # Boucle sur les Matériaux
            for i in range(nmat):
                filename.write('{ \n        "ID": '+ str(i+1) +', \n        "Name": "Material '+ str(i+1) +'",') 
                filename.write('\n        "Absorption_XS": ' + str(self.wind9.SigA[i][:]) +','
                             + '\n        "Transport_XS": '+ str(self.wind10.SigTr[i][:])+','
                             + '\n        "Fission_XS": '+ str(self.wind11.SigF[i][:])+','
                             + '\n        "Nu*Fission_XS": '+ str(self.wind12.NuSigF[i][:])+','
                             + '\n        "Chi": '+ str(self.wind13.Chi[i][:])+',')
                filename.write('\n        "Scattering_XS":'+str(self.wind14.SigS[i][:]))
                if i == nmat-1:
                    filename.write('\n       }],')
                else:
                    filename.write('\n       },\n       ')  

            filename.write('\n      "Assemblies": \n      [')
            # Boucle sur Core
            for i in range(np):
                filename.write('{ \n        "ID": '+ str(i+1) +', \n        "Name": "Planar '+ str(i+1) +'",') 
                filename.write('\n         "Assembly": ' + str(self.wind114.core_xy[i][:]))
                if i == np-1:
                    filename.write('\n       }],')
                else:
                    filename.write('\n       },\n       ')  
            filename.write('\n      "XY_Assembly": ' + str(self.wind114.core_xy)+',') 
            filename.write('\n      "Z_Assembly": ' + str(self.wind1115.core_z)+',') 

            filename.write('\n      "Boundary Condition": \n      { ')
            filename.write('\n         "X_East": '+ str(x_east)+',')
            filename.write('\n         "X_West": '+ str(x_west)+',')
            filename.write('\n         "Y_North": '+ str(y_north)+',')
            filename.write('\n         "Y_South": '+ str(y_south)+',')
            filename.write('\n         "Z_Top": '+ str(z_top)+',')
            filename.write('\n         "Z_Bottom": '+ str(z_bott))
            filename.write('\n      },')

            filename.write('\n      "Fixed Source Parameters": \n      { ')
            filename.write('\n         "Source Number": '+ str(ns) +',')
            filename.write('\n         "Radial FS Number": '+ str(npor) +',')
            filename.write('\n         "Axial FS Number": '+ str(npox) +',')

            filename.write('\n      "Source Parameters": \n      [')
            # Boucle sur le spectre des sources
            for i in range(ns):
                filename.write('{ \n        "ID": '+ str(i+1) +', \n        "Name": "Source '+ str(i+1) +'",') 
                filename.write('\n        "Source Density": ' + str(self.wind18.ds[i]) +','
                             + '\n        "Source Energy Spectrum": ' + str(self.wind16.sps[i][:])  +','
                             + '\n        "Radial FS Position (x)": ' + str(self.wind15.xpos[i][:]) +','
                             + '\n        "Radial FS Position (y)": ' + str(self.wind15.ypos[i][:]) +','
                             + '\n        "Axial FS Position":'+str(self.wind17.zpos[i][:]))
                if i == ns-1:
                    filename.write('\n       }]')
                else:
                    filename.write('\n       },\n       ')  
            filename.write('\n      }')

            # Fin Boucle
            filename.write('\n   } \n}') 
            filename.close() 
            fh = open("app/input/input.json","r")  
            self.ui.textEdit_1.setText(fh.read())    
            fh.close()  
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    # def CloseFile(self):
        # if self.ui.textEdit_1.toPlainText() == "":
            # pass
        # else:
            # reply = QMessageBox.question(self,"", "Are you sure you want to close this file ?", QMessageBox.Yes | QMessageBox.No)
            # if reply == QMessageBox.Yes:
                # self.ui.textEdit_1.clear()
                # self.setWindowTitle(self.title)
                # self.isFileCreate = True
                # self.isFileOpen = False
            # else:
                # pass
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    def cursorPosition(self):
        cursor = self.ui.textEdit_1.textCursor()

        # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()
        # self.statusbar().showMessage("Line: {} | Column: {} --> Input".format(line,col))

    def cursorPosition_2(self):
        cursor = self.ui.textEdit_2.textCursor()
        # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()
        # self.statusbar().showMessage("Line: {} | Column: {} --> Output".format(line,col))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def NewFile(self):
        self.isFileCreate = True
        self.CloseFile()
        self.ui.textEdit_1.show()
    def openFile(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self,'Open File', "~", "*.json")[0]
        open('app/link/script.dir', "w" ).write(str(self.filename))
        if self.filename != "":
            self.isFileOpen = True
            file = open(self.filename,"r")
            self.setWindowTitle(self.title + ':' + self.filename)
            self.ui.textEdit_1.show()
            self.ui.textEdit_1.setText(file.read())
            file.close()
    def About(self):
        QMessageBox.about(self, "About OpenNode",
                "<center> Python GUI Programming Using Qt <center>\n \n" 
                "<center> This project was developed by <center>\n"
                "<center> Hicham Satti & Otman El-Hajjaji. <center>\n"
                "<center> Laboratory of Radiation & Nuclear Systems, <center>\n"
                                  " Department of Physics\n,  <center>\n"
                "<center> Abdelmalek Essaadi University, Faculty of Sciences,<center>\n"
                                  " Tetouan / Morocco. <center>")
    def Help(self):
        QMessageBox.about(self, "OpenNode",
                "<center> For Help Contact Us: <center>\n \n \n" 
                "<center> hsatti@uae.ac.ma  &  oelhajjaji@uae.ac.ma <center>")
    def SaveFile(self):
        if self.isFileOpen == False or self.isFileCreate == False:
            pass
        if self.isFileOpen == True:
            file = open(self.filename,"w")
            self.setWindowTitle(self.title + ':' + self.filename)
            file.write(self.ui.textEdit_1.toPlainText())
            file.close()
            self.ui.statusbar.showMessage(self.parseFileName() + " has been saved " + " at " +
                                          time.strftime('%d/%m/%y %H:%M', time.localtime()), 4600)
        elif self.isFileCreate == True:
            self.isFileOpen = True
            self.filename = QtWidgets.QFileDialog.getSaveFileName(self,'Save File', "data.json", "*.json")[0]
            if self.filename != "":
                file = open(self.filename,"w")
                self.setWindowTitle(self.title + ':' + self.filename)
                file.write(self.ui.textEdit_1.toPlainText())
                file.close()
                self.ui.statusbar.showMessage(self.parseFileName()  + " has been saved " + " at " +
                                              time.strftime('%d/%m/%y %H:%M', time.localtime()), 4600)
        else:
            pass
    def parseFileName(self):
        filename = self.filename.split("/")
        self.fname = filename[-1]
        return self.fname        
    def Save_AsFile(self):
        self.filename = QtWidgets.QFileDialog.getSaveFileName(self,'Save as File', "data.json", "*.json")[0]
        if self.filename != "":
            file = open(self.filename,"w")
            self.setWindowTitle(self.title + ':' + self.filename)
            file.write(self.ui.textEdit_1.toPlainText())
            file.close()
            self.ui.statusbar.showMessage(self.parseFileName()  + " Has Been Saved " + " at " +
                                          time.strftime('%d/%m/%y %H:%M', time.localtime()), 4600)
        else:
            pass
    def Quit(self):
        """Generate 'question' dialog on clicking 'X' button in title bar.
        Reimplement the closeEvent() event handler to include a 'Question'
        dialog with options on how to proceed - Save, Close, Cancel buttons
        """
        reply = QMessageBox.question(self, "Message",
            "Are you Sure you Want to Quit? Any Unsaved Work will be Lost.", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            qapp.quit()
        else:
            pass


    def currentCharFormatChanged(self, format):
        self.fontChanged(format.font())
        self.colorChanged(format.foreground().color())

    def CloseFile(self):
        if self.ui.textEdit_1.toPlainText() == "":
            pass
        else:
            reply = QMessageBox.question(self,"", "Are you Sure you Want to Close this File?, Any Unsaved Work will be Lost.", QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
                QMessageBox.Save)
            if reply == QMessageBox.Save:
                # self.ui.actionSave.triggered.connect(lambda:self.SaveFile())
                self.ui.textEdit_1.clear()
                self.setWindowTitle(self.title)
                self.isFileCreate = True
                self.isFileOpen = False
            elif reply == QMessageBox.Close:
                self.ui.textEdit_1.clear()
            elif reply == QMessageBox.Cancel:
                pass

    def keyPressEvent(self, event):
        """Close application from escape key.

        results in QMessageBox dialog from closeEvent, good but how/why?
        """
        if event.key() == Qt.Key_Escape:
            self.close()


    # def Find(self):

    def initUI(self):
        # QProcess object for external app
        self.process = QtCore.QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        self.process.readyReadStandardOutput.connect(self.stdoutReady)
        self.process.readyReadStandardError.connect(self.stderrReady)

    def Compile(self):
        """exécuté lors du clic sur le bouton
        """
        #print ('Starting process')
        # self.process.start('python', ['app/Compile.py'])
        a = None
        Test = None
        M00 = open('app/link/script00.py', "r" ).read() 

        if M00 == 'NEM':
                cmd= 'f2py -c app/Sources/NEM.f90 -m NEM'
                proc = Popen( shlex.split(cmd), stdout=PIPE, encoding = 'utf8') 
                
                if os.path.exists('app/NEM.pyd'):
                    os.remove('app/NEM.pyd')

                for line in iter(proc.stdout.readline, b''):
                    if type(line) != str or line == '' and proc.poll() != None: 
                        break
                        
                    elif type(line) == str and len(line) > 6:
                        Test = str(a)
                        print (line),
                proc.communicate()     
            
                if os.path.exists('NEM.cp38-win_amd64.pyd'):
                    os.rename('NEM.cp38-win_amd64.pyd', 'NEM.pyd')
                shutil.move('NEM.pyd', 'app')

                if  Test == str(a):
                    QMessageBox.information(self,"Information","Compiling Case Finished")
                else:
                    QMessageBox.critical(self,"Critical","Check Error")                    
        else:
            QMessageBox.warning(self,"Warning","Select the Calculation Method")

    def Run(self):
        self.process.start('python', ['Main.py'])

    def Comp_Geo(self): 
        a = None
        Test = None
        M00 = open('app/link/script00.py', "r" ).read() 
        Drct = open(os.getcwd()+'/app/link/script.dir', "r" ).read()
        FileName = (Path(Drct).stem)

        if M00 == 'NEM':
                cmd= 'blender -b -P app/3D-Graphic.py'
                proc = Popen( shlex.split(cmd), stdout=PIPE, encoding = 'utf8') 
                
                if os.path.exists('app/Output/'+FileName+'.blend'):
                    os.remove('app/Output/'+FileName+'.blend')
                if os.path.exists('app/Output/'+FileName+'.blend1'):
                    os.remove('app/Output/'+FileName+'.blend1')

                for line in iter(proc.stdout.readline, b''):
                    if type(line) != str or line == '' and proc.poll() != None: 
                        break
                        
                    elif type(line) == str and len(line) > 6:
                        Test = str(a)
                        print (line),
                proc.communicate()     

                shutil.move(FileName+'.blend', 'app/Output')
                if os.path.exists(FileName+'.blend1'):
                    shutil.move(FileName+'.blend1', 'app/Output')
                
                if  Test == str(a):
                    QMessageBox.information(self,"Information","Compiling Case Finished")
                else:
                    QMessageBox.critical(self,"Critical","Check Error")                    
        else:
            QMessageBox.warning(self,"Warning","Select the Calculation Method")

    def Run_Geo(self):
        Drct = open(os.getcwd()+'/app/link/script.dir', "r" ).read()
        FileName = (Path(Drct).stem)

        self.process.start('blender', ['app/Output/'+FileName+'.blend'])

    # def Comp_Geo(self):
        # self.process.start('python', ['app/Compile_3D.py'])
        
    def Progress1(self):
        count = 0
        while count < 100 :
            # self.completed += 0.00001
            count += 1
            time.sleep(0.001)
            self.pbar1.setValue(count)
    def Progress2(self):
        count = 0
        while count < 100 :
            # self.completed += 0.00001
            count += 1
            time.sleep(0.1)
            self.pbar2.setValue(count)
    def Progress3(self):
        count = 0
        while count < 100 :
            # self.completed += 0.00001
            count += 1
            time.sleep(0.001)
            self.pbar3.setValue(count)
    def Progress4(self):
        count = 0
        while count < 100 :
            # self.completed += 0.00001
            count += 1
            time.sleep(0.001)
            self.pbar4.setValue(count)
    def Progress5(self):
        count = 0
        while count < 100 :
            # self.completed += 0.00001
            count += 1
            time.sleep(0.001)
            self.pbar5.setValue(count)
    def Progress6(self):
        count = 0
        while count < 100 :
            # self.completed += 0.00001
            count += 1
            time.sleep(0.001)
            self.pbar6.setValue(count)

    def stdoutReady(self):
        text = bytearray(self.process.readAllStandardOutput())
        text = text.decode("ascii")
        self.append_text(text)

    def stderrReady(self):
        text = bytearray(self.process.readAllStandardError())
        text = text.decode("ascii")
        self.append_text(text)

    def append(self, text):
        cursor = self.ui.textEdit_2.textCursor()
        cursor.insertText(text)
        self.ui.textEdit_2.ensureCursorVisible()

    def append_text(self,text):
        cursor = self.ui.textEdit_2.textCursor()
        cursor.insertText(text)
        self.ui.textEdit_2.ensureCursorVisible()

    def normalOutputWritten(self,text):
        cursor = self.ui.textEdit_2.textCursor()
        cursor.insertText(text)

if __name__ == '__main__': 
    qapp = QApplication(sys.argv) 
    app = Application(u'OpenNode')
    app.show()
    sys.exit(qapp.exec_())
                
# if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())