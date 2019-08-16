from PyQt5.QtWidgets import  QDialog,  QLabel , QPushButton , QCheckBox , QTextBrowser 
import PyQt5.QtCore


class linux_gui (QDialog) :
   "linux Gui dialog (title , parent=None)"
   def __init__(self , title , parent=None) :
      super().__init__(parent)
      self.title = title
      self.left , self.top , self.width , self.height = 200,100,370,300
      
   def initUI (self) :
      "main window"
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top , self.width , self.height)
      
      #component 
      self.labels()
      self.check_boxs()
      self.buttons()
      self.text_browser()
      
      self.show()
   
   def labels(self):
      "All window labels"
      user = QLabel("User" , self)
      user.move(20,20)
      group = QLabel("Group" , self)
      group.move(20,53)
      others = QLabel("Others" , self)   
      others.move(20,87)
      
   def check_boxs (self):
      "All window checkboxs"
      self.checks = [
      #for user/owner
      [QCheckBox("Read [r]" , self), QCheckBox("Write [w]" , self), QCheckBox("Execute [x]" , self)] ,\
      #for groups
      [QCheckBox("Read [r]" , self), QCheckBox("Write [w]" , self), QCheckBox("Execute [x]" , self)],\
      #for others 
      [QCheckBox("Read [r]" , self), QCheckBox("Write [w]" , self), QCheckBox("Execute [x]" , self)]
      ]
      
      self.checks[0][0].move(70,15)
      self.checks[0][1].move(150,15)
      self.checks[0][2].move(240,15)
      
      self.checks[1][0].move(70,50)
      self.checks[1][1].move(150,50)
      self.checks[1][2].move(240,50)
      
      self.checks[2][0].move(70,85)
      self.checks[2][1].move(150,85)
      self.checks[2][2].move(240,85)

         
   def buttons(self):
      "All window buttons "
      calc_button = QPushButton("Calc",self)
      calc_button.move(40,250)
      calc_button.clicked.connect(self.calc)
      
      clear_button =QPushButton("Clear" , self)
      clear_button.move(140,250)
      clear_button.clicked.connect(self.clear)
      
      quit_button = QPushButton("Quit",self)
      quit_button.move(240,250)
      quit_button.setStyleSheet("background:red;color:white")
      quit_button.clicked.connect(self.close)
      
   def text_browser(self):
      "textbrowser widget | Result showen as text browser "
      self.result = QTextBrowser(self)
      self.result.setStyleSheet("font-size:16px")
      self.result.setGeometry(20,120 , 310 , 100)

   
   #button actions
   def clear (self) :
      "clear button action "
      self.result.setText("")
      for ugo in self.checks : #ugo mean user , group , others
         for i in ugo:
            i.setChecked(False)

   
   def calc (self):
      "calc button action "
      res_number , res_character = [] , []
      for ugo in self.checks : #ugo mean user , group , others
         check , chmod , character = [4,2,1] , 0 , {0:"---" , 1:"--x",2:"-w-",3:"-wx",4:"r--",5:"r-x",6:"wr-",7:"rwx"}
         for index , i in enumerate(ugo) :
            if i.isChecked():
               chmod +=  check[index]
         res_character .append(character[chmod])
         res_number.append(chmod)
         check = 0
      
      #reformat res 
      self.result.setText("\nNumber Code\t" + "".join( [str(i) for i in res_number]) +\
                          "\n" + "Attributes\t\t" + "".join(res_character))