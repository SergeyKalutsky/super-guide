from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication
from inst import txt_title, win_height, win_width, win_x, win_y, txt_hello, txt_instruction, txt_next
from second_win import TestWin

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

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

    def connects(self):
        pass

app = QApplication([])
mw = MainWin()
app.exec_()
