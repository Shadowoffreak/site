from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Управление отступами")
window.resize(400, 50)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
button3 = QtWidgets.QPushButton("3")
button4 = QtWidgets.QPushButton("4")
button5 = QtWidgets.QPushButton("5")
button6 = QtWidgets.QPushButton("6")
vbox = QtWidgets.QVBoxLayout()

hbox = QtWidgets.QHBoxLayout()
hbox.setContentsMargins(0, 0, 0, 0)
hbox.setSpacing(0)
hbox.addWidget(button1)
hbox.addWidget(button2)
hbox.addWidget(button3)
vbox.addLayout(hbox)

hbox2 = QtWidgets.QHBoxLayout()
hbox2.setContentsMargins(30, 30, 30, 30)
hbox2.setSpacing(20)
hbox2.addWidget(button4)
hbox2.addWidget(button5)
hbox2.addWidget(button6)
vbox.addLayout(hbox2)

window.setLayout(vbox)
window.show()
sys.exit(app.exec())
