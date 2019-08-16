from PyQt5.QtWidgets import QDialog , QPushButton , QLabel , QTextBrowser 
from PyQt5.Qt import Qt

class license (QDialog) :
    "License Dialog (title : str , parent=None)"
    def __init__(self,title ,parent=None) :
        super().__init__(parent)
        self.title=title
    
    def initUI (self):
        "main window"
        self.setWindowTitle(self.title)
        self.setGeometry(200,100,400,500)
        
        self.labels()
        self.buttons()
        self.text_browse()
        self.show()
    
    def labels (self):
        "all window's labels"
        lb = QLabel("License : GPL V3",self)
        lb.setGeometry(0,0,400,50)
        lb.setAlignment(Qt.AlignCenter)
        lb.setStyleSheet("font-size:20px")
        
    def buttons (self):
        "all window's buttons"
        close_button = QPushButton("Close",self)
        close_button.move(150,450)
        close_button.setStyleSheet("background:red;color:white")
        close_button.clicked.connect(self.close)
        
    def text_browse(self):
        "text_browser for showing result"
        text = QTextBrowser(self)
        text.setGeometry(10,40,380,400)
        with open ("LICENSE","r") as f:
            text.setText(f.read())