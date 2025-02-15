from PyQt6 import QtCore, QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
        self.button = QtWidgets.QPushButton("Изменить указатель", self)
        self.button.setGeometry(50, 10, 200, 30)
        self.button.clicked.connect(self.on_clicked)
        
    def on_clicked(self):
        QtWidgets.QApplication.setOverrideCursor(
                                  QtCore.Qt.CursorShape.WaitCursor)
        self.button.setEnabled(False)
        QtCore.QTimer.singleShot(5000, self.on_timeout)
        
    def on_timeout(self):
        QtWidgets.QApplication.restoreOverrideCursor()
        self.button.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Изменение курсора мыши у программы")
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec())
