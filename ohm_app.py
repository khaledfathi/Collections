import sys , os
from math import sqrt
from datetime import datetime
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton ,\
     QLabel , QRadioButton , QComboBox , QMessageBox , QHBoxLayout , QVBoxLayout,\
      QGroupBox , QLineEdit 
from PyQt5.QtGui import QFont 

############
# GUI QT 5 #
############

class ohm_gui (QMainWindow) :
    "the whole app GUI"
    def __init__ (self,title , parent=None):
        "__init__ function"
        super().__init__(parent)
        self.title = title
        self.left = 100
        self.top = 100
        self.width = 770
        self.height = 300
        
    def initUI (self):
        "Initilization UI "
        self.setGeometry(self.left , self.top , self.width , self.height)
        self.setWindowTitle(self.title)
        self.setMinimumWidth(self.width)
        self.setMinimumHeight(self.height)
        self.setMaximumWidth(self.width)
        self.setMaximumHeight(self.height)
        self.statusBar().showMessage("result logs saved on : " + str(os.getcwd())+"/results.txt")
        
        self.inputs()
        self.selection()
        self.buttons()
        
        self.show()

    def inputs (self):
        "inputs section"
        self.lb1 = QLabel("------", self)
        self.lb1.setGeometry (15,30,100,22)
        self.lb2 = QLabel("------",self)
        self.lb2.setGeometry(15,70,100,22)
        
        self.value1 = QLineEdit(self)
        self.value1.setGeometry (100,30,100,22)
        self.value1.setToolTip("Number Only")
        self.value1.setDisabled(True)
        self.value2 = QLineEdit(self)
        self.value2.setGeometry (100,70,100,22)
        self.value2.setToolTip("Number Only")
        self.value2.setDisabled(True)
        
        self.res = QLabel("Res = ------ " ,self)
        self.res.setFont(QFont("Time", 14))
        self.res.setStyleSheet("color:red;")
        self.res.setGeometry(10,190,500,100)
        
    def selection (self):
        "selection section"
        #radio button [select the lost value]
        self.resistance = QRadioButton ("Resistance")
        self.resistance.clicked.connect(self.select_option)
        self.voltage = QRadioButton ("Voltage")
        self.voltage.clicked.connect(self.select_option)
        self.current = QRadioButton ("Current")
        self.current.clicked.connect(self.select_option)
        self.power = QRadioButton ("Power")
        self.power.clicked.connect(self.select_option)
        
        #combo box [for select value to calculate]
        self.get_resistance = QComboBox()
        self.get_resistance.addItems(["Voltage and current","Voltage and Power","Current and Power"])
        self.get_resistance.setMaximumWidth(200)
        self.get_resistance.setHidden(True)
        self.get_resistance.currentIndexChanged.connect(self.select_sub_option)
        self.get_resistance.currentIndexChanged.connect(self.clear_by_sub_options)
        
        self.get_voltage = QComboBox ()
        self.get_voltage.addItems(["Resistance and Current","Resistance and Power","Current and Power"])
        self.get_voltage.setMaximumWidth(200)
        self.get_voltage.setHidden(True)
        self.get_voltage.currentIndexChanged.connect(self.select_sub_option)
        self.get_voltage.currentIndexChanged.connect(self.clear_by_sub_options)
        
        self.get_current = QComboBox ()
        self.get_current.addItems(["Voltage and Resistance","Vlotage and Power","Resistance and Power"])
        self.get_current.setMaximumWidth(200)
        self.get_current.setHidden(True)
        self.get_current.currentIndexChanged.connect(self.select_sub_option)
        self.get_current.currentIndexChanged.connect(self.clear_by_sub_options)
        
        self.get_power = QComboBox ()
        self.get_power.addItems(["Voltage and Current","Voltage and Resistance","Current and Resistance"])
        self.get_power.setMaximumWidth(200)
        self.get_power.setHidden(True)
        self.get_power.currentIndexChanged.connect(self.select_sub_option)
        self.get_power.currentTextChanged.connect(self.clear_by_sub_options)
        
        #units 
        self.unit_normal = QRadioButton ("Normal")
        self.unit_normal.setChecked(True)
        self.unit_normal.clicked.connect(self.change_unit)
        self.unit_kilo = QRadioButton ("Kilo")
        self.unit_kilo.clicked.connect(self.change_unit)
        self.unit_mega = QRadioButton ("Mega")
        self.unit_mega.clicked.connect(self.change_unit)
        self.unit_giga = QRadioButton ("Giga")
        self.unit_giga.clicked.connect(self.change_unit)
        self.unit_tera = QRadioButton ("Tera")
        self.unit_tera.clicked.connect(self.change_unit)
        
        #layouts
        main_select = QHBoxLayout ()
        main_select.addWidget (self.resistance)
        main_select.addWidget (self.voltage)
        main_select.addWidget (self.current)
        main_select.addWidget (self.power)
        
        main_selections = QGroupBox ("Select Lost Value" ,self)
        main_selections.setGeometry (300,5,350,100)
        main_selections.setLayout (main_select)
        
        options = QHBoxLayout ()
        options.addWidget (self.get_resistance)
        options.addWidget (self.get_voltage)
        options.addWidget (self.get_current)
        options.addWidget (self.get_power)
        
        
        all_options = QGroupBox("Get by", self)
        all_options.setGeometry(300,110,350,100)
        all_options.setLayout(options)
        
        units = QVBoxLayout ()
        units.addWidget (self.unit_normal)
        units.addWidget (self.unit_kilo)
        units.addWidget (self.unit_mega)
        units.addWidget (self.unit_giga)
        units.addWidget (self.unit_tera)
        
        all_units = QGroupBox("Result unit",self)
        all_units.setGeometry(660,5,100,205)
        all_units.setLayout(units)
                
    def buttons (self):
        self.calc = QPushButton ("Calc",self)
        self.calc.move(70,110)
        self.calc.setToolTip("Calculate Values")
        self.calc.setDisabled(True)
        self.calc.clicked.connect(self.run_calc)
        
        self.clear = QPushButton("Clear" , self)
        self.clear.move(70,150)
        self.clear.setToolTip("Clear feilds and results")
        self.clear.setDisabled(True)
        self.clear.clicked.connect(self.clear_input)
        
        about = QPushButton ("About",self)
        about.move(530,250)
        about.clicked.connect(self.about_app)
        
        quit_ = QPushButton ("Quit",self)
        quit_.move(650,250)
        quit_.setToolTip("Exit")
        quit_.setStyleSheet("background:red;color:white")
        quit_.clicked.connect(self.close_app)
        
    #*****************
    # OPTIONS ACTION *
    #*****************
    
    def enable_all (self):
        "enable inputs and calc button"
        self.value1.setDisabled(False)
        self.value2.setDisabled(False)
        self.calc.setDisabled(False)
        self.clear.setDisabled(False)
    
    def unhide (self , resistance=True , voltage=True , current=True, power=True):
        "exchange hide and unhide option for each selection , [ used by another function ]"
        self.get_resistance.setHidden(resistance)
        self.get_voltage.setHidden(voltage)
        self.get_current.setHidden(current)
        self.get_power.setHidden(power)
    
    def type_checked (self):
        "return the label of the current type options checked"
        if self.resistance.isChecked():
            return self.resistance.text()
        elif self.voltage.isChecked():
            return self.voltage.text()
        elif self.current.isChecked():
            return self.current.text()
        elif self.power.isChecked():
            return self.power.text()

    def clear_input(self):
        self.res.setText("Res = ------ ")
        self.value1.clear()
        self.value2.clear()
    
    def unit_value (self) :
        if self.unit_normal.isChecked():
            return "normal"
        elif self.unit_kilo.isChecked():
            return "kilo"
        elif self.unit_mega.isChecked():
            return "mega"
        elif self.unit_giga.isChecked():
            return "giga"
        elif self.unit_tera.isChecked():
            return "tera"
    
            
    #******************
    # SLOTS FUNCTIONS *
    #******************
    def select_option (self):
        "man select [Radio buttons] chose Resistance | Voltage | Current | Power \
        to perparing the calculations"
        self.enable_all()
        self.clear_input()
        if self.resistance.isChecked() :
            self.unhide(resistance=False)
        elif self.voltage.isChecked():
            self. unhide(voltage=False)
        elif self.current.isChecked():
            self.unhide(current=False)
        elif self.power.isChecked():
            self.unhide(power=False)
        self.select_sub_option()
    
    def select_sub_option (self):
        "sub option for each main option , this function return status of what is main select \
        and what is the option , return output in dictionary form"
        if self.resistance.isChecked ():
            if self.get_resistance.currentIndex() == 0 :
                self.lb1.setText ("Voltage")
                self.lb2.setText ("Current")
            elif self.get_resistance.currentIndex () == 1 :
                self.lb1.setText ("Voltage")
                self.lb2.setText ("Power")
            elif self.get_resistance.currentIndex () == 2 :
                self.lb1.setText ("Current")
                self.lb2.setText ("Power")
            status = {"type":"resistance", "option":self.get_resistance.currentIndex()}
        elif self.voltage.isChecked ():
            if self.get_voltage.currentIndex () == 0 :
                self.lb1.setText("Resistance")
                self.lb2.setText("Current")
            elif self.get_voltage.currentIndex () == 1 :
                self.lb1.setText("Resistance")
                self.lb2.setText("Power")
            elif self.get_voltage.currentIndex () == 2 :
                self.lb1.setText("Current")
                self.lb2.setText("Power")
            status = {"type":"voltage", "option":self.get_voltage.currentIndex()}
        elif self.current.isChecked ():
            if self.get_current.currentIndex () == 0 :
                self.lb1.setText("Voltage")
                self.lb2.setText("Resistance")
            if self.get_current.currentIndex () == 1 :
                self.lb1.setText("Voltage")
                self.lb2.setText("Power")
            if self.get_current.currentIndex () == 2 :
                self.lb1.setText("Resistance")
                self.lb2.setText("Power")
            status = {"type":"current", "option":self.get_current.currentIndex()}
        elif self.power.isChecked ():
            if self.get_power.currentIndex () == 0 :
                self.lb1.setText("Voltage")
                self.lb2.setText("Current")
            if self.get_power.currentIndex () == 1 :
                self.lb1.setText("Voltage")
                self.lb2.setText("Resistance")
            if self.get_power.currentIndex () == 2 :
                self.lb1.setText("Current")
                self.lb2.setText("Resistance")
            status = {"type":"power", "option":self.get_power.currentIndex()}
        return status
    
    def clear_by_sub_options (self):
        self.value1.clear()
        self.value2.clear()
        self.res.setText("Res = ------ ")
    
    def change_unit(self):
        self.run_calc()
        
    def close_app (self):
        "close application"
        self.close()
        
    def about_app (self):
        "application description"
        QMessageBox().about(self,"About Application" , "OLC [Ohm Law Calc] Version 0.2 \n\n\
        Simple Application to calculate the whole Ohm law \n\n\
        [ Resistance | Voltage | Current | Power ]\n\n\
        Khaledfathi@protonmail.com")
    
    def run_calc (self):
        "run Ohm Law Calculation and set the result in the main window"
        v1_string = self.value1.text()
        v2_string = self.value2.text()
        if not v1_string and not v2_string : #do not nothing if theres input and clicked on calc button
            self.res.setText("Res = ------")
            return 
        try : #try to convert input to float , if not show error
            v1 = float(v1_string)
            v2 = float(v2_string)
        except Exception as e :
            error = "ERROR : Enter Only Numbers"
            with open ("result.txt", "a") as f : #save on log file
                f.write("\n--------\n\n" + str(datetime.now()) + "\n" + self.lb1.text() + " = " + self.value1.text() + "\n" + self.lb2.text() + " = " + self.value2.text() + "\n" + error + "\nCode : " + str(e))
            self.res.setText(error)
            return 
        type_ = self.select_sub_option()["type"] 
        option = self.select_sub_option()["option"]
        #Ohm calculator 
        try: #run calcularion from ohm class , and check the result , if something wrong > show error and save on log file
            self.final= ohm(type_ , option , v1 , v2 ).calc_res() #return (result , 4th result , name of 4th result)
            unit = self.unit_value()
            if unit == "normal":
                result_text = self.type_checked() + " = " + str(round(self.final[0], 10)) + self.final[3]+ "\n" + str(self.final[2]) + " = " +  str(round(self.final[1], 8)) + self.final[4]
            elif unit == "kilo" :
                result_text = self.type_checked() + " = " + str(round(self.final[0]/1000, 10)) + " Kilo" + self.final[3] + "\n" + str(self.final[2]) + " = " +  str(round(self.final[1]/1000, 8)) + " Kilo" + self.final[4]
            elif unit == "mega" :
                result_text = self.type_checked() + " = " + str(round(self.final[0]/1000000, 10)) + " Mega" + self.final[3] + "\n" + str(self.final[2]) + " = " +  str(round(self.final[1]/1000000, 8)) + " Mega" + self.final[4]
            elif unit == "giga" :
                result_text = self.type_checked() + " = " + str(round(self.final[0]/1000000000, 10)) + " Giga" + self.final[3] + "\n" +str(self.final[2]) + " = " +  str(round(self.final[1]/1000000000, 8)) + " Giga" + self.final[4]
            elif unit == "tera" :
                result_text = self.type_checked() + " = " + str(round(self.final[0]/1000000000000, 10)) +  " Tera" + self.final[3] + "\n" + str(self.final[2]) + " = " +  str(round(self.final[1]/1000000000000, 8)) + " Tera" + self.final[4]
            with open ("result.txt", "a") as f :
                f.write("\n--------\n\n" + str(datetime.now()) + "\n" + self.lb1.text() + " = " + self.value1.text() + "\n" + self.lb2.text() + " = " + self.value2.text() + "\n" + result_text)
            self.res.setText(result_text)
        except Exception as e:
            error = "Math Error : Can not dived zero" 
            with open ("result.txt", "a") as f :
                f.write("\n--------\n\n" + str(datetime.now()) + "\n" + self.lb1.text() + " = " + self.value1.text() + "\n" + self.lb2.text() + " = " + self.value2.text() + "\n" + error + "\nCode : " + str(e))
            self.res.setText( error )

