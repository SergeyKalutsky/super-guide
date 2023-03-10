from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout
from inst import txt_title, win_height, win_width, win_x, win_y

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        # self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def initUI(self):
        self.line_name = QLineEdit('Ф.И.О')
        self.line_age = QLineEdit('0')
        self.line_test1 = QLineEdit('0')
        self.line_test1 = QLineEdit('0')
        self.line_test3 = QLineEdit('0')
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        
        self.text1 = QLabel(sdjnfksnfn)
        self.text2 = QLabel(dsfgdgfsg)
        self.button1 = QPushButton(dfgdsgsdg)
        self.button2 = QPushButton(dfgdsgsdg)
        self.button3 = QPushButton(dfgdsgsdg)
        self.button4 = QPushButton(dfgdsgsdg)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text1)
        self.layout.addWidget(self.text2)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.setLayout(self.layout)
