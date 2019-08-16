from PyQt5.QtWidgets import QDialog , QLabel , QPushButton , QComboBox ,\
     QTextBrowser , QDoubleSpinBox 

class temp_gui (QDialog):
    "temp gui dialog ( parent=None )"
    def __init__(self,title,parent=None):
        super().__init__(parent)
        self.title = title
        self.left , self.top , self.width , self.height = 200,100,370,280 
    
    def initUI (self):
        "main app window"
        self.setWindowTitle(self.title)
        self.setGeometry(self.left , self.top , self.width , self.height)
        
        #gui component
        self.labels()
        self.inputs()
        self.buttons()
        self.combo_boxes()
        self.text_browse()
        
        self.show()
        
    def labels (self):
        "All window labels"
        "labels widgets"
        lb_temp = QLabel("Temperature",self)
        lb_temp.move(20,50)
        self.lb_unit = QLabel ("Celsius",self)
        self.lb_unit.move(250,50)
        lb_from = QLabel("From",self)
        lb_from.move(30,110)
        lb_to = QLabel("To",self)
        lb_to.move(195,110)
        
    def inputs (self) :
        "All window Inputs"
        self.value = QDoubleSpinBox (self)
        self.value.setMinimum(-273.15)
        self.value.setMaximum(999999999)
        self.value.setDecimals(4)
        self.value.setGeometry(120,42,115,30)
        pass
        
    def buttons(self):
        "All buttons widgets"
        convert_button = QPushButton("Convert",self)
        convert_button.move(90,220)
        convert_button.clicked.connect(self.calc_button)
        quit_button = QPushButton("Quit",self)
        quit_button.move(190,220)
        quit_button.setStyleSheet("background:red;color:white")
        quit_button.clicked.connect(self.close)

    def combo_boxes (self) :
        "All window combo_boxs"
        self.from_list = QComboBox(self)
        self.from_list.move(80,105)
        self.from_list.addItem("Celsius")
        self.from_list.addItem("fahrenheit")
        self.from_list.addItem("kelvin")
        self.from_list.currentIndexChanged.connect(self.check_box_select)
        
        self.to_list = QComboBox(self)
        self.to_list.move(240,105)
        self.to_list.addItem("Celsius")
        self.to_list.addItem("fahrenheit")
        self.to_list.addItem("kelvin")
   
    def text_browse(self):
        "show result as a text"
        self.result = QTextBrowser(self)
        self.result.setText("TEST TEXT BROWSER")
        self.result.setGeometry(50,150,250,40)
    
    #############
    ## actions ##
    #############
    def check_box_select(self) :
        "change unit text while changing the from list "
        self.lb_unit.setText(self.from_list.currentText())
        
    def calc_button(self):
        "action when clicked to convert button"
        self.result.setText ( str(self.calc(float(self.value.text()),self.selections())) )
    
    ##################
    ## core methods ##
    ##################
    def selections (self):
        "Effect when change selection -> [QComboBox] Widget"
        marks ={0:"c",1:"f",2:"k"}
        return marks [self.from_list.currentIndex()] + marks[self.to_list.currentIndex()]
        
    #calculations
    def calc ( self ,temp , from_to ):
        "calculation methods (temp : float , from_to : str )"
        #each letter maen [f = fahrenheit , c = celsius , k = kelvin] ,
        #each pair like ck  mean convert from c to k 
        if from_to[0] == from_to[1]:
            return temp
        calculations = {
        "cf" : (1.8*temp)+32,\
        "ck" : temp+273.15,\
        "fc" : (temp-32)/1.8,\
        "fk" : (((temp-32)*5)/9)+32,\
        "kc" : temp-273.15 ,\
        "kf" : (((temp-273.15)*9)/5)+32
        }
        return calculations[from_to]
    