#############
# Ohm Class #
#############

class ohm :
    "Ohm calculations and results object"
    def __init__ (self,type_,option,value1 ,value2):
        self.type_ = type_ 
        self.option = option
        self.v1 = value1
        self.v2 = value2
    
    def resistance_vi (self, v,i) :
        "get resistance by volt and current"
        return v/i
    def resistance_vp (self, v,p) :
        "get resistance by volt and power"
        return (v**2)/p
    def resistance_ip (self, i,p) :
        "get resistance by current and power"
        return p/(i**2)

    def voltage_ri (self, r,i) :
        "get voltage by resistance and current"
        return r*i
    def voltage_rp (self, r,p) :
        "get voltage by resistance and power"
        return sqrt(p*r)
    def voltage_ip (self, i,p) :
        "get voltage by current and power"
        return p/i
    
    def current_vr (self, v,r) :
        "get current by voltage and resistance"
        return v/r
    def current_vp (self, v,p) :
        "get current by voltage and power "
        return p/v
    def current_rp (self, r,p) :
        "get current bu resistance and power"
        return sqrt(p/r)
   
    def power_vi (self, v,i) :
        "get power by voltage and current"
        return v*i
    def power_vr (self, v,r) :
        "get power by voltage and resistance "
        return (v**2)/r
    def power_ir (self, i,r) :
        "get power by current and resistance"
        return (i**2)/r
    
    def calc_res (self) :
        "return list for [result calculation , find and calculate lost value , text for lost type]"
        if self.type_ == "resistance" and self.option == 0:
            return self.resistance_vi(self.v1,self.v2), self.power_vi(self.v1,self.v2) , "Power" , " Ohm" , " Watt"
        elif self.type_ == "resistance" and self.option == 1:
            return self.resistance_vp (self.v1,self.v2), self.current_vp(self.v1,self.v2) , "Current" , " Ohm" , " Amp"
        elif self.type_ == "resistance" and self.option == 2:
            return self.resistance_ip(self.v1,self.v2) , self.voltage_ip(self.v1,self.v2) , "Voltage" , " Ohm" ," Volt"
        
        elif self.type_ == "voltage" and self.option == 0:
            return self.voltage_ri(self.v1,self.v2) , self.power_ir(self.v1,self.v2) , "Power" , " Volt" , " Watt"
        elif self.type_ == "voltage" and self.option == 1:
            return self.voltage_rp(self.v1,self.v2) , self.current_rp (self.v1,self.v2) , "Current" , " Volt" , " Amp"
        elif self.type_ == "voltage" and self.option == 2:
            return self.voltage_ip(self.v1,self.v2) , self.resistance_ip(self.v1,self.v2), "Resistance" ," Volt" , " Ohm"
        
        elif self.type_ == "current" and self.option == 0:
            return self.current_vr(self.v1,self.v2) , self.power_vr(self.v1,self.v2), "Power" , " Amp" ," Watt"
        elif self.type_ == "current" and self.option == 1:
            return self.current_vp(self.v1,self.v2) , self.resistance_vp(self.v1,self.v2), "Resistance" , " Amp" , " Ohm"
        elif self.type_ == "current" and self.option == 2:
            return self.current_rp(self.v1,self.v2) , self.voltage_rp (self.v1,self.v2) , "Voltage" , " Amp"," Volt"
        
        elif self.type_ == "power" and self.option == 0:
            return self.power_vi(self.v1,self.v2) , self.resistance_vi (self.v1,self.v2) , "Resistance" , "Watt" , " Ohm"
        elif self.type_ == "power" and self.option == 1:
            return self.power_vr(self.v1,self.v2) , self.current_vr (self.v1,self.v2) , "Current" , " Watt" , " Amp"
        elif self.type_ == "power" and self.option == 2:
            return self.power_ir(self.v1,self.v2) , self.voltage_ri(self.v1,self.v2), "Voltage" , " Watt" , " Volt"

