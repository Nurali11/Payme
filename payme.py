from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from login import Login
from kirish import Kirish

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('font-size: 25px')
        self.h_lay = QHBoxLayout()
        self.v_lay = QVBoxLayout()
        
        self.login = QPushButton('Login')
        self.login.setStyleSheet('background: grey')
        self.login.clicked.connect(self.Login)

        self.kirish = QPushButton('Kirish')
        self.kirish.setStyleSheet('background: grey')
        self.kirish.clicked.connect(self.Kirish)

        self.chiqish = QPushButton('Chiqish')
        self.chiqish.setStyleSheet('background: grey')
        self.chiqish.clicked.connect(exit)

        self.h_lay.addWidget(self.login)
        self.h_lay.addWidget(self.kirish)

        self.v_lay.addLayout(self.h_lay)
        self.v_lay.addWidget(self.chiqish)

        self.setLayout(self.v_lay)
    
    def Login(self):
        self.log = Login()
        self.log.show()

    def Kirish(self):
        self.kir = Kirish()
        self.kir.show()