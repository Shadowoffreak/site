from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    view.clearSpans()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTableView")
window.resize(500, 400)
view = QtWidgets.QTableView()

model = QtGui.QStandardItemModel(4, 4)
for row in range(0, 4):
    for column in range(0, 4):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        model.setItem(row, column, item)
view.setModel(model)
model.setHorizontalHeaderLabels(["A", "B", "C", "D"])
model.setVerticalHeaderLabels(["01", "02", "03", "04"])

view.setSpan(0, 0, 1, 2)
view.setSpan(0, 3, 3, 1)

print(view.rowSpan(0, 0))
print(view.columnSpan(0, 0))

button = QtWidgets.QPushButton("Убрать все объединения")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
