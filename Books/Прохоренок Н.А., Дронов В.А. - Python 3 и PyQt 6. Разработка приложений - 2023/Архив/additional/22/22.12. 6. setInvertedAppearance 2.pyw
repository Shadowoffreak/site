from PyQt6 import QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QProgressBar")
window.resize(300, 400)
progressBar = QtWidgets.QProgressBar()
progressBar.setRange(0, 100)
progressBar.setValue(70)
progressBar.setOrientation(QtCore.Qt.Orientation.Vertical)
progressBar.setInvertedAppearance(True)
progressBar2 = QtWidgets.QProgressBar()
progressBar2.setRange(0, 100)
progressBar2.setValue(70)
progressBar2.setOrientation(QtCore.Qt.Orientation.Vertical)
progressBar2.setInvertedAppearance(False)
box = QtWidgets.QHBoxLayout()
box.addWidget(progressBar)
box.addWidget(progressBar2)
window.setLayout(box)
window.show()
sys.exit(app.exec())
