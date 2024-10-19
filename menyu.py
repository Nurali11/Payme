from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class Menyu(QWidget):
    def __init__(self):
        super().__init__()

        with open('tekshiruv.txt') as f:
            for i in f.read().split('\n'): 
                if len(i) > 0:
                    i.split(',')
                    if i[3] == self.lbl2.text():

                        self.win=Menyu()

                        self.ver_lay=QVBoxLayout()

                        self.hisob=QLabel(f"{i[4]}")
                    
                        self.hisobga_pul_qoyish=QPushButton("Hisobga pul qoyish")
                        self.hisobga_pul_qoyish.setStyleSheet("background: grey; color:black; font-size=20px")

                        self.hisobdan_pul_olish=QPushButton("Hisobdan pul olish")
                        self.hisobdan_pul_olish.setStyleSheet("background:grey; color:black; font-size=20px")

                        self.boshqa_hisobga_pul_otkazish=QPushButton("boshqa hisobga pul otkazish")
                        self.boshqa_hisobga_pul_otkazish.setStyleSheet("background: grey; color:black; font-size=20px")

                        self.chiqish=QPushButton("Chiqish")
                        self.chiqish.setStyleSheet("background: grey; color: black; font-size=20px")
                        self.chiqish.clicked.connect(exit)

                        self.ver_lay.addWidget (self.hisob)
                        self.ver_lay.addWidget (self.hisobga_pul_qoyish)
                        self.ver_lay.addWidget (self.hisobdan_pul_olish)
                        self.ver_lay.addWidget (self.boshqa_hisobga_pul_otkazish)
                        self.ver_lay.addWidget (self.chiqish)
                        self.win.setLayout(self.ver_lay)
                        self.win.show()

                        return
                