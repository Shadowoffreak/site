from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    print("Текст:", comboBox.currentText())
    print("Данные:", comboBox.itemData(comboBox.currentIndex()))

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtWidgets.QComboBox()
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i), i)
comboBox.setItemText(0, "Новое значение")
ico = window.style().standardIcon(
             QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical)
comboBox.setItemIcon(0, ico)
comboBox.setItemData(0, 50, role=QtCore.Qt.ItemDataRole.UserRole)
comboBox.setItemData(0, "Это текст всплывающей подсказки",
                     role=QtCore.Qt.ItemDataRole.ToolTipRole)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
