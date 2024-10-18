from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class Kirish(QWidget):
    def __init__(self):
        super().__init__()
        self.h1_lay = QHBoxLayout()
        self.h2_lay = QHBoxLayout()
        self.h3_lay = QHBoxLayout()
        self.h4_lay = QHBoxLayout()
        self.v_lay = QVBoxLayout()

        self.lbl = QLabel('            Payme\n')
        self.lbl.setStyleSheet('color: blue')

        self.lbl1 = QLabel('Parol kiriting')
        self.setStyleSheet('font-size: 25px')
        self.lbl2 = QLabel('')

        self.bir = QPushButton('1')
        self.bir.clicked.connect(self.Bir)
        self.ikki = QPushButton('2')
        self.ikki.clicked.connect(self.Ikki)
        self.uch = QPushButton('3')
        self.uch.clicked.connect(self.Uch)
        self.tort = QPushButton('4')
        self.tort.clicked.connect(self.Tort)
        self.besh = QPushButton('5')
        self.besh.clicked.connect(self.Besh)
        self.olti = QPushButton('6')
        self.olti.clicked.connect(self.Olti)
        self.yetti = QPushButton('7')
        self.yetti.clicked.connect(self.Yetti)
        self.sakkiz = QPushButton('8')
        self.sakkiz.clicked.connect(self.Sakkiz)
        self.toqqiz = QPushButton('9')
        self.toqqiz.clicked.connect(self.Toqqiz)

        self.submit = QPushButton('Submit')
        self.submit.setStyleSheet('background: lightgreen')
        self.submit.clicked.connect(self.Submit)
        self.submit.hide()

        self.h4_lay.addWidget(self.lbl2)
        self.h1_lay.addWidget(self.bir)
        self.h1_lay.addWidget(self.ikki)
        self.h1_lay.addWidget(self.uch)
        self.h2_lay.addWidget(self.tort)
        self.h2_lay.addWidget(self.besh)
        self.h2_lay.addWidget(self.olti)
        self.h3_lay.addWidget(self.yetti)
        self.h3_lay.addWidget(self.sakkiz)
        self.h3_lay.addWidget(self.toqqiz)

        self.v_lay.addWidget(self.lbl)
        self.v_lay.addWidget(self.lbl1)
        self.v_lay.addLayout(self.h4_lay)
        self.v_lay.addLayout(self.h1_lay)
        self.v_lay.addLayout(self.h2_lay)
        self.v_lay.addLayout(self.h3_lay)
        self.v_lay.addWidget(self.submit)

        self.setLayout(self.v_lay)
        self.raqamlar_soni = 0

    def Bir(self):
        self.textga_otqazish('1')
    def Ikki(self):
        self.textga_otqazish('2')
    def Uch(self):
        self.textga_otqazish('3')
    def Tort(self):
        self.textga_otqazish('4')
    def Besh(self):
        self.textga_otqazish('5')
    def Olti(self):
        self.textga_otqazish('6')
    def Yetti(self):
        self.textga_otqazish('7')
    def Sakkiz(self):
        self.textga_otqazish('8')
    def Toqqiz(self):
        self.textga_otqazish('9')
        
    def textga_otqazish(self, data):
        if self.raqamlar_soni < 4: 
            txt = self.lbl2.text()+data
            self.lbl2.setText(txt)
            self.raqamlar_soni += 1 
        else:
            self.submit.show()

    def Submit(self):
        self.topildi = False
        self.msg = QMessageBox()
        with open('tekshiruv.txt') as f:
                for i in f.read().split('\n'):
                    if len(i) > 0:
                        i = i.split(',')
                        if i[3] == self.lbl2.text():
                            self.msg.setText('Topildi!')
                            self.msg.exec_()
                            self.topildi = True
        if self.topildi == False:
            self.lbl2.setText("")
            self.raqamlar_soni =0
            self.msg.setIcon(QMessageBox.critical)
            self.msg.setText('Topilmadi!')
            self.msg.exec_()