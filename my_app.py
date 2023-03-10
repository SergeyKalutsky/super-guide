from PyQt5.QtWidgets import QWidget

class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()# устанавливает, как будет выглядеть окно
    self.initUI() # создаём и настраиваем графические элементы
    self.connects() # устанавливает связи между элементами
    self.show() # старт
