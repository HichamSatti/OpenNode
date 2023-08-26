# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1217, 775)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Prefix/Radiation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMessageBox{\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"    font: 10pt \"Comic Sans MS\";\n"
"    border-color: rgb(92, 143, 143);\n"
"border-radius:5px\n"
"}\n"
"\n"
"QMainWindow{\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color:rgb(207, 255, 255);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"/* HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {\n"
"    background-color:rgb(255, 114, 116);\n"
"    min-height: 30px;\n"
"    margin: 0px 0 0px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN TOP - SCROLLBAR*/\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    border-top-left-radius:7px;\n"
"    border-top-right-radius:7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN BOTTOM - SCROLLBAR*/\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    border-bottom-left-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"\n"
"/*RESET ARROW*/\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     border: 2px grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"    background-color:rgb(207, 255, 255) ;\n"
" }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"/* --------------------------  */\n"
"\n"
"/* HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none ;\n"
"    background-color:rgb(207, 255, 255);\n"
"    width: 14px;\n"
"    height: 15px;\n"
"    margin: 0 15px 0 15px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color:rgb(255, 114, 116);\n"
"    min-height: 30px;\n"
"    min-width:20px;\n"
"    margin: 0 0px 0 0px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN LEFT - SCROLLBAR*/\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    width: 14px;\n"
"    border-top-left-radius:7px;\n"
"    border-bottom-left-radius:7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN RIGHT - SCROLLBAR*/\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    width: 14px;\n"
"    border-top-right-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*RESET ARROW*/\n"
" QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"     border: 2px grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"    background-color:rgb(207, 255, 255) ;\n"
" }\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
" }\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 3px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(255, 114, 116);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"\n"
"}\n"
"QCheckBox::indicator:checked:hover {\n"
"    border-color:qlineargradient(spread:pad, x1:0.603, y1:0.914773, x2:0.221591, y2:0.222, stop:0.323864 rgba(238, 238, 105, 255), stop:0.926136 rgba(244, 244, 160, 255));\n"
"    background-color:qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QCheckBox::indicator:checked:pressed {\n"
"    background-color: rgb(255, 196, 197);\n"
"    border-color:rgb(255, 166, 168);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border-color:qlineargradient(spread:pad, x1:0.603, y1:0.914773, x2:0.221591, y2:0.222, stop:0.323864 rgba(238, 238, 105, 255), stop:0.926136 rgba(244, 244, 160, 255));\n"
"    background-color:qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    background-color: rgb(255, 196, 197);\n"
"    border-color:rgb(255, 166, 168);\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid rgb(92, 143, 143);\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    border-style: outset;\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"}\n"
"QComboBox:editable {\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox::item:selected {\n"
"background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.369, y2:0.142409, stop:0.323864 rgba(255, 200, 201, 255), stop:0.926136 rgba(255, 234, 234, 255));\n"
"    border-radius:5px;}\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background-color: qlineargradient(spread:pad, x1:0.460318, y1:0, x2:0.466, y2:0.806818, stop:0 rgba(95, 176, 176, 255), stop:1 rgba(172, 214, 214, 255));\n"
"}\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background-color: qlineargradient(spread:pad, x1:0.603, y1:0.914773, x2:0.221591, y2:0.222, stop:0.323864 rgba(238, 238, 105, 255), stop:0.926136 rgba(244, 244, 160, 255));\n"
"}\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;}\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;}\n"
"QComboBox:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QComboBox:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QComboBox::separator {\n"
"    height: 1px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.505591, y2:1, stop:0.323864 rgba(242, 108, 110, 255), stop:0.926136 rgba(251, 207, 208, 255));\n"
"    margin-left: 18px;\n"
"    margin-right: 25px;\n"
"    border-radius:5px;\n"
"}\n"
"QGroupBox {\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"    border: 2px solid rgb(92, 143, 143);\n"
"    border-radius: 10px;}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: yellow;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"QMenu {\n"
"background-color: qlineargradient(spread:pad, x1:0.763, y1:0.284091, x2:0.817, y2:0.931682, stop:0.323864 rgba(255, 234, 234, 255), stop:0.926136 rgba(255, 243, 243, 255));\n"
"    margin: 1px; /* some spacing around the menu */\n"
"    font: 75 10pt \"Comic Sans MS\";\n"
"    border-radius:5px;}\n"
"QMenu::item {\n"
"    padding: 2px 25px 2px 20px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"    border-radius:5px;}\n"
"QMenu::item:selected {\n"
"    background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.380364, y2:0, stop:0.323864 rgba(255, 185, 186, 255), stop:0.926136 rgba(255, 221, 222, 255));\n"
"    border-radius:5px;}\n"
"QMenu::icon:checked { /* appearance of a \'checked\' icon */\n"
"    background: gray;\n"
"    border: 1px inset rgb(92, 143, 143);\n"
"    position: absolute;\n"
"    top: 1px;\n"
"    right: 1px;\n"
"    bottom: 1px;\n"
"    left: 1px;\n"
"    border-radius:5px;}\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.460318, y1:0, x2:0.466, y2:0.806818, stop:0 rgba(95, 176, 176, 255), stop:1 rgba(172, 214, 214, 255));\n"
"    margin-left: 18px;\n"
"    margin-right: 25px;\n"
"    border-radius:5px;\n"
"}\n"
"QMenuBar {\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"    spacing: 3px; /* spacing between menu bar items */\n"
"    font: 75 10pt \"Comic Sans MS\";}\n"
"QMenuBar::item {\n"
"    padding: 1px 4px;\n"
"    background: transparent;\n"
"    border-radius: 4px;}\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"    border-radius:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.380364, y2:0, stop:0.323864 rgba(255, 185, 186, 255), stop:0.926136 rgba(255, 221, 222, 255));\n"
"}\n"
"QMenuBar::item:pressed {\n"
"    border-radius:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.633, y1:0, x2:0.760182, y2:0.926, stop:0.323864 rgba(252, 113, 115, 255), stop:0.926136 rgba(255, 174, 177, 255));\n"
"}\n"
"QProgressBar {\n"
"    border: 1px solid rgb(92, 143, 143);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(236, 236, 236, 255));\n"
"    border-style: outset;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color:rgb(255, 114, 116);\n"
"    border-radius: 3px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.460318, y1:0, x2:0.466, y2:0.806818, stop:0 rgba(95, 176, 176, 255), stop:1 rgba(172, 214, 214, 255));\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(92, 143, 143);\n"
"    font: 10pt \"Comic Sans MS\";\n"
"    min-width: 3em;\n"
"    padding: 6px;}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.603, y1:0.914773, x2:0.221591, y2:0.222, stop:0.323864 rgba(238, 238, 105, 255), stop:0.926136 rgba(244, 244, 160, 255));\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 3px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0.633, y1:0.829955, x2:0.357, y2:0.0225909, stop:0.323864 rgba(252, 113, 115, 255), stop:0.926136 rgba(255, 174, 177, 255));\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"QRadioButton::indicator:checked:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.211682, y1:0.057, x2:0.597, y2:0.989, stop:0.323864 rgba(255, 162, 163, 255), stop:0.926136 rgba(255, 214, 215, 255));\n"
"    border-color:rgb(255, 114, 116);\n"
"}\n"
"QRadioButton::indicator:checked:pressed {\n"
"    border-color:rgb(238, 232, 142);\n"
"    background-color:qlineargradient(spread:pad, x1:0.364409, y1:0.051, x2:0.550773, y2:1, stop:0.323864 rgba(255, 255, 165, 255), stop:0.926136 rgba(255, 255, 214, 255))\n"
"}\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border-color:rgb(238, 232, 142);\n"
"    background-color:qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.511, y2:0, stop:0.323864 rgba(255, 255, 165, 255), stop:0.926136 rgba(255, 255, 214, 255));\n"
"}\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.380364, y2:0, stop:0.323864 rgba(255, 185, 186, 255), stop:0.926136 rgba(255, 221, 222, 255));\n"
"    border-color:rgb(255, 114, 116);\n"
"}\n"
"\n"
"QSpinBox{\n"
"    border: 1px solid rgb(92, 143, 143);\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 2em;\n"
"  }\n"
"QSpinBox:editable {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"    selection-background-color: rgb(255, 255, 127);\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"QSpinBox:!editable, QSpinBox::drop-down:editable {\n"
"    background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(236, 236, 236, 255));\n"
"}\n"
"QSpinBox:!editable:on, QSpinBox::drop-down:editable:on {\n"
"    background: white;\n"
"\n"
"}\n"
"QSpinBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"}\n"
"QSpinBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"QSpinBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"}\n"
"QSpinBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"    background-color:rgb(255, 255, 113);\n"
"    border-radius: 5px;\n"
"}\n"
"QSpinBox::up-button:pressed{\n"
"    background-color:rgb(238, 238, 114);\n"
"    border-radius: 5px;\n"
"}\n"
"QSpinBox::down-button:hover{\n"
"    background-color:rgb(255, 255, 113);\n"
"    border-radius: 5px;\n"
"}\n"
"QSpinBox::down-button:pressed{\n"
"    background-color:rgb(238, 238, 114);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0 rgba(255, 114, 116, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    margin-left: 5px; /* make non-selected tabs look smaller */\n"
"    margin-right: 5px; /* make non-selected tabs look smaller */\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"background-color: qlineargradient(spread:pad, x1:0.460318, y1:0, x2:0.466, y2:0.806818, stop:0 rgba(95, 176, 176, 255), stop:1 rgba(172, 214, 214, 255));\n"
"    border: 2px solid rgb(92, 143, 143);\n"
"    border-bottom-color: rgb(172, 214, 214); /* same as the pane color */\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    min-width: 10ex;\n"
"    padding: 3px;\n"
"    border-style: outset;\n"
"\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0.429545, y1:0, x2:0.449682, y2:1, stop:0 rgba(192, 236, 236, 255), stop:1 rgba(239, 250, 250, 255));\n"
"}\n"
"QTabBar::tab:selected {\n"
"    border: 2px solid rgb(95, 176, 200);\n"
"    border-style: outset;\n"
"    border-bottom-color:  qlineargradient(spread:pad, x1:0.477682, y1:0.409, x2:0.4715, y2:0, stop:0 rgba(255, 114, 116, 255), stop:1 rgba(255, 255, 255, 255)); /* same as pane color */}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */}\n"
"\n"
"QTextEdit{\n"
"    border: 1px solid rgb(92, 143, 143);\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    background-color: white;\n"
"    selection-background-color: rgb(255, 255, 113);\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QToolBar {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(207, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"QToolButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.380364, y2:0, stop:0.323864 rgba(255, 185, 186, 255), stop:0.926136 rgba(255, 221, 222, 255));\n"
"}\n"
"QToolButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.633, y1:0, x2:0.760182, y2:0.926, stop:0.323864 rgba(252, 113, 115, 255), stop:0.926136 rgba(255, 174, 177, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.523, 0.0227273, 0.534, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.323864, QtGui.QColor(255, 255, 217))
        gradient.setColorAt(0.926136, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.523, 0.0227273, 0.534, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.323864, QtGui.QColor(255, 255, 217))
        gradient.setColorAt(0.926136, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.523, 0.0227273, 0.534, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.323864, QtGui.QColor(255, 255, 217))
        gradient.setColorAt(0.926136, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.523, 0.0227273, 0.534, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.323864, QtGui.QColor(255, 255, 217))
        gradient.setColorAt(0.926136, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.523, 0.0227273, 0.534, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.323864, QtGui.QColor(255, 255, 217))
        gradient.setColorAt(0.926136, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.523, 0.0227273, 0.534, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.323864, QtGui.QColor(255, 255, 217))
        gradient.setColorAt(0.926136, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.523, 0.0227273, 0.534, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.323864, QtGui.QColor(255, 255, 217))
        gradient.setColorAt(0.926136, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.523, 0.0227273, 0.534, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.323864, QtGui.QColor(255, 255, 217))
        gradient.setColorAt(0.926136, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.523, 0.0227273, 0.534, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.323864, QtGui.QColor(255, 255, 217))
        gradient.setColorAt(0.926136, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.scrollArea.setPalette(palette)
        self.scrollArea.setStyleSheet("QWidget  {\n"
"        background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"    }\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color:rgb(207, 255, 255);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"/* HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {\n"
"    background-color:rgb(255, 114, 116);\n"
"    min-height: 30px;\n"
"    margin: 0px 0 0px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN TOP - SCROLLBAR*/\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    border-top-left-radius:7px;\n"
"    border-top-right-radius:7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN BOTTOM - SCROLLBAR*/\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    border-bottom-left-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"\n"
"/*RESET ARROW*/\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     border: 2px grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"    background-color:rgb(207, 255, 255) ;\n"
" }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"/* --------------------------  */\n"
"\n"
"/* HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none ;\n"
"    background-color:rgb(207, 255, 255);\n"
"    width: 14px;\n"
"    height: 15px;\n"
"    margin: 0 15px 0 15px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color:rgb(255, 114, 116);\n"
"    min-height: 30px;\n"
"    min-width:20px;\n"
"    margin: 0 0px 0 0px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN LEFT - SCROLLBAR*/\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    width: 14px;\n"
"    border-top-left-radius:7px;\n"
"    border-bottom-left-radius:7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN RIGHT - SCROLLBAR*/\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    width: 14px;\n"
"    border-top-right-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*RESET ARROW*/\n"
" QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"     border: 2px grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"    background-color:rgb(207, 255, 255) ;\n"
" }\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
" }")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-383, 0, 1568, 756))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(1550, 738))
        self.frame.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame.setBaseSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox_1 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_1.setGeometry(QtCore.QRect(0, 0, 631, 734))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_1.setFont(font)
        self.groupBox_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_1.setStyleSheet("QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 3px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0.633, y1:0.829955, x2:0.357, y2:0.0225909, stop:0.323864 rgba(252, 113, 115, 255), stop:0.926136 rgba(255, 174, 177, 255));\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"QCheckBox::indicator:checked:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.211682, y1:0.057, x2:0.597, y2:0.989, stop:0.323864 rgba(255, 162, 163, 255), stop:0.926136 rgba(255, 214, 215, 255));\n"
