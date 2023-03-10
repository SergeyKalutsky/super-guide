from PyQt5.QtWidgets import QWidget
from inst import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()  # устанавливает, как будет выглядеть окно
        self.initUI()  # создаём и настраиваем графические элементы
        self.connects()  # устанавливает связи между элементами
        self.show()  # старт


    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(): 
        pass
    def connects(): 
        pass
