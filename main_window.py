#!/usr/bin/python3
#WARRNING : This App is Just a practice Coding with python3.6 and pyqt5

#Name ----------: collections 
#version -------: 0.1
#Created -------: 14/08/2019
#Last Updates --: 16/08/2019
#Author --------: Khaled Fathi [KhaledFathi@protonmail.com]
#Code ----------: Python3.6 | Frameworks : PyQt5
#repository ----: None

import sys , time , math , os , pathlib
#from app lib
import license_app , ohm_app , stopwatch_app , temp_app , linux_app
#from PyQt
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton  , QAction , QMessageBox
import PyQt5.uic 
class app (QMainWindow) :
    "Main Application GUI ( parent=None )"
    def __init__ (self,parent=None) :
        super().__init__(parent)
        self.title = "Collections"
        self.left , self.top , self.width , self.height  = 100 , 100 , 270 , 350

        #imported object that will run without repeat
        self.lic = license_app.license(self.title +" [License]", self)  #license window
        self.ohm = ohm_app.ohm_gui(self.title + " [Ohm Calculations]",self)
        self.stopwatch = stopwatch_app.stopwatch_gui(self.title + "[ Stopwatch]",self)
        self.temp = temp_app.temp_gui(self.title + " [Temperature conversions]", self )
        self.linux = linux_app.linux_gui(self.title+" [Linux Chmod Calculator]",self)

    def initUI (self) :
        "main window"
        self.setWindowTitle(self.title)
        self.setGeometry(self.left , self.top , self.width , self.height)
        self.setMaximumHeight(self.height)
        self.setMinimumHeight(self.height)
        self.setMaximumWidth(self.width)
        self.setMinimumWidth(self.width)

        self.menu_bar()
        self.buttons()
        self.show()

    def menu_bar(self):
        "menu bar for main window"
        #file actions
        new_action = QAction("New",self)
        new_action.setShortcut("Ctrl+n")
        new_action.triggered.connect(self.new_window)

        exit_action = QAction("Exit",self)
        exit_action.setShortcut("Ctrl+w")
        exit_action.triggered.connect(self.close)

        #about actions
        source_action = QAction("License",self)
        source_action.triggered.connect(self.show_license)

        about_action = QAction("About",self)
        about_action.triggered.connect(self.about_app)

        #menu
        menu = self.menuBar()
        file = menu.addMenu("&File")
        file.addAction(new_action)
        file.addAction(exit_action)
        about = menu.addMenu("&About")
        about.addAction(source_action)
        about.addAction(about_action)

    def buttons (self):
        "main menu buttons"
        tip_text = "Run or Reset"
        angels = QPushButton("Angels",self)
        angels.move(20,40)
        angels.setToolTip(tip_text)
        
        temp = QPushButton("Temperature",self)
        temp.move(150,40)
        temp.clicked.connect(self.temp_button)
        temp.setToolTip(tip_text)
       
        astro = QPushButton("Astronimical",self)
        astro.move(20,90)
        astro.setToolTip(tip_text)
        
        ohm = QPushButton("Ohm Law",self)
        ohm.move(150,90)
        ohm.setToolTip(tip_text)
        ohm.clicked.connect(self.ohm_button)
        
        char = QPushButton("Characters",self)
        char.move(20,140)
        char.setToolTip(tip_text)
        
        linux = QPushButton("Linux chmod",self)
        linux.move(150,140)
        linux.setToolTip(tip_text)
        linux.clicked.connect(self.linux_button)
        
        length = QPushButton("Lengths",self)
        length.move(20,190)
        length.setToolTip(tip_text)
        
        volume = QPushButton("Volumes",self)
        volume.move(150,190)
        volume.setToolTip(tip_text)
        
        stopwatch = QPushButton("StopWatch",self)
        stopwatch.move(20,240)
        stopwatch.setToolTip(tip_text)
        stopwatch.clicked.connect(self.stopwatch_button)
        
        timer = QPushButton("Timer",self)
        timer.move(150,240)
        timer.setToolTip(tip_text)

        quit_ = QPushButton("Quit",self)
        quit_.move(80,300)
        quit_.setToolTip("Exit")
        quit_.setStyleSheet("background:red;color:white")
        quit_.clicked.connect(self.close)

    #actions for menu bar
    #file > new
    def new_window(self):
        new_win = app(self)
        new_win.setStyleSheet("background:gray")
        new_win.left , new_win.top = 200,200
        new_win.initUI()

   #about > license
    def show_license (self):
        self.lic.initUI()

    def about_app (self):
        QMessageBox.about(self,self.title+" [About App]","Practice with PyQt5 \nEmail me : Khaledfathi@protonmail.com")

    #support methods
    def load_and_reset (self,old_obj,new_obj,title , parent):
        "load GUI of specific app or reset it , and protect it from repeating \
        ( old_obj : target object , new_obj : import new class , title : window title , parrent : parent widget)"
        try :
            old_obj.close()
            del old_obj
            old_obj = new_obj(title,parent)
            old_obj.initUI()
            return old_obj
        except Exception as e :
            old_obj.initUI()
                    
    #action for buttons
    def ohm_button (self):
        "run dialog [ohm application]"
        self.ohm = self.load_and_reset(self.ohm , ohm_app.ohm_gui , self.title + " [Ohm Calculator ]" , self)
        
    def stopwatch_button (self):
        "run dailoge [stopwatch]"
        self.stopwatch = self.load_and_reset(self.stopwatch , stopwatch_app.stopwatch_gui ,  self.title + " [Stopwatch]",self)
    
    def temp_button (self):
        "run dailog [Temperature]"
        self.temp = self.load_and_reset(self.temp , temp_app.temp_gui , self.title + " [Temperature]" , self)
        
    def linux_button (self):
        "run dailog [Linux chmod]"
        self.linux = self.load_and_reset(self.linux , linux_app.linux_gui , self.title + " [Linux chmod Calculator]" , self)
        
def run_app ():
    "Run application Main GUI window"
    APP = QApplication(sys.argv)
    ex = app()
    ex.initUI()
    sys.exit(APP.exec_())

if __name__ == "__main__" :
    run_app()