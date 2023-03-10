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
        