"    border-color:rgb(255, 114, 116);\n"
"}\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border-color:rgb(238, 232, 142);\n"
"    background-color:qlineargradient(spread:pad, x1:0.364409, y1:0.051, x2:0.550773, y2:1, stop:0.323864 rgba(255, 255, 165, 255), stop:0.926136 rgba(255, 255, 214, 255))\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border-color:rgb(238, 232, 142);\n"
"    background-color:qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.511, y2:0, stop:0.323864 rgba(255, 255, 165, 255), stop:0.926136 rgba(255, 255, 214, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.380364, y2:0, stop:0.323864 rgba(255, 185, 186, 255), stop:0.926136 rgba(255, 221, 222, 255));\n"
"    border-color:rgb(255, 114, 116);\n"
"}\n"
"/* --------------------------  */\n"
"QComboBox {\n"
"    border: 2px solid rgb(92, 143, 143);\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    border-style: outset;\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"}\n"
"QComboBox:editable {\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox::item:selected {\n"
"background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.369, y2:0.142409, stop:0.323864 rgba(255, 200, 201, 255), stop:0.926136 rgba(255, 234, 234, 255));\n"
"    border-radius:5px;}\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background-color: qlineargradient(spread:pad, x1:0.460318, y1:0, x2:0.466, y2:0.806818, stop:0 rgba(95, 176, 176, 255), stop:1 rgba(172, 214, 214, 255));\n"
"}\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background-color: qlineargradient(spread:pad, x1:0.603, y1:0.914773, x2:0.221591, y2:0.222, stop:0.323864 rgba(238, 238, 105, 255), stop:0.926136 rgba(244, 244, 160, 255));\n"
"}\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;}\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;}\n"
"QComboBox:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QComboBox:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QComboBox::separator {\n"
"    height: 1px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.505591, y2:1, stop:0.323864 rgba(242, 108, 110, 255), stop:0.926136 rgba(251, 207, 208, 255));\n"
"    margin-left: 18px;\n"
"    margin-right: 25px;\n"
"    border-radius:5px;\n"
"}\n"
"/* --------------------------  */\n"
"QGroupBox {\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"    border: 2px solid rgb(92, 143, 143);\n"
"    border-radius: 10px;}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;}\n"
"/* --------------------------  */\n"
"QLabel{\n"
"background-color: transparent\n"
"}\n"
"/* --------------------------  */\n"
"QLine{\n"
"background-color: transparent\n"
"}\n"
"/* --------------------------  */\n"
"\n"
"QFrame[frameShape=\"4\"],\n"
"QFrame[frameShape=\"5\"]\n"
"{\n"
"    border: none;\n"
"    background: qlineargradient(spread:pad, x1:0.633, y1:0, x2:0.760182, y2:0.926, stop:0.323864 rgba(252, 113, 115, 255), stop:0.926136 rgba(255, 174, 177, 255));\n"
"    margin:9px\n"
"}\n"
"/* --------------------------  */\n"
"QMainWindow{\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"}\n"
"/* --------------------------  */\n"
"QMenu {\n"
"background-color: qlineargradient(spread:pad, x1:0.763, y1:0.284091, x2:0.817, y2:0.931682, stop:0.323864 rgba(255, 234, 234, 255), stop:0.926136 rgba(255, 243, 243, 255));\n"
"    margin: 1px; /* some spacing around the menu */\n"
"    font: 75 10pt \"Comic Sans MS\";\n"
"    border-radius:5px;}\n"
"QMenu::item {\n"
"    padding: 2px 25px 2px 20px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"    border-radius:5px;}\n"
"QMenu::item:selected {\n"
"    background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.380364, y2:0, stop:0.323864 rgba(255, 185, 186, 255), stop:0.926136 rgba(255, 221, 222, 255));\n"
"    border-radius:5px;}\n"
"QMenu::icon:checked { /* appearance of a \'checked\' icon */\n"
"    background: gray;\n"
"    border: 1px inset rgb(92, 143, 143);\n"
"    position: absolute;\n"
"    top: 1px;\n"
"    right: 1px;\n"
"    bottom: 1px;\n"
"    left: 1px;\n"
"    border-radius:5px;}\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.460318, y1:0, x2:0.466, y2:0.806818, stop:0 rgba(95, 176, 176, 255), stop:1 rgba(172, 214, 214, 255));\n"
"    margin-left: 18px;\n"
"    margin-right: 25px;\n"
"    border-radius:5px;\n"
"}\n"
"QMenuBar {\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"    spacing: 3px; /* spacing between menu bar items */\n"
"    font: 75 10pt \"Comic Sans MS\";}\n"
"QMenuBar::item {\n"
"    padding: 1px 4px;\n"
"    background: transparent;\n"
"    border-radius: 4px;}\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"    border-radius:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.380364, y2:0, stop:0.323864 rgba(255, 185, 186, 255), stop:0.926136 rgba(255, 221, 222, 255));\n"
"}\n"
"QMenuBar::item:pressed {\n"
"    border-radius:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.633, y1:0, x2:0.760182, y2:0.926, stop:0.323864 rgba(252, 113, 115, 255), stop:0.926136 rgba(255, 174, 177, 255));\n"
"}\n"
"/* --------------------------  */\n"
"QProgressBar {\n"
"    border: 1px solid rgb(92, 143, 143);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(236, 236, 236, 255));\n"
"    border-style: outset;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color:rgb(255, 114, 116);\n"
"    border-radius: 3px;\n"
"    margin: 0.5px;\n"
"}\n"
"/* --------------------------  */\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.460318, y1:0, x2:0.466, y2:0.806818, stop:0 rgba(95, 176, 176, 255), stop:1 rgba(172, 214, 214, 255));\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(92, 143, 143);\n"
"    font: 10pt \"Comic Sans MS\";\n"
"    min-width: 3em;\n"
"    padding: 6px;}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.603, y1:0.914773, x2:0.221591, y2:0.222, stop:0.323864 rgba(238, 238, 105, 255), stop:0.926136 rgba(244, 244, 160, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.603, y1:0.914773, x2:0.221591, y2:0.222, stop:0.323864 rgba(238, 238, 105, 255), stop:0.926136 rgba(244, 244, 160, 255));\n"
"border-color: rgb(133, 217, 217);\n"
"}\n"
"/* --------------------------  */\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 3px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0.633, y1:0.829955, x2:0.357, y2:0.0225909, stop:0.323864 rgba(252, 113, 115, 255), stop:0.926136 rgba(255, 174, 177, 255));\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"QRadioButton::indicator:checked:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.211682, y1:0.057, x2:0.597, y2:0.989, stop:0.323864 rgba(255, 162, 163, 255), stop:0.926136 rgba(255, 214, 215, 255));\n"
"    border-color:rgb(255, 114, 116);\n"
"}\n"
"QRadioButton::indicator:checked:pressed {\n"
"    border-color:rgb(238, 232, 142);\n"
"    background-color:qlineargradient(spread:pad, x1:0.364409, y1:0.051, x2:0.550773, y2:1, stop:0.323864 rgba(255, 255, 165, 255), stop:0.926136 rgba(255, 255, 214, 255))\n"
"}\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border-color:rgb(238, 232, 142);\n"
"    background-color:qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.511, y2:0, stop:0.323864 rgba(255, 255, 165, 255), stop:0.926136 rgba(255, 255, 214, 255));\n"
"}\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.380364, y2:0, stop:0.323864 rgba(255, 185, 186, 255), stop:0.926136 rgba(255, 221, 222, 255));\n"
"    border-color:rgb(255, 114, 116);\n"
"}\n"
"/* --------------------------  */\n"
"/* VERTICAL SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color:rgb(207, 255, 255);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"/* HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {\n"
"    background-color:rgb(255, 114, 116);\n"
"    min-height: 30px;\n"
"    margin: 0px 0 0px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN TOP - SCROLLBAR*/\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    border-top-left-radius:7px;\n"
"    border-top-right-radius:7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN BOTTOM - SCROLLBAR*/\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    border-bottom-left-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*RESET ARROW*/\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     border: 2px grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"    background-color:rgb(207, 255, 255) ;\n"
" }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"/* --------------------------  */\n"
"/* HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none ;\n"
"    background-color:rgb(207, 255, 255);\n"
"    width: 14px;\n"
"    height: 15px;\n"
"    margin: 0 15px 0 15px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color:rgb(255, 114, 116);\n"
"    min-height: 30px;\n"
"    min-width:20px;\n"
"    margin: 0 0px 0 0px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN LEFT - SCROLLBAR*/\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    width: 14px;\n"
"    border-top-left-radius:7px;\n"
"    border-bottom-left-radius:7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN RIGHT - SCROLLBAR*/\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    width: 14px;\n"
"    border-top-right-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*RESET ARROW*/\n"
" QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"     border: 2px grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"    background-color:rgb(207, 255, 255) ;\n"
" }\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
" }\n"
"/* --------------------------  */\n"
"QSpinBox{\n"
"    border: 1px solid rgb(92, 143, 143);\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 2em;\n"
"  }\n"
"QSpinBox:editable {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"    selection-background-color: rgb(255, 255, 127);\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"QSpinBox:!editable, QSpinBox::drop-down:editable {\n"
"    background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(236, 236, 236, 255));\n"
"}\n"
"QSpinBox:!editable:on, QSpinBox::drop-down:editable:on {\n"
"    background: white;\n"
"\n"
"}\n"
"QSpinBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"}\n"
"QSpinBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"QSpinBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"}\n"
"QSpinBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"    background-color:rgb(255, 255, 113);\n"
"    border-radius: 5px;\n"
"}\n"
"QSpinBox::up-button:pressed{\n"
"    background-color:rgb(238, 238, 114);\n"
"    border-radius: 5px;\n"
"}\n"
"QSpinBox::down-button:hover{\n"
"    background-color:rgb(255, 255, 113);\n"
"    border-radius: 5px;\n"
"}\n"
"QSpinBox::down-button:pressed{\n"
"    background-color:rgb(238, 238, 114);\n"
"    border-radius: 5px;\n"
"}\n"
"/* --------------------------  */\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0 rgba(255, 114, 116, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    margin-left: 5px; /* make non-selected tabs look smaller */\n"
"    margin-right: 5px; /* make non-selected tabs look smaller */\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"background-color: qlineargradient(spread:pad, x1:0.460318, y1:0, x2:0.466, y2:0.806818, stop:0 rgba(95, 176, 176, 255), stop:1 rgba(172, 214, 214, 255));\n"
"    border: 2px solid rgb(92, 143, 143);\n"
"    border-bottom-color: rgb(172, 214, 214); /* same as the pane color */\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    min-width: 10ex;\n"
"    padding: 3px;\n"
"    border-style: outset;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0.429545, y1:0, x2:0.449682, y2:1, stop:0 rgba(192, 236, 236, 255), stop:1 rgba(239, 250, 250, 255));\n"
"}\n"
"QTabBar::tab:selected {\n"
"    border: 2px solid rgb(95, 176, 200);\n"
"    border-style: outset;\n"
"    border-bottom-color:  qlineargradient(spread:pad, x1:0.477682, y1:0.409, x2:0.4715, y2:0, stop:0 rgba(255, 114, 116, 255), stop:1 rgba(255, 255, 255, 255)); /* same as pane color */}\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */}\n"
"/* --------------------------  */\n"
"QTextEdit{\n"
"    border: 1px solid rgb(92, 143, 143);\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 255, 113);\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"/* --------------------------  */\n"
"QToolBar {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(207, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    spacing: 3px; /* spacing between items in the tool bar */}\n"
"\n"
"")
        self.groupBox_1.setObjectName("groupBox_1")
        self.tabWidget_1 = QtWidgets.QTabWidget(self.groupBox_1)
        self.tabWidget_1.setEnabled(True)
        self.tabWidget_1.setGeometry(QtCore.QRect(20, 20, 607, 711))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_1.sizePolicy().hasHeightForWidth())
        self.tabWidget_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget_1.setFont(font)
        self.tabWidget_1.setStyleSheet("")
        self.tabWidget_1.setObjectName("tabWidget_1")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_1 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_1.setGeometry(QtCore.QRect(20, 20, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setStyleSheet("    background-color: transparent;\n"
"")
        self.radioButton_1.setObjectName("radioButton_1")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 70, 597, 451))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_39 = QtWidgets.QLabel(self.groupBox_3)
        self.label_39.setGeometry(QtCore.QRect(30, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.groupBox_3)
        self.label_40.setGeometry(QtCore.QRect(30, 50, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_5.setGeometry(QtCore.QRect(214, 232, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_5.setFont(font)
        self.spinBox_5.setStyleSheet("")
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_6 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_6.setGeometry(QtCore.QRect(214, 256, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_6.setFont(font)
        self.spinBox_6.setObjectName("spinBox_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(192, 180, 103, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(255, 255, 127);\n"
"")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setFrame(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.label_41 = QtWidgets.QLabel(self.groupBox_3)
        self.label_41.setGeometry(QtCore.QRect(30, 220, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.groupBox_3)
        self.label_42.setGeometry(QtCore.QRect(30, 250, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.groupBox_3)
        self.label_43.setGeometry(QtCore.QRect(30, 280, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.groupBox_3)
        self.label_44.setGeometry(QtCore.QRect(30, 300, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.spinBox_8 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_8.setGeometry(QtCore.QRect(214, 306, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_8.setFont(font)
        self.spinBox_8.setObjectName("spinBox_8")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_3.setGeometry(QtCore.QRect(214, 76, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setStyleSheet("")
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_2.setGeometry(QtCore.QRect(214, 51, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setAcceptDrops(False)
        self.spinBox_2.setToolTipDuration(-1)
        self.spinBox_2.setStyleSheet("")
        self.spinBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBox_2.setReadOnly(False)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_1 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_1.setGeometry(QtCore.QRect(214, 26, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_1.setFont(font)
        self.spinBox_1.setStyleSheet("")
        self.spinBox_1.setObjectName("spinBox_1")
        self.spinBox_7 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_7.setGeometry(QtCore.QRect(214, 281, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_7.setFont(font)
        self.spinBox_7.setObjectName("spinBox_7")
        self.line_2 = QtWidgets.QFrame(self.groupBox_3)
        self.line_2.setGeometry(QtCore.QRect(292, 17, 19, 153))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_45 = QtWidgets.QLabel(self.groupBox_3)
        self.label_45.setGeometry(QtCore.QRect(20, 90, 141, 49))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.comboBox_1 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_1.setGeometry(QtCore.QRect(20, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_1.setFont(font)
        self.comboBox_1.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_1.setEditable(False)
        self.comboBox_1.setFrame(True)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_1.setGeometry(QtCore.QRect(204, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.label_46 = QtWidgets.QLabel(self.groupBox_3)
        self.label_46.setGeometry(QtCore.QRect(310, 13, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.groupBox_3)
        self.label_47.setGeometry(QtCore.QRect(320, 37, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.groupBox_3)
        self.label_48.setGeometry(QtCore.QRect(320, 61, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.groupBox_3)
        self.label_49.setGeometry(QtCore.QRect(320, 91, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.groupBox_3)
        self.label_50.setGeometry(QtCore.QRect(320, 108, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.groupBox_3)
        self.label_51.setGeometry(QtCore.QRect(320, 137, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.groupBox_3)
        self.label_52.setGeometry(QtCore.QRect(320, 155, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.line_3 = QtWidgets.QFrame(self.groupBox_3)
        self.line_3.setGeometry(QtCore.QRect(310, 175, 107, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(204, 360, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_54 = QtWidgets.QLabel(self.groupBox_3)
        self.label_54.setGeometry(QtCore.QRect(20, 325, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_4.setGeometry(QtCore.QRect(20, 400, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setFrame(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(204, 400, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_55 = QtWidgets.QLabel(self.groupBox_3)
        self.label_55.setGeometry(QtCore.QRect(30, 170, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.groupBox_3)
        self.label_56.setGeometry(QtCore.QRect(30, 200, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_4.setGeometry(QtCore.QRect(214, 207, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_4.setFont(font)
        self.spinBox_4.setStyleSheet("")
        self.spinBox_4.setSuffix("")
        self.spinBox_4.setPrefix("")
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_57 = QtWidgets.QLabel(self.groupBox_3)
        self.label_57.setGeometry(QtCore.QRect(30, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 360, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setFrame(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_5.setGeometry(QtCore.QRect(410, 44, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setDuplicatesEnabled(False)
        self.comboBox_5.setFrame(True)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_6.setGeometry(QtCore.QRect(410, 68, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));")
        self.comboBox_6.setEditable(False)
        self.comboBox_6.setFrame(True)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_7.setGeometry(QtCore.QRect(410, 92, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));")
        self.comboBox_7.setEditable(False)
        self.comboBox_7.setFrame(True)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_8.setGeometry(QtCore.QRect(410, 115, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));")
        self.comboBox_8.setEditable(False)
        self.comboBox_8.setFrame(True)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_9.setGeometry(QtCore.QRect(410, 139, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_9.setFont(font)
        self.comboBox_9.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));")
        self.comboBox_9.setEditable(False)
        self.comboBox_9.setFrame(True)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_10 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_10.setGeometry(QtCore.QRect(410, 163, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_10.setFont(font)
        self.comboBox_10.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"gridline-color: rgb(85, 255, 0);\n"
"")
        self.comboBox_10.setEditable(False)
        self.comboBox_10.setFrame(True)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(370, 364, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setGeometry(QtCore.QRect(34, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 530, 597, 141))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_7.setGeometry(QtCore.QRect(173, 30, 280, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_8.setGeometry(QtCore.QRect(187, 60, 88, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_7.setGeometry(QtCore.QRect(5, 60, 94, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_36 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_36.setGeometry(QtCore.QRect(20, 20, 114, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_37.setGeometry(QtCore.QRect(150, 20, 114, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_9.setGeometry(QtCore.QRect(101, 60, 84, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setGeometry(QtCore.QRect(6, 30, 163, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_5.setGeometry(QtCore.QRect(9, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_6.setGeometry(QtCore.QRect(86, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.progressBar_1 = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar_1.setGeometry(QtCore.QRect(9, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.progressBar_1.setFont(font)
        self.progressBar_1.setProperty("value", 25)
        self.progressBar_1.setTextVisible(True)
        self.progressBar_1.setInvertedAppearance(False)
        self.progressBar_1.setObjectName("progressBar_1")
        self.progressBar_2 = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar_2.setGeometry(QtCore.QRect(85, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.progressBar_2.setFont(font)
        self.progressBar_2.setProperty("value", 25)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setObjectName("progressBar_2")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_8.setGeometry(QtCore.QRect(457, 30, 134, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_8.setObjectName("groupBox_8")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_10.setGeometry(QtCore.QRect(6, 20, 122, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_11.setGeometry(QtCore.QRect(6, 60, 122, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.line_1 = QtWidgets.QFrame(self.tab_1)
        self.line_1.setGeometry(QtCore.QRect(11, 230, 201, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.line_1.setFont(font)
        self.line_1.setStyleSheet("")
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.tabWidget_1.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_9.setGeometry(QtCore.QRect(0, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_9)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 20, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("    background-color: transparent;\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_10.setGeometry(QtCore.QRect(0, 70, 597, 451))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_58 = QtWidgets.QLabel(self.groupBox_10)
        self.label_58.setGeometry(QtCore.QRect(30, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.groupBox_10)
        self.label_59.setGeometry(QtCore.QRect(30, 50, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.spinBox_13 = QtWidgets.QSpinBox(self.groupBox_10)
        self.spinBox_13.setGeometry(QtCore.QRect(214, 232, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_13.setFont(font)
        self.spinBox_13.setStyleSheet("")
        self.spinBox_13.setObjectName("spinBox_13")
        self.spinBox_14 = QtWidgets.QSpinBox(self.groupBox_10)
        self.spinBox_14.setGeometry(QtCore.QRect(214, 256, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_14.setFont(font)
        self.spinBox_14.setObjectName("spinBox_14")
        self.comboBox_12 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_12.setGeometry(QtCore.QRect(192, 180, 103, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_12.setFont(font)
        self.comboBox_12.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(255, 255, 127);\n"
"")
        self.comboBox_12.setEditable(False)
        self.comboBox_12.setFrame(True)
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.label_60 = QtWidgets.QLabel(self.groupBox_10)
        self.label_60.setGeometry(QtCore.QRect(30, 220, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.groupBox_10)
        self.label_61.setGeometry(QtCore.QRect(30, 250, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.groupBox_10)
        self.label_62.setGeometry(QtCore.QRect(30, 280, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.groupBox_10)
        self.label_63.setGeometry(QtCore.QRect(30, 300, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.spinBox_16 = QtWidgets.QSpinBox(self.groupBox_10)
        self.spinBox_16.setGeometry(QtCore.QRect(214, 306, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_16.setFont(font)
        self.spinBox_16.setObjectName("spinBox_16")
        self.spinBox_11 = QtWidgets.QSpinBox(self.groupBox_10)
        self.spinBox_11.setGeometry(QtCore.QRect(214, 76, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_11.setFont(font)
        self.spinBox_11.setStyleSheet("")
        self.spinBox_11.setObjectName("spinBox_11")
        self.spinBox_10 = QtWidgets.QSpinBox(self.groupBox_10)
        self.spinBox_10.setGeometry(QtCore.QRect(214, 51, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_10.setFont(font)
        self.spinBox_10.setAcceptDrops(False)
        self.spinBox_10.setToolTipDuration(-1)
        self.spinBox_10.setStyleSheet("")
        self.spinBox_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBox_10.setReadOnly(False)
        self.spinBox_10.setObjectName("spinBox_10")
        self.spinBox_9 = QtWidgets.QSpinBox(self.groupBox_10)
        self.spinBox_9.setGeometry(QtCore.QRect(214, 26, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_9.setFont(font)
        self.spinBox_9.setStyleSheet("")
        self.spinBox_9.setObjectName("spinBox_9")
        self.spinBox_15 = QtWidgets.QSpinBox(self.groupBox_10)
        self.spinBox_15.setGeometry(QtCore.QRect(214, 281, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_15.setFont(font)
        self.spinBox_15.setObjectName("spinBox_15")
        self.line_4 = QtWidgets.QFrame(self.groupBox_10)
        self.line_4.setGeometry(QtCore.QRect(292, 17, 19, 153))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.line_4.setFont(font)
        self.line_4.setStyleSheet("")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_64 = QtWidgets.QLabel(self.groupBox_10)
        self.label_64.setGeometry(QtCore.QRect(20, 90, 141, 49))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.comboBox_11 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_11.setGeometry(QtCore.QRect(20, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_11.setFont(font)
        self.comboBox_11.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_11.setEditable(False)
        self.comboBox_11.setFrame(True)
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_12.setGeometry(QtCore.QRect(204, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_65 = QtWidgets.QLabel(self.groupBox_10)
        self.label_65.setGeometry(QtCore.QRect(310, 13, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.groupBox_10)
        self.label_66.setGeometry(QtCore.QRect(320, 37, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.groupBox_10)
        self.label_67.setGeometry(QtCore.QRect(320, 61, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.groupBox_10)
        self.label_68.setGeometry(QtCore.QRect(320, 91, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.groupBox_10)
        self.label_69.setGeometry(QtCore.QRect(320, 108, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.groupBox_10)
        self.label_70.setGeometry(QtCore.QRect(320, 137, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.groupBox_10)
        self.label_71.setGeometry(QtCore.QRect(320, 155, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.line_5 = QtWidgets.QFrame(self.groupBox_10)
        self.line_5.setGeometry(QtCore.QRect(310, 175, 107, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.line_5.setFont(font)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_13.setGeometry(QtCore.QRect(204, 360, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_73 = QtWidgets.QLabel(self.groupBox_10)
        self.label_73.setGeometry(QtCore.QRect(20, 325, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.comboBox_14 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_14.setGeometry(QtCore.QRect(20, 400, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_14.setFont(font)
        self.comboBox_14.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_14.setEditable(False)
        self.comboBox_14.setFrame(True)
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_14.setGeometry(QtCore.QRect(204, 400, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_74 = QtWidgets.QLabel(self.groupBox_10)
        self.label_74.setGeometry(QtCore.QRect(30, 170, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.label_75 = QtWidgets.QLabel(self.groupBox_10)
        self.label_75.setGeometry(QtCore.QRect(30, 200, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.spinBox_12 = QtWidgets.QSpinBox(self.groupBox_10)
        self.spinBox_12.setGeometry(QtCore.QRect(214, 207, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_12.setFont(font)
        self.spinBox_12.setStyleSheet("")
        self.spinBox_12.setSuffix("")
        self.spinBox_12.setPrefix("")
        self.spinBox_12.setObjectName("spinBox_12")
        self.label_76 = QtWidgets.QLabel(self.groupBox_10)
        self.label_76.setGeometry(QtCore.QRect(30, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.comboBox_13 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_13.setGeometry(QtCore.QRect(20, 360, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_13.setFont(font)
        self.comboBox_13.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_13.setEditable(False)
        self.comboBox_13.setFrame(True)
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_15 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_15.setGeometry(QtCore.QRect(410, 44, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_15.setFont(font)
        self.comboBox_15.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_15.setEditable(False)
        self.comboBox_15.setDuplicatesEnabled(False)
        self.comboBox_15.setFrame(True)
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_16 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_16.setGeometry(QtCore.QRect(410, 68, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_16.setFont(font)
        self.comboBox_16.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));")
        self.comboBox_16.setEditable(False)
        self.comboBox_16.setFrame(True)
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_17 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_17.setGeometry(QtCore.QRect(410, 92, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_17.setFont(font)
        self.comboBox_17.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));")
        self.comboBox_17.setEditable(False)
        self.comboBox_17.setFrame(True)
        self.comboBox_17.setObjectName("comboBox_17")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_18 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_18.setGeometry(QtCore.QRect(410, 115, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_18.setFont(font)
        self.comboBox_18.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));")
        self.comboBox_18.setEditable(False)
        self.comboBox_18.setFrame(True)
        self.comboBox_18.setObjectName("comboBox_18")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_19 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_19.setGeometry(QtCore.QRect(410, 139, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_19.setFont(font)
        self.comboBox_19.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));")
        self.comboBox_19.setEditable(False)
        self.comboBox_19.setFrame(True)
        self.comboBox_19.setObjectName("comboBox_19")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_20 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_20.setGeometry(QtCore.QRect(410, 163, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_20.setFont(font)
        self.comboBox_20.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"gridline-color: rgb(85, 255, 0);\n"
"")
        self.comboBox_20.setEditable(False)
        self.comboBox_20.setFrame(True)
        self.comboBox_20.setObjectName("comboBox_20")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.line_6 = QtWidgets.QFrame(self.groupBox_10)
        self.line_6.setGeometry(QtCore.QRect(10, 160, 201, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.line_6.setFont(font)
        self.line_6.setStyleSheet("")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_10)
        self.groupBox_11.setGeometry(QtCore.QRect(370, 364, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_15.setGeometry(QtCore.QRect(34, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_12.setGeometry(QtCore.QRect(0, 530, 597, 141))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_12.setObjectName("groupBox_12")
        self.groupBox_14 = QtWidgets.QGroupBox(self.groupBox_12)
        self.groupBox_14.setGeometry(QtCore.QRect(173, 30, 280, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_14.setFont(font)
        self.groupBox_14.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_14.setObjectName("groupBox_14")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_14)
        self.pushButton_20.setGeometry(QtCore.QRect(101, 60, 84, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_14)
        self.pushButton_19.setGeometry(QtCore.QRect(187, 60, 88, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_14)
        self.pushButton_18.setGeometry(QtCore.QRect(5, 60, 94, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setAutoDefault(False)
        self.pushButton_18.setDefault(False)
        self.pushButton_18.setFlat(False)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_38 = QtWidgets.QPushButton(self.groupBox_14)
        self.pushButton_38.setGeometry(QtCore.QRect(20, 20, 114, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.groupBox_14)
        self.pushButton_39.setGeometry(QtCore.QRect(150, 20, 114, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setObjectName("pushButton_39")
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_12)
        self.groupBox_13.setGeometry(QtCore.QRect(6, 30, 163, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_13.setObjectName("groupBox_13")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_16.setGeometry(QtCore.QRect(9, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_17.setGeometry(QtCore.QRect(86, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.progressBar_3 = QtWidgets.QProgressBar(self.groupBox_13)
        self.progressBar_3.setGeometry(QtCore.QRect(9, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.progressBar_3.setFont(font)
        self.progressBar_3.setProperty("value", 25)
        self.progressBar_3.setTextVisible(True)
        self.progressBar_3.setInvertedAppearance(False)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_4 = QtWidgets.QProgressBar(self.groupBox_13)
        self.progressBar_4.setGeometry(QtCore.QRect(85, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.progressBar_4.setFont(font)
        self.progressBar_4.setProperty("value", 25)
        self.progressBar_4.setTextVisible(True)
        self.progressBar_4.setInvertedAppearance(False)
        self.progressBar_4.setObjectName("progressBar_4")
        self.groupBox_15 = QtWidgets.QGroupBox(self.groupBox_12)
        self.groupBox_15.setGeometry(QtCore.QRect(457, 30, 134, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_15.setObjectName("groupBox_15")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_15)
        self.pushButton_21.setGeometry(QtCore.QRect(6, 20, 122, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_15)
        self.pushButton_22.setGeometry(QtCore.QRect(6, 60, 122, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        self.tabWidget_1.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_16.setGeometry(QtCore.QRect(0, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_16.setFont(font)
        self.groupBox_16.setObjectName("groupBox_16")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_16)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 20, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("    background-color: transparent;\n"
"")
        self.radioButton_3.setObjectName("radioButton_3")
        self.groupBox_17 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_17.setGeometry(QtCore.QRect(0, 70, 597, 451))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_17.setFont(font)
        self.groupBox_17.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_17.setObjectName("groupBox_17")
        self.label_77 = QtWidgets.QLabel(self.groupBox_17)
        self.label_77.setGeometry(QtCore.QRect(30, 20, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_77.setFont(font)
        self.label_77.setObjectName("label_77")
        self.label_78 = QtWidgets.QLabel(self.groupBox_17)
        self.label_78.setGeometry(QtCore.QRect(30, 50, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.spinBox_21 = QtWidgets.QSpinBox(self.groupBox_17)
        self.spinBox_21.setGeometry(QtCore.QRect(214, 232, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_21.setFont(font)
        self.spinBox_21.setStyleSheet("")
        self.spinBox_21.setObjectName("spinBox_21")
        self.spinBox_22 = QtWidgets.QSpinBox(self.groupBox_17)
        self.spinBox_22.setGeometry(QtCore.QRect(214, 256, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_22.setFont(font)
        self.spinBox_22.setObjectName("spinBox_22")
        self.comboBox_22 = QtWidgets.QComboBox(self.groupBox_17)
        self.comboBox_22.setGeometry(QtCore.QRect(192, 180, 103, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_22.setFont(font)
        self.comboBox_22.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(255, 255, 127);\n"
"")
        self.comboBox_22.setEditable(False)
        self.comboBox_22.setFrame(True)
        self.comboBox_22.setObjectName("comboBox_22")
        self.comboBox_22.addItem("")
        self.label_79 = QtWidgets.QLabel(self.groupBox_17)
        self.label_79.setGeometry(QtCore.QRect(30, 220, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(self.groupBox_17)
        self.label_80.setGeometry(QtCore.QRect(30, 250, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.label_81 = QtWidgets.QLabel(self.groupBox_17)
        self.label_81.setGeometry(QtCore.QRect(30, 280, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.label_82 = QtWidgets.QLabel(self.groupBox_17)
        self.label_82.setGeometry(QtCore.QRect(30, 300, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.spinBox_24 = QtWidgets.QSpinBox(self.groupBox_17)
        self.spinBox_24.setGeometry(QtCore.QRect(214, 306, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_24.setFont(font)
        self.spinBox_24.setObjectName("spinBox_24")
        self.spinBox_19 = QtWidgets.QSpinBox(self.groupBox_17)
        self.spinBox_19.setGeometry(QtCore.QRect(214, 76, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_19.setFont(font)
        self.spinBox_19.setStyleSheet("")
        self.spinBox_19.setObjectName("spinBox_19")
        self.spinBox_18 = QtWidgets.QSpinBox(self.groupBox_17)
        self.spinBox_18.setGeometry(QtCore.QRect(214, 51, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_18.setFont(font)
        self.spinBox_18.setAcceptDrops(False)
        self.spinBox_18.setToolTipDuration(-1)
        self.spinBox_18.setStyleSheet("")
        self.spinBox_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBox_18.setReadOnly(False)
        self.spinBox_18.setObjectName("spinBox_18")
        self.spinBox_17 = QtWidgets.QSpinBox(self.groupBox_17)
        self.spinBox_17.setGeometry(QtCore.QRect(214, 26, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_17.setFont(font)
        self.spinBox_17.setStyleSheet("")
        self.spinBox_17.setObjectName("spinBox_17")
        self.spinBox_23 = QtWidgets.QSpinBox(self.groupBox_17)
        self.spinBox_23.setGeometry(QtCore.QRect(214, 281, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_23.setFont(font)
        self.spinBox_23.setObjectName("spinBox_23")
        self.line_7 = QtWidgets.QFrame(self.groupBox_17)
        self.line_7.setGeometry(QtCore.QRect(292, 17, 19, 347))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.line_7.setFont(font)
        self.line_7.setStyleSheet("")
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_83 = QtWidgets.QLabel(self.groupBox_17)
        self.label_83.setGeometry(QtCore.QRect(20, 90, 141, 49))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.comboBox_21 = QtWidgets.QComboBox(self.groupBox_17)
        self.comboBox_21.setGeometry(QtCore.QRect(20, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_21.setFont(font)
        self.comboBox_21.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_21.setEditable(False)
        self.comboBox_21.setFrame(True)
        self.comboBox_21.setObjectName("comboBox_21")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox_17)
        self.pushButton_23.setGeometry(QtCore.QRect(204, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.label_84 = QtWidgets.QLabel(self.groupBox_17)
        self.label_84.setGeometry(QtCore.QRect(310, 13, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.label_85 = QtWidgets.QLabel(self.groupBox_17)
        self.label_85.setGeometry(QtCore.QRect(320, 37, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.label_86 = QtWidgets.QLabel(self.groupBox_17)
        self.label_86.setGeometry(QtCore.QRect(320, 61, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_86.setFont(font)
        self.label_86.setObjectName("label_86")
        self.label_87 = QtWidgets.QLabel(self.groupBox_17)
        self.label_87.setGeometry(QtCore.QRect(320, 91, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_87.setFont(font)
        self.label_87.setObjectName("label_87")
        self.label_88 = QtWidgets.QLabel(self.groupBox_17)
        self.label_88.setGeometry(QtCore.QRect(320, 108, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_88.setFont(font)
        self.label_88.setObjectName("label_88")
        self.label_89 = QtWidgets.QLabel(self.groupBox_17)
        self.label_89.setGeometry(QtCore.QRect(320, 137, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_89.setFont(font)
        self.label_89.setObjectName("label_89")
        self.label_90 = QtWidgets.QLabel(self.groupBox_17)
        self.label_90.setGeometry(QtCore.QRect(320, 155, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_90.setFont(font)
        self.label_90.setObjectName("label_90")
        self.line_8 = QtWidgets.QFrame(self.groupBox_17)
        self.line_8.setGeometry(QtCore.QRect(310, 175, 107, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.line_8.setFont(font)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.pushButton_24 = QtWidgets.QPushButton(self.groupBox_17)
        self.pushButton_24.setGeometry(QtCore.QRect(204, 360, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setObjectName("pushButton_24")
        self.label_92 = QtWidgets.QLabel(self.groupBox_17)
        self.label_92.setGeometry(QtCore.QRect(20, 325, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_92.setFont(font)
        self.label_92.setObjectName("label_92")
        self.comboBox_24 = QtWidgets.QComboBox(self.groupBox_17)
        self.comboBox_24.setGeometry(QtCore.QRect(20, 400, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_24.setFont(font)
        self.comboBox_24.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_24.setEditable(False)
        self.comboBox_24.setFrame(True)
        self.comboBox_24.setObjectName("comboBox_24")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.pushButton_25 = QtWidgets.QPushButton(self.groupBox_17)
        self.pushButton_25.setGeometry(QtCore.QRect(204, 400, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setObjectName("pushButton_25")
        self.label_93 = QtWidgets.QLabel(self.groupBox_17)
        self.label_93.setGeometry(QtCore.QRect(30, 170, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_93.setFont(font)
        self.label_93.setObjectName("label_93")
        self.label_94 = QtWidgets.QLabel(self.groupBox_17)
        self.label_94.setGeometry(QtCore.QRect(30, 200, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_94.setFont(font)
        self.label_94.setObjectName("label_94")
        self.spinBox_20 = QtWidgets.QSpinBox(self.groupBox_17)
        self.spinBox_20.setGeometry(QtCore.QRect(214, 207, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_20.setFont(font)
        self.spinBox_20.setStyleSheet("")
        self.spinBox_20.setSuffix("")
        self.spinBox_20.setPrefix("")
        self.spinBox_20.setObjectName("spinBox_20")
        self.label_95 = QtWidgets.QLabel(self.groupBox_17)
        self.label_95.setGeometry(QtCore.QRect(30, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_95.setFont(font)
        self.label_95.setObjectName("label_95")
        self.comboBox_23 = QtWidgets.QComboBox(self.groupBox_17)
        self.comboBox_23.setGeometry(QtCore.QRect(20, 360, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_23.setFont(font)
        self.comboBox_23.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_23.setEditable(False)
        self.comboBox_23.setFrame(True)
        self.comboBox_23.setObjectName("comboBox_23")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_25 = QtWidgets.QComboBox(self.groupBox_17)
        self.comboBox_25.setGeometry(QtCore.QRect(410, 44, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_25.setFont(font)
        self.comboBox_25.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_25.setEditable(False)
        self.comboBox_25.setDuplicatesEnabled(False)
        self.comboBox_25.setFrame(True)
        self.comboBox_25.setObjectName("comboBox_25")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_26 = QtWidgets.QComboBox(self.groupBox_17)
        self.comboBox_26.setGeometry(QtCore.QRect(410, 68, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_26.setFont(font)
        self.comboBox_26.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));")
        self.comboBox_26.setEditable(False)
        self.comboBox_26.setFrame(True)
        self.comboBox_26.setObjectName("comboBox_26")
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_27 = QtWidgets.QComboBox(self.groupBox_17)
        self.comboBox_27.setGeometry(QtCore.QRect(410, 92, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_27.setFont(font)
        self.comboBox_27.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));")
        self.comboBox_27.setEditable(False)
        self.comboBox_27.setFrame(True)
        self.comboBox_27.setObjectName("comboBox_27")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_28 = QtWidgets.QComboBox(self.groupBox_17)
        self.comboBox_28.setGeometry(QtCore.QRect(410, 115, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_28.setFont(font)
        self.comboBox_28.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));")
        self.comboBox_28.setEditable(False)
        self.comboBox_28.setFrame(True)
        self.comboBox_28.setObjectName("comboBox_28")
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_28.addItem("")
        self.comboBox_29 = QtWidgets.QComboBox(self.groupBox_17)
        self.comboBox_29.setGeometry(QtCore.QRect(410, 139, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_29.setFont(font)
        self.comboBox_29.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));")
        self.comboBox_29.setEditable(False)
        self.comboBox_29.setFrame(True)
        self.comboBox_29.setObjectName("comboBox_29")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_30 = QtWidgets.QComboBox(self.groupBox_17)
        self.comboBox_30.setGeometry(QtCore.QRect(410, 163, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_30.setFont(font)
        self.comboBox_30.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"gridline-color: rgb(85, 255, 0);\n"
"")
        self.comboBox_30.setEditable(False)
        self.comboBox_30.setFrame(True)
        self.comboBox_30.setObjectName("comboBox_30")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.label_96 = QtWidgets.QLabel(self.groupBox_17)
        self.label_96.setGeometry(QtCore.QRect(310, 187, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_96.setFont(font)
        self.label_96.setObjectName("label_96")
        self.label_97 = QtWidgets.QLabel(self.groupBox_17)
        self.label_97.setGeometry(QtCore.QRect(320, 209, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_97.setFont(font)
        self.label_97.setObjectName("label_97")
        self.label_100 = QtWidgets.QLabel(self.groupBox_17)
        self.label_100.setGeometry(QtCore.QRect(320, 271, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_100.setFont(font)
        self.label_100.setObjectName("label_100")
        self.label_101 = QtWidgets.QLabel(self.groupBox_17)
        self.label_101.setGeometry(QtCore.QRect(320, 294, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_101.setFont(font)
        self.label_101.setObjectName("label_101")
        self.spinBox_25 = QtWidgets.QSpinBox(self.groupBox_17)
        self.spinBox_25.setGeometry(QtCore.QRect(490, 215, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_25.setFont(font)
        self.spinBox_25.setObjectName("spinBox_25")
        self.spinBox_26 = QtWidgets.QSpinBox(self.groupBox_17)
        self.spinBox_26.setGeometry(QtCore.QRect(492, 276, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_26.setFont(font)
        self.spinBox_26.setObjectName("spinBox_26")
        self.spinBox_27 = QtWidgets.QSpinBox(self.groupBox_17)
        self.spinBox_27.setGeometry(QtCore.QRect(492, 301, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox_27.setFont(font)
        self.spinBox_27.setObjectName("spinBox_27")
        self.groupBox_18 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_18.setGeometry(QtCore.QRect(370, 364, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_18.setFont(font)
        self.groupBox_18.setObjectName("groupBox_18")
        self.pushButton_28 = QtWidgets.QPushButton(self.groupBox_18)
        self.pushButton_28.setGeometry(QtCore.QRect(34, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setObjectName("pushButton_28")
        self.comboBox_32 = QtWidgets.QComboBox(self.groupBox_17)
        self.comboBox_32.setGeometry(QtCore.QRect(306, 325, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_32.setFont(font)
        self.comboBox_32.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_32.setEditable(False)
        self.comboBox_32.setFrame(True)
        self.comboBox_32.setObjectName("comboBox_32")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.pushButton_27 = QtWidgets.QPushButton(self.groupBox_17)
        self.pushButton_27.setGeometry(QtCore.QRect(482, 324, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_26 = QtWidgets.QPushButton(self.groupBox_17)
        self.pushButton_26.setGeometry(QtCore.QRect(482, 240, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setObjectName("pushButton_26")
        self.comboBox_31 = QtWidgets.QComboBox(self.groupBox_17)
        self.comboBox_31.setGeometry(QtCore.QRect(306, 240, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_31.setFont(font)
        self.comboBox_31.setStyleSheet("selection-color: rgb(0, 0, 0);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.83, y1:0.170455, x2:0.892091, y2:0.961, stop:0 rgba(255, 255, 127, 255), stop:1 rgba(255, 255, 182, 255));\n"
"")
        self.comboBox_31.setEditable(False)
        self.comboBox_31.setFrame(True)
        self.comboBox_31.setObjectName("comboBox_31")
        self.comboBox_31.addItem("")
        self.comboBox_31.addItem("")
        self.comboBox_31.addItem("")
        self.line_9 = QtWidgets.QFrame(self.tab_3)
        self.line_9.setGeometry(QtCore.QRect(10, 230, 201, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.line_9.setFont(font)
        self.line_9.setStyleSheet("")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.groupBox_19 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_19.setGeometry(QtCore.QRect(0, 530, 597, 141))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_19.setFont(font)
        self.groupBox_19.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_19.setObjectName("groupBox_19")
        self.groupBox_21 = QtWidgets.QGroupBox(self.groupBox_19)
        self.groupBox_21.setGeometry(QtCore.QRect(173, 30, 280, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_21.setFont(font)
        self.groupBox_21.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_21.setObjectName("groupBox_21")
        self.pushButton_33 = QtWidgets.QPushButton(self.groupBox_21)
        self.pushButton_33.setGeometry(QtCore.QRect(101, 60, 84, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_32 = QtWidgets.QPushButton(self.groupBox_21)
        self.pushButton_32.setGeometry(QtCore.QRect(187, 60, 88, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_31 = QtWidgets.QPushButton(self.groupBox_21)
        self.pushButton_31.setGeometry(QtCore.QRect(5, 60, 94, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setAutoDefault(False)
        self.pushButton_31.setDefault(False)
        self.pushButton_31.setFlat(False)
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_40 = QtWidgets.QPushButton(self.groupBox_21)
        self.pushButton_40.setGeometry(QtCore.QRect(20, 20, 114, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.groupBox_21)
        self.pushButton_41.setGeometry(QtCore.QRect(150, 20, 114, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setObjectName("pushButton_41")
        self.groupBox_20 = QtWidgets.QGroupBox(self.groupBox_19)
        self.groupBox_20.setGeometry(QtCore.QRect(6, 30, 163, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_20.setFont(font)
        self.groupBox_20.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_20.setObjectName("groupBox_20")
        self.pushButton_29 = QtWidgets.QPushButton(self.groupBox_20)
        self.pushButton_29.setGeometry(QtCore.QRect(9, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox_20)
        self.pushButton_30.setGeometry(QtCore.QRect(86, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setObjectName("pushButton_30")
        self.progressBar_5 = QtWidgets.QProgressBar(self.groupBox_20)
        self.progressBar_5.setGeometry(QtCore.QRect(9, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.progressBar_5.setFont(font)
        self.progressBar_5.setProperty("value", 25)
        self.progressBar_5.setTextVisible(True)
        self.progressBar_5.setInvertedAppearance(False)
        self.progressBar_5.setObjectName("progressBar_5")
        self.progressBar_6 = QtWidgets.QProgressBar(self.groupBox_20)
        self.progressBar_6.setGeometry(QtCore.QRect(85, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.progressBar_6.setFont(font)
        self.progressBar_6.setProperty("value", 25)
        self.progressBar_6.setTextVisible(True)
        self.progressBar_6.setInvertedAppearance(False)
        self.progressBar_6.setObjectName("progressBar_6")
        self.groupBox_22 = QtWidgets.QGroupBox(self.groupBox_19)
        self.groupBox_22.setGeometry(QtCore.QRect(457, 30, 134, 101))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_22.setFont(font)
        self.groupBox_22.setStyleSheet("QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}")
        self.groupBox_22.setObjectName("groupBox_22")
        self.pushButton_34 = QtWidgets.QPushButton(self.groupBox_22)
        self.pushButton_34.setGeometry(QtCore.QRect(6, 20, 122, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.groupBox_22)
        self.pushButton_35.setGeometry(QtCore.QRect(6, 60, 122, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setObjectName("pushButton_35")
        self.tabWidget_1.addTab(self.tab_3, "")
        self.groupBox_23 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_23.setGeometry(QtCore.QRect(640, 0, 901, 734))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox_23.setFont(font)
        self.groupBox_23.setStyleSheet("QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 3px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(255, 114, 116);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"QCheckBox::indicator:checked:hover {\n"
"    border-color:qlineargradient(spread:pad, x1:0.603, y1:0.914773, x2:0.221591, y2:0.222, stop:0.323864 rgba(238, 238, 105, 255), stop:0.926136 rgba(244, 244, 160, 255));\n"
"    background-color:qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QCheckBox::indicator:checked:pressed {\n"
"    background-color: rgb(255, 196, 197);\n"
"    border-color:rgb(255, 166, 168);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border-color:qlineargradient(spread:pad, x1:0.603, y1:0.914773, x2:0.221591, y2:0.222, stop:0.323864 rgba(238, 238, 105, 255), stop:0.926136 rgba(244, 244, 160, 255));\n"
"    background-color:qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    background-color: rgb(255, 196, 197);\n"
"    border-color:rgb(255, 166, 168);\n"
"}\n"
"/* --------------------------  */\n"
"QComboBox {\n"
"    border: 2px solid rgb(92, 143, 143);\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    border-style: outset;\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"}\n"
"QComboBox:editable {\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox::item:selected {\n"
"background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.369, y2:0.142409, stop:0.323864 rgba(255, 200, 201, 255), stop:0.926136 rgba(255, 234, 234, 255));\n"
"    border-radius:5px;}\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background-color: qlineargradient(spread:pad, x1:0.460318, y1:0, x2:0.466, y2:0.806818, stop:0 rgba(95, 176, 176, 255), stop:1 rgba(172, 214, 214, 255));\n"
"}\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background-color: qlineargradient(spread:pad, x1:0.603, y1:0.914773, x2:0.221591, y2:0.222, stop:0.323864 rgba(238, 238, 105, 255), stop:0.926136 rgba(244, 244, 160, 255));\n"
"}\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;}\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;}\n"
"QComboBox:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QComboBox:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QComboBox::separator {\n"
"    height: 1px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.505591, y2:1, stop:0.323864 rgba(242, 108, 110, 255), stop:0.926136 rgba(251, 207, 208, 255));\n"
"    margin-left: 18px;\n"
"    margin-right: 25px;\n"
"    border-radius:5px;\n"
"}\n"
"/* --------------------------  */\n"
"QGroupBox {\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"    border: 2px solid rgb(92, 143, 143);\n"
"    border-radius: 10px;}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 5px;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;}\n"
"/* --------------------------  */\n"
"QLabel{\n"
"background-color: transparent\n"
"}\n"
"/* --------------------------  */\n"
"QLine{\n"
"background-color: transparent\n"
"}\n"
"/* --------------------------  */\n"
"\n"
"QFrame[frameShape=\"4\"],\n"
"QFrame[frameShape=\"5\"]\n"
"{\n"
"    border: none;\n"
"    background: qlineargradient(spread:pad, x1:0.633, y1:0, x2:0.760182, y2:0.926, stop:0.323864 rgba(252, 113, 115, 255), stop:0.926136 rgba(255, 174, 177, 255));\n"
"    margin:9px\n"
"}\n"
"/* --------------------------  */\n"
"QMainWindow{\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"}\n"
"/* --------------------------  */\n"
"QMenu {\n"
"background-color: qlineargradient(spread:pad, x1:0.763, y1:0.284091, x2:0.817, y2:0.931682, stop:0.323864 rgba(255, 234, 234, 255), stop:0.926136 rgba(255, 243, 243, 255));\n"
"    margin: 1px; /* some spacing around the menu */\n"
"    font: 75 10pt \"Comic Sans MS\";\n"
"    border-radius:5px;}\n"
"QMenu::item {\n"
"    padding: 2px 25px 2px 20px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"    border-radius:5px;}\n"
"QMenu::item:selected {\n"
"    background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.380364, y2:0, stop:0.323864 rgba(255, 185, 186, 255), stop:0.926136 rgba(255, 221, 222, 255));\n"
"    border-radius:5px;}\n"
"QMenu::icon:checked { /* appearance of a \'checked\' icon */\n"
"    background: gray;\n"
"    border: 1px inset rgb(92, 143, 143);\n"
"    position: absolute;\n"
"    top: 1px;\n"
"    right: 1px;\n"
"    bottom: 1px;\n"
"    left: 1px;\n"
"    border-radius:5px;}\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.460318, y1:0, x2:0.466, y2:0.806818, stop:0 rgba(95, 176, 176, 255), stop:1 rgba(172, 214, 214, 255));\n"
"    margin-left: 18px;\n"
"    margin-right: 25px;\n"
"    border-radius:5px;\n"
"}\n"
"QMenuBar {\n"
"background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"    spacing: 3px; /* spacing between menu bar items */\n"
"    font: 75 10pt \"Comic Sans MS\";}\n"
"QMenuBar::item {\n"
"    padding: 1px 4px;\n"
"    background: transparent;\n"
"    border-radius: 4px;}\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"    border-radius:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.380364, y2:0, stop:0.323864 rgba(255, 185, 186, 255), stop:0.926136 rgba(255, 221, 222, 255));\n"
"}\n"
"QMenuBar::item:pressed {\n"
"    border-radius:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.633, y1:0, x2:0.760182, y2:0.926, stop:0.323864 rgba(252, 113, 115, 255), stop:0.926136 rgba(255, 174, 177, 255));\n"
"}\n"
"/* --------------------------  */\n"
"QProgressBar {\n"
"    border: 1px solid rgb(92, 143, 143);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(236, 236, 236, 255));\n"
"    border-style: outset;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color:rgb(255, 114, 116);\n"
"    border-radius: 3px;\n"
"    margin: 0.5px;\n"
"}\n"
"/* --------------------------  */\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0.460318, y1:0, x2:0.466, y2:0.806818, stop:0 rgba(95, 176, 176, 255), stop:1 rgba(172, 214, 214, 255));\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(92, 143, 143);\n"
"    font: 10pt \"Comic Sans MS\";\n"
"    min-width: 3em;\n"
"    padding: 6px;}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.603, y1:0.914773, x2:0.221591, y2:0.222, stop:0.323864 rgba(238, 238, 105, 255), stop:0.926136 rgba(244, 244, 160, 255));\n"
"}\n"
"/* --------------------------  */\n"
"QRadioButton::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-radius: 3px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0.633, y1:0.829955, x2:0.357, y2:0.0225909, stop:0.323864 rgba(252, 113, 115, 255), stop:0.926136 rgba(255, 174, 177, 255));\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"QRadioButton::indicator:checked:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.211682, y1:0.057, x2:0.597, y2:0.989, stop:0.323864 rgba(255, 162, 163, 255), stop:0.926136 rgba(255, 214, 215, 255));\n"
"    border-color:rgb(255, 114, 116);\n"
"}\n"
"QRadioButton::indicator:checked:pressed {\n"
"    border-color:rgb(238, 232, 142);\n"
"    background-color:qlineargradient(spread:pad, x1:0.364409, y1:0.051, x2:0.550773, y2:1, stop:0.323864 rgba(255, 255, 165, 255), stop:0.926136 rgba(255, 255, 214, 255))\n"
"}\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border-color:rgb(238, 232, 142);\n"
"    background-color:qlineargradient(spread:pad, x1:0.512, y1:1, x2:0.511, y2:0, stop:0.323864 rgba(255, 255, 165, 255), stop:0.926136 rgba(255, 255, 214, 255));\n"
"}\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.831, y1:1, x2:0.380364, y2:0, stop:0.323864 rgba(255, 185, 186, 255), stop:0.926136 rgba(255, 221, 222, 255));\n"
"    border-color:rgb(255, 114, 116);\n"
"}\n"
"/* --------------------------  */\n"
"/* VERTICAL SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color:rgb(207, 255, 255);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"/* HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {\n"
"    background-color:rgb(255, 114, 116);\n"
"    min-height: 30px;\n"
"    margin: 0px 0 0px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN TOP - SCROLLBAR*/\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    border-top-left-radius:7px;\n"
"    border-top-right-radius:7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN BOTTOM - SCROLLBAR*/\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    border-bottom-left-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*RESET ARROW*/\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     border: 2px grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"    background-color:rgb(207, 255, 255) ;\n"
" }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"/* --------------------------  */\n"
"/* HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none ;\n"
"    background-color:rgb(207, 255, 255);\n"
"    width: 14px;\n"
"    height: 15px;\n"
"    margin: 0 15px 0 15px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color:rgb(255, 114, 116);\n"
"    min-height: 30px;\n"
"    min-width:20px;\n"
"    margin: 0 0px 0 0px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN LEFT - SCROLLBAR*/\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    width: 14px;\n"
"    border-top-left-radius:7px;\n"
"    border-bottom-left-radius:7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN RIGHT - SCROLLBAR*/\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    width: 14px;\n"
"    border-top-right-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*RESET ARROW*/\n"
" QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"     border: 2px grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"    background-color:rgb(207, 255, 255) ;\n"
" }\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
" }\n"
"/* --------------------------  */\n"
"QSpinBox{\n"
"    border: 1px solid rgb(92, 143, 143);\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 2em;\n"
"  }\n"
"QSpinBox:editable {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"    selection-background-color: rgb(255, 255, 127);\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"QSpinBox:!editable, QSpinBox::drop-down:editable {\n"
"    background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(236, 236, 236, 255));\n"
"}\n"
"QSpinBox:!editable:on, QSpinBox::drop-down:editable:on {\n"
"    background: white;\n"
"\n"
"}\n"
"QSpinBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"}\n"
"QSpinBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"QSpinBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"}\n"
"QSpinBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"    background-color:rgb(255, 255, 113);\n"
"    border-radius: 5px;\n"
"}\n"
"QSpinBox::up-button:pressed{\n"
"    background-color:rgb(238, 238, 114);\n"
"    border-radius: 5px;\n"
"}\n"
"QSpinBox::down-button:hover{\n"
"    background-color:rgb(255, 255, 113);\n"
"    border-radius: 5px;\n"
"}\n"
"QSpinBox::down-button:pressed{\n"
"    background-color:rgb(238, 238, 114);\n"
"    border-radius: 5px;\n"
"}\n"
"/* --------------------------  */\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0 rgba(255, 114, 116, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    margin-left: 5px; /* make non-selected tabs look smaller */\n"
"    margin-right: 5px; /* make non-selected tabs look smaller */\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"background-color: qlineargradient(spread:pad, x1:0.460318, y1:0, x2:0.466, y2:0.806818, stop:0 rgba(95, 176, 176, 255), stop:1 rgba(172, 214, 214, 255));\n"
"    border: 2px solid rgb(92, 143, 143);\n"
"    border-bottom-color: rgb(172, 214, 214); /* same as the pane color */\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    min-width: 10ex;\n"
"    padding: 3px;\n"
"    border-style: outset;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:0.471591, y2:0.908, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 255, 182, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0.429545, y1:0, x2:0.449682, y2:1, stop:0 rgba(192, 236, 236, 255), stop:1 rgba(239, 250, 250, 255));\n"
"}\n"
"QTabBar::tab:selected {\n"
"    border: 2px solid rgb(95, 176, 200);\n"
"    border-style: outset;\n"
"    border-bottom-color:  qlineargradient(spread:pad, x1:0.477682, y1:0.409, x2:0.4715, y2:0, stop:0 rgba(255, 114, 116, 255), stop:1 rgba(255, 255, 255, 255)); /* same as pane color */}\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */}\n"
"/* --------------------------  */\n"
"QTextEdit{\n"
"    border: 1px solid rgb(92, 143, 143);\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 255, 113);\n"
"    selection-color: rgb(0, 0, 0);\n"
"}\n"
"/* --------------------------  */\n"
"QToolBar {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(207, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    spacing: 3px; /* spacing between items in the tool bar */}\n"
"\n"
"")
        self.groupBox_23.setObjectName("groupBox_23")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox_23)
        self.tabWidget_2.setEnabled(True)
        self.tabWidget_2.setGeometry(QtCore.QRect(7, 20, 887, 711))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setAcceptDrops(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textEdit_1 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_1.setGeometry(QtCore.QRect(0, 10, 877, 661))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_1.setFont(font)
        self.textEdit_1.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color:rgb(207, 255, 255);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"/* HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {\n"
"    background-color:rgb(255, 114, 116);\n"
"    min-height: 30px;\n"
"    margin: 0px 0 0px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN TOP - SCROLLBAR*/\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    border-top-left-radius:7px;\n"
"    border-top-right-radius:7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN BOTTOM - SCROLLBAR*/\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    border-bottom-left-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"\n"
"/*RESET ARROW*/\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     border: 2px grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"    background-color:rgb(207, 255, 255) ;\n"
" }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"/* --------------------------  */\n"
"\n"
"/* HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none ;\n"
"    background-color:rgb(207, 255, 255);\n"
"    width: 14px;\n"
"    height: 15px;\n"
"    margin: 0 15px 0 15px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color:rgb(255, 114, 116);\n"
"    min-height: 30px;\n"
"    min-width:20px;\n"
"    margin: 0 0px 0 0px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN LEFT - SCROLLBAR*/\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    width: 14px;\n"
"    border-top-left-radius:7px;\n"
"    border-bottom-left-radius:7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN RIGHT - SCROLLBAR*/\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    width: 14px;\n"
"    border-top-right-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*RESET ARROW*/\n"
" QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"     border: 2px grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"    background-color:rgb(207, 255, 255) ;\n"
" }\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
" }")
        self.textEdit_1.setObjectName("textEdit_1")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 10, 877, 661))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("QWidget  {\n"
"        background-color: qlineargradient(spread:pad, x1:0.523, y1:0.0227273, x2:0.534, y2:1, stop:0.323864 rgba(255, 255, 217, 255), stop:0.926136 rgba(255, 255, 255, 255));\n"
"    }\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color:rgb(207, 255, 255);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"/* HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {\n"
"    background-color:rgb(255, 114, 116);\n"
"    min-height: 30px;\n"
"    margin: 0px 0 0px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN TOP - SCROLLBAR*/\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    border-top-left-radius:7px;\n"
"    border-top-right-radius:7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN BOTTOM - SCROLLBAR*/\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    border-bottom-left-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"\n"
"/*RESET ARROW*/\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     border: 2px grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"    background-color:rgb(207, 255, 255) ;\n"
" }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"/* --------------------------  */\n"
"\n"
"/* HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none ;\n"
"    background-color:rgb(207, 255, 255);\n"
"    width: 14px;\n"
"    height: 15px;\n"
"    margin: 0 15px 0 15px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color:rgb(255, 114, 116);\n"
"    min-height: 30px;\n"
"    min-width:20px;\n"
"    margin: 0 0px 0 0px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN LEFT - SCROLLBAR*/\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    width: 14px;\n"
"    border-top-left-radius:7px;\n"
"    border-bottom-left-radius:7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*BTN RIGHT - SCROLLBAR*/\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color:rgb(255, 114, 116) ;\n"
"    height:15px;\n"
"    width: 14px;\n"
"    border-top-right-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"    background-color:rgb(119, 220, 220);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed{\n"
"    background-color:rgb(95, 176, 176);\n"
"}\n"
"/*RESET ARROW*/\n"
" QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"     border: 2px grey;\n"
"     width: 3px;\n"
"     height: 3px;\n"
"    background-color:rgb(207, 255, 255) ;\n"
" }\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
"}")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1217, 21))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        self.menuPlot = QtWidgets.QMenu(self.menuNew)
        self.menuPlot.setObjectName("menuPlot")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 27))
        self.toolBar.setSizeIncrement(QtCore.QSize(0, 0))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionRun = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Prefix/Run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon1)
        self.actionRun.setIconVisibleInMenu(True)
        self.actionRun.setObjectName("actionRun")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Prefix/Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon2)
        self.actionClose.setIconVisibleInMenu(True)
        self.actionClose.setObjectName("actionClose")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Prefix/Add_File.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon3)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Prefix/Folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon4)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Prefix/Save_as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon5)
        self.actionSave_as.setIconVisibleInMenu(True)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Prefix/Quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon6)
        self.actionQuit.setIconVisibleInMenu(True)
        self.actionQuit.setObjectName("actionQuit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Prefix/Undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon7)
        self.actionUndo.setIconVisibleInMenu(True)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Prefix/Redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon8)
        self.actionRedo.setIconVisibleInMenu(True)
        self.actionRedo.setObjectName("actionRedo")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Prefix/Trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon9)
        self.actionDelete.setIconVisibleInMenu(True)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Prefix/Select_All.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelect_All.setIcon(icon10)
        self.actionSelect_All.setIconVisibleInMenu(True)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Prefix/Save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon11)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName("actionSave")
        self.actionFind = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Prefix/Find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon12)
        self.actionFind.setIconVisibleInMenu(True)
        self.actionFind.setObjectName("actionFind")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Prefix/Cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon13)
        self.actionCut.setIconVisibleInMenu(True)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/Prefix/Paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon14)
        self.actionPaste.setIconVisibleInMenu(True)
        self.actionPaste.setObjectName("actionPaste")
        self.actionRadial_Power = QtWidgets.QAction(MainWindow)
        self.actionRadial_Power.setIconVisibleInMenu(True)
        self.actionRadial_Power.setObjectName("actionRadial_Power")
        self.actionAxial_Power = QtWidgets.QAction(MainWindow)
        self.actionAxial_Power.setIconVisibleInMenu(True)
        self.actionAxial_Power.setObjectName("actionAxial_Power")
        self.actionRadial_Flux = QtWidgets.QAction(MainWindow)
        self.actionRadial_Flux.setIconVisibleInMenu(True)
        self.actionRadial_Flux.setObjectName("actionRadial_Flux")
        self.actionGeometry = QtWidgets.QAction(MainWindow)
        self.actionGeometry.setIconVisibleInMenu(True)
        self.actionGeometry.setObjectName("actionGeometry")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/Prefix/Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon15)
        self.actionCopy.setIconVisibleInMenu(True)
        self.actionCopy.setObjectName("actionCopy")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/Prefix/Q_t.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_Qt.setIcon(icon16)
        self.actionAbout_Qt.setIconVisibleInMenu(True)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/Prefix/Info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon17)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/Prefix/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon18)
        self.actionHelp.setIconVisibleInMenu(True)
        self.actionHelp.setObjectName("actionHelp")
        self.actionCompile = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/Prefix/compiile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompile.setIcon(icon19)
        self.actionCompile.setIconVisibleInMenu(True)
        self.actionCompile.setObjectName("actionCompile")
        self.menuPlot.addAction(self.actionGeometry)
        self.menuPlot.addSeparator()
        self.menuPlot.addAction(self.actionRadial_Flux)
        self.menuPlot.addSeparator()
        self.menuPlot.addAction(self.actionRadial_Power)
        self.menuPlot.addAction(self.actionAxial_Power)
        self.menuNew.addAction(self.actionNew)
        self.menuNew.addAction(self.actionOpen)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionSave)
        self.menuNew.addAction(self.actionSave_as)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionCompile)
        self.menuNew.addAction(self.actionRun)
        self.menuNew.addAction(self.menuPlot.menuAction())
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionClose)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSave_as)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionSelect_All)
        self.toolBar.addAction(self.actionFind)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCompile)
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionAbout_Qt)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClose)
        self.toolBar.addAction(self.actionQuit)
        self.label_56.setBuddy(self.spinBox_4)
        self.label_75.setBuddy(self.spinBox_4)
        self.label_94.setBuddy(self.spinBox_4)

        self.retranslateUi(MainWindow)
        self.tabWidget_1.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.scrollArea, self.tabWidget_1)
        MainWindow.setTabOrder(self.tabWidget_1, self.radioButton_1)
        MainWindow.setTabOrder(self.radioButton_1, self.spinBox_1)
        MainWindow.setTabOrder(self.spinBox_1, self.spinBox_2)
        MainWindow.setTabOrder(self.spinBox_2, self.spinBox_3)
        MainWindow.setTabOrder(self.spinBox_3, self.comboBox_1)
        MainWindow.setTabOrder(self.comboBox_1, self.pushButton_1)
        MainWindow.setTabOrder(self.pushButton_1, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.spinBox_4)
        MainWindow.setTabOrder(self.spinBox_4, self.spinBox_5)
        MainWindow.setTabOrder(self.spinBox_5, self.spinBox_6)
        MainWindow.setTabOrder(self.spinBox_6, self.spinBox_7)
        MainWindow.setTabOrder(self.spinBox_7, self.spinBox_8)
        MainWindow.setTabOrder(self.spinBox_8, self.comboBox_3)
        MainWindow.setTabOrder(self.comboBox_3, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.comboBox_4)
        MainWindow.setTabOrder(self.comboBox_4, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.comboBox_5)
        MainWindow.setTabOrder(self.comboBox_5, self.comboBox_6)
        MainWindow.setTabOrder(self.comboBox_6, self.comboBox_7)
        MainWindow.setTabOrder(self.comboBox_7, self.comboBox_8)
        MainWindow.setTabOrder(self.comboBox_8, self.comboBox_9)
        MainWindow.setTabOrder(self.comboBox_9, self.comboBox_10)
        MainWindow.setTabOrder(self.comboBox_10, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.pushButton_8)
        MainWindow.setTabOrder(self.pushButton_8, self.pushButton_9)
        MainWindow.setTabOrder(self.pushButton_9, self.pushButton_10)
        MainWindow.setTabOrder(self.pushButton_10, self.tabWidget_2)
        MainWindow.setTabOrder(self.tabWidget_2, self.textEdit_1)
        MainWindow.setTabOrder(self.textEdit_1, self.textEdit_2)
        MainWindow.setTabOrder(self.textEdit_2, self.pushButton_10)
        MainWindow.setTabOrder(self.pushButton_10, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.comboBox_7)
        MainWindow.setTabOrder(self.comboBox_7, self.spinBox_8)
        MainWindow.setTabOrder(self.spinBox_8, self.spinBox_3)
        MainWindow.setTabOrder(self.spinBox_3, self.spinBox_6)
        MainWindow.setTabOrder(self.spinBox_6, self.spinBox_1)
        MainWindow.setTabOrder(self.spinBox_1, self.radioButton_1)
        MainWindow.setTabOrder(self.radioButton_1, self.tabWidget_1)
        MainWindow.setTabOrder(self.tabWidget_1, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.spinBox_2)
        MainWindow.setTabOrder(self.spinBox_2, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.spinBox_5)
        MainWindow.setTabOrder(self.spinBox_5, self.comboBox_6)
        MainWindow.setTabOrder(self.comboBox_6, self.comboBox_1)
        MainWindow.setTabOrder(self.comboBox_1, self.pushButton_1)
        MainWindow.setTabOrder(self.pushButton_1, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.spinBox_7)
        MainWindow.setTabOrder(self.spinBox_7, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.comboBox_4)
        MainWindow.setTabOrder(self.comboBox_4, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.spinBox_4)
        MainWindow.setTabOrder(self.spinBox_4, self.comboBox_3)
        MainWindow.setTabOrder(self.comboBox_3, self.comboBox_5)
        MainWindow.setTabOrder(self.comboBox_5, self.pushButton_8)
        MainWindow.setTabOrder(self.pushButton_8, self.pushButton_9)
        MainWindow.setTabOrder(self.pushButton_9, self.comboBox_10)
        MainWindow.setTabOrder(self.comboBox_10, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.comboBox_8)
        MainWindow.setTabOrder(self.comboBox_8, self.comboBox_9)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_1.setTitle(_translate("MainWindow", "Calculation Mode"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Calculation Method"))
        self.radioButton_1.setText(_translate("MainWindow", "NEM"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Input Parameters"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Energy Groups</span></p></body></html>"))
        self.label_40.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Materials</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Cartesian"))
        self.label_41.setText(_translate("MainWindow", "Assemblies Number (x)"))
        self.label_42.setText(_translate("MainWindow", "Assemblies Number (y)"))
        self.label_43.setText(_translate("MainWindow", "Assemblies Number (z)"))
        self.label_44.setText(_translate("MainWindow", "Planar Number"))
        self.label_45.setText(_translate("MainWindow", "<html><head/><body><p>Cross Sections</p></body></html>"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "                X-S"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "Absorption_XS"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "Transport_XS"))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "Fission_XS"))
        self.comboBox_1.setItemText(4, _translate("MainWindow", "Nu*Fission_XS"))
        self.comboBox_1.setItemText(5, _translate("MainWindow", "Chi"))
        self.comboBox_1.setItemText(6, _translate("MainWindow", "Scattering_XS"))
        self.pushButton_1.setText(_translate("MainWindow", "Insert"))
        self.label_46.setText(_translate("MainWindow", "Boundary Conditions"))
        self.label_47.setText(_translate("MainWindow", "East"))
        self.label_48.setText(_translate("MainWindow", "West"))
        self.label_49.setText(_translate("MainWindow", "North"))
        self.label_50.setText(_translate("MainWindow", "South"))
        self.label_51.setText(_translate("MainWindow", "Top"))
        self.label_52.setText(_translate("MainWindow", "Bottom"))
        self.pushButton_2.setText(_translate("MainWindow", "Insert"))
        self.label_54.setText(_translate("MainWindow", "Constructive Geometry"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "  Assignement to Axes"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Planar to Z"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Material to XY"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Material to Z"))
        self.pushButton_3.setText(_translate("MainWindow", "Insert"))
        self.label_55.setText(_translate("MainWindow", "Geometry"))
        self.label_56.setText(_translate("MainWindow", "Dimensions"))
        self.label_57.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Polynomial Order</span></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "       Division/Size"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Assembly Division"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Assembly Size"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_10.setItemText(3, _translate("MainWindow", "Reflective"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Input File"))
        self.pushButton_4.setText(_translate("MainWindow", "Upload"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Output Parameters"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Plots-2D"))
        self.pushButton_8.setText(_translate("MainWindow", "Axial Power"))
        self.pushButton_7.setText(_translate("MainWindow", "Radial Power"))
        self.pushButton_36.setText(_translate("MainWindow", "Radial Geometry"))
        self.pushButton_37.setText(_translate("MainWindow", "Axial Geometry"))
        self.pushButton_9.setText(_translate("MainWindow", "Radial Flux"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Controls"))
        self.pushButton_5.setText(_translate("MainWindow", "Compile"))
        self.pushButton_6.setText(_translate("MainWindow", "Run"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Plots-3D"))
        self.pushButton_10.setText(_translate("MainWindow", "Compile Geometry"))
        self.pushButton_11.setText(_translate("MainWindow", "Run Geometry"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_1), _translate("MainWindow", "Forward"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Calculation Method"))
        self.radioButton_2.setText(_translate("MainWindow", "NEM"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Input Parameters"))
        self.label_58.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Energy Groups</span></p></body></html>"))
        self.label_59.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Materials</span></p></body></html>"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "Cartesian"))
        self.label_60.setText(_translate("MainWindow", "Assemblies Number (x)"))
        self.label_61.setText(_translate("MainWindow", "Assemblies Number (y)"))
        self.label_62.setText(_translate("MainWindow", "Assemblies Number (z)"))
        self.label_63.setText(_translate("MainWindow", "Planar Number"))
        self.label_64.setText(_translate("MainWindow", "<html><head/><body><p>Cross Sections</p></body></html>"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "                X-S"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "Absorption_XS"))
        self.comboBox_11.setItemText(2, _translate("MainWindow", "Transport_XS"))
        self.comboBox_11.setItemText(3, _translate("MainWindow", "Fission_XS"))
        self.comboBox_11.setItemText(4, _translate("MainWindow", "Nu*Fission_XS"))
        self.comboBox_11.setItemText(5, _translate("MainWindow", "Chi"))
        self.comboBox_11.setItemText(6, _translate("MainWindow", "Scattering_XS"))
        self.pushButton_12.setText(_translate("MainWindow", "Insert"))
        self.label_65.setText(_translate("MainWindow", "Boundary Conditions"))
        self.label_66.setText(_translate("MainWindow", "East"))
        self.label_67.setText(_translate("MainWindow", "West"))
        self.label_68.setText(_translate("MainWindow", "North"))
        self.label_69.setText(_translate("MainWindow", "South"))
        self.label_70.setText(_translate("MainWindow", "Top"))
        self.label_71.setText(_translate("MainWindow", "Bottom"))
        self.pushButton_13.setText(_translate("MainWindow", "Insert"))
        self.label_73.setText(_translate("MainWindow", "Constructive Geometry"))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "  Assignement to Axes"))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "Planar to Z"))
        self.comboBox_14.setItemText(2, _translate("MainWindow", "Material to XY-Assembly"))
        self.comboBox_14.setItemText(3, _translate("MainWindow", "Material to Z-Assembly"))
        self.pushButton_14.setText(_translate("MainWindow", "Insert"))
        self.label_74.setText(_translate("MainWindow", "Geometry"))
        self.label_75.setText(_translate("MainWindow", "Dimensions"))
        self.label_76.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Polynomial Order</span></p></body></html>"))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "       Division/Size"))
        self.comboBox_13.setItemText(1, _translate("MainWindow", "Assembly Division"))
        self.comboBox_13.setItemText(2, _translate("MainWindow", "Assembly Size"))
        self.comboBox_15.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_15.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_15.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_15.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_16.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_16.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_16.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_16.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_17.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_17.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_17.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_17.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_18.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_18.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_18.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_18.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_19.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_19.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_19.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_19.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_20.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_20.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_20.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_20.setItemText(3, _translate("MainWindow", "Reflective"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Input File"))
        self.pushButton_15.setText(_translate("MainWindow", "Upload"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Output Parameters"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Plots-2D"))
        self.pushButton_20.setText(_translate("MainWindow", "Radial Flux"))
        self.pushButton_19.setText(_translate("MainWindow", "Axial Power"))
        self.pushButton_18.setText(_translate("MainWindow", "Radial Power"))
        self.pushButton_38.setText(_translate("MainWindow", "Radial Geometry"))
        self.pushButton_39.setText(_translate("MainWindow", "Axial Geometry"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Controls"))
        self.pushButton_16.setText(_translate("MainWindow", "Compile"))
        self.pushButton_17.setText(_translate("MainWindow", "Run"))
        self.groupBox_15.setTitle(_translate("MainWindow", "Plots-3D"))
        self.pushButton_21.setText(_translate("MainWindow", "Compile Geometry"))
        self.pushButton_22.setText(_translate("MainWindow", "Run Geometry"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_2), _translate("MainWindow", "Adjoint"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Calculation Method"))
        self.radioButton_3.setText(_translate("MainWindow", "NEM"))
        self.groupBox_17.setTitle(_translate("MainWindow", "Input Parameters"))
        self.label_77.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Energy Groups</span></p></body></html>"))
        self.label_78.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Materials</span></p></body></html>"))
        self.comboBox_22.setItemText(0, _translate("MainWindow", "Cartesian"))
        self.label_79.setText(_translate("MainWindow", "Assemblies Number (x)"))
        self.label_80.setText(_translate("MainWindow", "Assemblies Number (y)"))
        self.label_81.setText(_translate("MainWindow", "Assemblies Number (z)"))
        self.label_82.setText(_translate("MainWindow", "Planar Number"))
        self.label_83.setText(_translate("MainWindow", "<html><head/><body><p>Cross Sections</p></body></html>"))
        self.comboBox_21.setItemText(0, _translate("MainWindow", "                X-S"))
        self.comboBox_21.setItemText(1, _translate("MainWindow", "Absorption_XS"))
        self.comboBox_21.setItemText(2, _translate("MainWindow", "Transport_XS"))
        self.comboBox_21.setItemText(3, _translate("MainWindow", "Fission_XS"))
        self.comboBox_21.setItemText(4, _translate("MainWindow", "Nu*Fission_XS"))
        self.comboBox_21.setItemText(5, _translate("MainWindow", "Chi"))
        self.comboBox_21.setItemText(6, _translate("MainWindow", "Scattering_XS"))
        self.pushButton_23.setText(_translate("MainWindow", "Insert"))
        self.label_84.setText(_translate("MainWindow", "Boundary Conditions"))
        self.label_85.setText(_translate("MainWindow", "East"))
        self.label_86.setText(_translate("MainWindow", "West"))
        self.label_87.setText(_translate("MainWindow", "North"))
        self.label_88.setText(_translate("MainWindow", "South"))
        self.label_89.setText(_translate("MainWindow", "Top"))
        self.label_90.setText(_translate("MainWindow", "Bottom"))
        self.pushButton_24.setText(_translate("MainWindow", "Insert"))
        self.label_92.setText(_translate("MainWindow", "Constructive Geometry"))
        self.comboBox_24.setItemText(0, _translate("MainWindow", "  Assignement to Axes"))
        self.comboBox_24.setItemText(1, _translate("MainWindow", "Planar to Z"))
        self.comboBox_24.setItemText(2, _translate("MainWindow", "Material to XY-Assembly"))
        self.comboBox_24.setItemText(3, _translate("MainWindow", "Material to Z-Assembly"))
        self.pushButton_25.setText(_translate("MainWindow", "Insert"))
        self.label_93.setText(_translate("MainWindow", "Geometry"))
        self.label_94.setText(_translate("MainWindow", "Dimensions"))
        self.label_95.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Polynomial Order</span></p></body></html>"))
        self.comboBox_23.setItemText(0, _translate("MainWindow", "       Division/Size"))
        self.comboBox_23.setItemText(1, _translate("MainWindow", "Assembly Division"))
        self.comboBox_23.setItemText(2, _translate("MainWindow", "Assembly Size"))
        self.comboBox_25.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_25.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_25.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_25.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_26.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_26.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_26.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_26.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_27.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_27.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_27.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_27.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_28.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_28.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_28.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_28.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_29.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_29.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_29.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_29.setItemText(3, _translate("MainWindow", "Reflective"))
        self.comboBox_30.setItemText(0, _translate("MainWindow", "             BC"))
        self.comboBox_30.setItemText(1, _translate("MainWindow", "Vacuum Flux"))
        self.comboBox_30.setItemText(2, _translate("MainWindow", "Vacuum Current"))
        self.comboBox_30.setItemText(3, _translate("MainWindow", "Reflective"))
        self.label_96.setText(_translate("MainWindow", "Fixed Source Parameters"))
        self.label_97.setText(_translate("MainWindow", "<html><head/><body><p>Source Number</p></body></html>"))
        self.label_100.setText(_translate("MainWindow", "<html><head/><body><p>Radial FS Number</p></body></html>"))
        self.label_101.setText(_translate("MainWindow", "<html><head/><body><p>Axial FS Number</p></body></html>"))
        self.groupBox_18.setTitle(_translate("MainWindow", "Input File"))
        self.pushButton_28.setText(_translate("MainWindow", "Upload"))
        self.comboBox_32.setItemText(0, _translate("MainWindow", "     FS Position (xyz)"))
        self.comboBox_32.setItemText(1, _translate("MainWindow", "Radial Position"))
        self.comboBox_32.setItemText(2, _translate("MainWindow", "Axial Position"))
        self.pushButton_27.setText(_translate("MainWindow", "Insert"))
        self.pushButton_26.setText(_translate("MainWindow", "Insert"))
        self.comboBox_31.setItemText(0, _translate("MainWindow", "    Density/Spectrum"))
        self.comboBox_31.setItemText(1, _translate("MainWindow", "Source Density"))
        self.comboBox_31.setItemText(2, _translate("MainWindow", "Source Spectrum"))
        self.groupBox_19.setTitle(_translate("MainWindow", "Output Parameters"))
        self.groupBox_21.setTitle(_translate("MainWindow", "Plots-2D"))
        self.pushButton_33.setText(_translate("MainWindow", "Radial Flux"))
        self.pushButton_32.setText(_translate("MainWindow", "Axial Power"))
        self.pushButton_31.setText(_translate("MainWindow", "Radial Power"))
        self.pushButton_40.setText(_translate("MainWindow", "Radial Geometry"))
        self.pushButton_41.setText(_translate("MainWindow", "Axial Geometry"))
        self.groupBox_20.setTitle(_translate("MainWindow", "Controls"))
        self.pushButton_29.setText(_translate("MainWindow", "Compile"))
        self.pushButton_30.setText(_translate("MainWindow", "Run"))
        self.groupBox_22.setTitle(_translate("MainWindow", "Plots-3D"))
        self.pushButton_34.setText(_translate("MainWindow", "Compile Geometry"))
        self.pushButton_35.setText(_translate("MainWindow", "Run Geometry"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_3), _translate("MainWindow", "Fixed Source"))
        self.groupBox_23.setTitle(_translate("MainWindow", "NoteBook"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Input"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Output"))
        self.menuNew.setTitle(_translate("MainWindow", "File"))
        self.menuPlot.setTitle(_translate("MainWindow", "Plot"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionRun.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+Alt+S"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Del"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionSelect_All.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionFind.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionRadial_Power.setText(_translate("MainWindow", "Radial Power"))
        self.actionAxial_Power.setText(_translate("MainWindow", "Axial Power"))
        self.actionRadial_Flux.setText(_translate("MainWindow", "Radial Flux"))
        self.actionGeometry.setText(_translate("MainWindow", "Geometry"))
        self.actionGeometry.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))
        self.actionAbout_Qt.setToolTip(_translate("MainWindow", "About Qt"))
        self.actionAbout_Qt.setShortcut(_translate("MainWindow", "F4"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "F3"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F2"))
        self.actionCompile.setText(_translate("MainWindow", "Compile"))
        self.actionCompile.setIconText(_translate("MainWindow", "Compile"))
        self.actionCompile.setShortcut(_translate("MainWindow", "Ctrl+L"))

import png

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

