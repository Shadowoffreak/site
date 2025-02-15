from PyQt6 import QtWidgets, QtGui
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Содержимое страницы")
        self.button = QtWidgets.QPushButton(
            "Вывести текст в строку состояния")
        self.button2 = QtWidgets.QPushButton(
            "Стереть текст в строке состояния")
        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.label)
        self.box.addWidget(self.button)
        self.box.addWidget(self.button2)
        self.setLayout(self.box)

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.w = MyWidget()
        self.setCentralWidget(self.w)
        self.w.button.clicked.connect(self.on_clicked)
        self.w.button2.clicked.connect(self.statusBar().clearMessage)
        self.add_menu()
        self.statusBar().showMessage("Начальный текст в строке состояния")

    def add_menu(self):
        self.menuFile = QtWidgets.QMenu("&File")
        self.menuFile.menuAction().setStatusTip("Это описание меню File")
        self.actOpen = QtGui.QAction("&Open", None)
        self.actOpen.setShortcut(QtGui.QKeySequence.StandardKey.Open)
        self.actOpen.setStatusTip("Это описание пункта Open")
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)
        self.menuBar().addMenu(self.menuFile)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_clicked(self):
        self.statusBar().showMessage("Текст, выводимый на 2 секунды",
                                     2000)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QStatusBar")
window.resize(500, 350)
window.show()
sys.exit(app.exec())
