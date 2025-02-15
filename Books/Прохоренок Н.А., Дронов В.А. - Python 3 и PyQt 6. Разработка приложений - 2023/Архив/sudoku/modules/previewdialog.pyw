from PyQt6 import QtCore, QtWidgets, QtPrintSupport

class PreviewDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        print("!")
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle("Предварительный просмотр")
        self.resize(600, 400)
        vBox = QtWidgets.QVBoxLayout()
        hBox1 = QtWidgets.QHBoxLayout()
        btnZoomIn = QtWidgets.QPushButton("&+")
        btnZoomIn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        hBox1.addWidget(btnZoomIn, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        btnZoomOut = QtWidgets.QPushButton("&-")
        btnZoomOut.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        hBox1.addWidget(btnZoomOut,
                        alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        btnZoomReset = QtWidgets.QPushButton("&Сброс")
        btnZoomReset.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        btnZoomReset.clicked.connect(self.zoomReset)
        hBox1.addWidget(btnZoomReset,
                        alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        hBox1.addStretch()
        vBox.addLayout(hBox1)
        hBox2 = QtWidgets.QHBoxLayout()
        self.ppw = QtPrintSupport.QPrintPreviewWidget(parent.printer)
        self.ppw.paintRequested.connect(parent.sudoku.print)
        hBox2.addWidget(self.ppw)
        btnZoomIn.clicked.connect(self.ppw.zoomIn)
        btnZoomOut.clicked.connect(self.ppw.zoomOut)
        box = QtWidgets.QDialogButtonBox(
                        QtWidgets.QDialogButtonBox.StandardButton.Close,
                        QtCore.Qt.Orientation.Vertical)
        btnClose = box.button(QtWidgets.QDialogButtonBox.StandardButton.Close)
        btnClose.setText("&Закрыть")
        btnClose.setFixedSize(96, 64)
        btnClose.clicked.connect(self.accept)
        hBox2.addWidget(box, alignment=QtCore.Qt.AlignmentFlag.AlignRight |
                                       QtCore.Qt.AlignmentFlag.AlignTop)
        vBox.addLayout(hBox2)
        self.setLayout(vBox)
        self.zoomReset()

    def zoomReset(self):
        self.ppw.setZoomFactor(1)
