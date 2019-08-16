import time  , threading
from PyQt5.QtWidgets import QDialog , QLabel , QPushButton , QSpinBox  
from PyQt5.QtGui import QFont

class timer_gui (QDialog) :
  "Dailod (title : str , parent=None)"
  def __init__(self,title , parent=None) :
    super().__init__(parent)
    self.title = title 
    self.left , self.top , self.width , self.height = 200,100,250,250
    
    #for timer_loop_thred
    self.thread_flag = 0 #thread flag 1 for runing 0 for not runing , protect from repeating 
    
  def initUI(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left , self.top , self.width , self.height)
    
    self.labels()
    self.data_entry()
    self.buttons()
    
    #i put it here (after label) , because i want to pass the Qlable into it  
    self.timer_thread = time_loop_thread(self.res) 
    
    self.show()
    
  def labels (self):
    "All window labels "
    lb_hr = QLabel("Hours",self)
    lb_hr.move(20,35)
    lb_mn = QLabel("Minutes" , self)
    lb_mn.move(90,35)
    lb_sc = QLabel ("Seconds",self)
    lb_sc.move(170,35)
    
    self.res = QLabel("00 : 00 : 00",self)
    self.res.move(20,65)
    self.res.setFont(QFont("Time", 25))
    
    
  def data_entry (self):
    "All Window entry fields"
    self.hr_value = QSpinBox(self)
    self.hr_value.setGeometry(20,65,50,40)
    self.hr_value.setMaximum(99)
    self.hr_value.setToolTip("max 99")
    self.mn_value = QSpinBox(self)
    self.mn_value.setGeometry(95,65,50,40)
    self.mn_value.setMaximum(59)
    self.mn_value.setToolTip("max 59")
    self.sc_value = QSpinBox(self)
    self.sc_value.setGeometry(170,65,50,40)
    self.sc_value.setMaximum(59)
    self.sc_value.setToolTip("max 59")
    
  def buttons (self):
    "All Window Buttons"
    self.start_button = QPushButton("Start", self)
    self.start_button.move(20,140)
    self.start_button.setToolTip("Start or Continue")
    self.start_button.clicked.connect(self.run_start_button)
    
    self.pause_button = QPushButton("Pause", self)
    self.pause_button.move(20,170)
    self.pause_button.setToolTip("Pause")
    self.pause_button.clicked.connect(self.run_pause_button)
    
    self.cancel_button = QPushButton("Cancle",self) 
    self.cancel_button.move(120,140)
    self.cancel_button.setToolTip("Cancel and Reset")
    self.cancel_button.clicked.connect(self.run_cancel_button)
    
    self.quit_button=QPushButton("Quit",self)
    self.quit_button.move(120,170)
    self.quit_button.setToolTip("Exit")
    self.quit_button.setStyleSheet("background:red;color:white")
    self.quit_button.clicked.connect(self.rune_quit_button)
  
  ##################
  ## Slot methods ##
  ##################
  def run_start_button(self):
    "slot for start button"
    self.hide_show_inputs(True)
    if not self.thread_flag :
      self.thread_flag=1
      self.timer_thread.hr = self.hr_value.value() 
      self.timer_thread.mn = self.mn_value.value()
      self.timer_thread.sc = self.sc_value.value()
      try :
        self.timer_thread.start()
      except :
        self.reconfig_timer_loop_thread ( self.res , self.hr_value.value(),self.mn_value.value(),self.sc_value.value())
        self.timer_thread.start()
  
  def run_pause_button(self):
    "slot for pause button"
    self.thread_flag=0
    self.timer_thread.flag=0
    
    self.hr_value.setValue (self.timer_thread.hr)
    self.mn_value.setValue (self.timer_thread.mn)
    self.sc_value.setValue (self.timer_thread.sc)
    self.reconfig_timer_loop_thread (self.res , self.hr_value.value(),self.mn_value.value(),self.sc_value.value())
    
  def run_cancel_button(self):
    "slot for cancel button"
    self.thread_flag=0
    self.timer_thread.flag=0
    
    self.hr_value.setValue (0)
    self.mn_value.setValue (0)
    self.sc_value.setValue (0)
    self.hide_show_inputs(False)
    
    self.reconfig_timer_loop_thread (self.res , self.hr_value.value(),self.mn_value.value(),self.sc_value.value())
  
  def rune_quit_button(self):
    "slot for quit button"
    self.timer_thread.flag=0
    self.close()
    
  ##################
  ## core methods ##
  ##################
  def reconfig_timer_loop_thread (self, res  , hr, mn , sc ):
    "( thread_obj : object , res : Qlabel , hr : int , mn : int , sc : int)\
    preconfigure timer_loop_thred , delete object and recreate it "
    del self.timer_thread
    self.timer_thread = time_loop_thread(self.res , hr, mn,sc )
  
  def hide_show_inputs (self,stat):
    "(stat : bool)\
    hidden or show inputs True =  hide , False = shoe " 
    self.hr_value.setHidden(stat)
    self.mn_value.setHidden(stat)
    self.sc_value.setHidden(stat)


######################
## thread for timer ##
######################
class time_loop_thread (threading.Thread) :
  "New Thread for timer ( res=None : QLabel , hr=0 , mn=0 , sec=0 )"
  def __init__(self, res , hr=0, mn=0 , sc=0):
    super().__init__()
    self.hr , self.mn , self.sc , self.res ,self.flag = hr , mn , sc ,res , 1
  
  def make_00 (self, *arg):
    "Reruen result [hr , mn , sc] 2 digits like this '02' insted of '2' "
    data = ["0"+str(i) if i < 10 else str(i) for i in arg ]
    return data[0] + " : " + data[1] + " : " + data[2]
  
        
  def run (self) :
    "start thread by using inhertance method 'start' "
    while self.flag :
      if self.hr == 0  and self.mn == 0 and self.sc == 0 :
        self.res.setText(self.make_00(self.hr , self.mn , self.sc))
        #notify by blinking red/black/white color 
        change = 3
        while self.flag :
          if change == 1:
            change = 2
            self.res.setStyleSheet("background:red")
            time.sleep(0.5)
          elif change == 2 :
            change = 3
            self.res.setStyleSheet("background:green")
            time.sleep(0.5)
          else :
            change = 1
            self.res.setStyleSheet("background:blue")
            time.sleep(0.5)
        self.res.setStyleSheet("color:black") # make color black , prevent loop color effect 
        break
      now = self.res.setText(self.make_00(self.hr , self.mn , self.sc))
      self.sc-=1
      if self.sc < 0 :
        self.sc = 59
        self.mn-=1
        if self.mn == 0 :
          self.mn = 0
      if self.mn < 0 and self.hr > 0:
        self.mn = 59
        self.hr -=1
      if self.hr < 0 :
        self.hr = 0
      time.sleep(1)

    
    
    
  