from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Fixed")
window.resize(300, 150)
label = QtWidgets.QLabel("Текст надписи")
button = QtWidgets.QPushButton("Текст на кнопке")

policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, 
                               QtWidgets.QSizePolicy.Policy.Fixed)
label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                    QtWidgets.QFrame.Shadow.Plain)
label.setSizePolicy(policy)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
