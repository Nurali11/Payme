from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from payme import MyWindow

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()