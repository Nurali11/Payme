from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from otqazish import Otqazish

class Menyu(QWidget):
    def __init__(self, malumot):
        super().__init__()
        self.malumot = malumot
        self.ver_lay=QVBoxLayout()
        self.setStyleSheet('font-size: 20px')

        self.hisob=QLabel(f"            {malumot[-1]} so'm")
        self.hisob.setStyleSheet('background: lightblue; font-size: 25px')

        self.boshqa_hisobga_pul_otkazish=QPushButton("boshqa hisobga pul otkazish")
        self.boshqa_hisobga_pul_otkazish.setStyleSheet("background: grey; color:black; font-size=20px")
        self.boshqa_hisobga_pul_otkazish.clicked.connect(self.otqazsh)

        self.chiqish=QPushButton("Chiqish")
        self.chiqish.setStyleSheet("background: grey; color: black; font-size=20px")
        self.chiqish.clicked.connect(exit)

        self.ver_lay.addWidget (self.hisob)
        self.ver_lay.addWidget (self.boshqa_hisobga_pul_otkazish)
        self.ver_lay.addWidget (self.chiqish)
        self.setLayout(self.ver_lay)
        self.show()
    
    def otqazsh(self):
        self.otqazish_window = Otqazish(self.malumot)
        self.otqazish_window.show()