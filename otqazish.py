from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class Otqazish(QWidget):
    def __init__(self, malumot):
        super().__init__()
        self.malumot = malumot
        self.msg = QMessageBox()
        self.setStyleSheet('font-size: 20px')
        self.v_lay = QVBoxLayout()
        self.lbl = QLabel('Boshqa userning kartasini kirting: ')
        self.lbl_edit = QLineEdit()

        self.summa = QLineEdit()
        self.summa.hide()

        self.btn = QPushButton('Submit')
        self.btn.setStyleSheet('background: lightgreen')
        self.btn.clicked.connect(self.Submit)

        self.v_lay.addWidget(self.lbl)
        self.v_lay.addWidget(self.lbl_edit)
        self.v_lay.addWidget(self.btn)
        self.setLayout(self.v_lay)

    def Submit(self):
        self.topildi = False
        if self.malumot[1] == self.lbl_edit:
            self.msg.setText('Ozingizga pul otqazolmaysiz!')
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.show()

        with open ('tekshiruv.txt') as f:
            for i in f.read().split('\n'):
                if len(i) > 0:
                    i = i.split(',')
                    self.boshqa_malumot = i
                    if i[1] == self.lbl_edit.text():
                        self.topildi = True
                        self.lbl2 = QLabel(f'{i[0]} ga necha som otqazmoqchisiz: ')
                        self.summa.show()
                        self.btn.clicked.connect(self.Submit2)

                        self.v_lay.addWidget(self.lbl2)
                        self.v_lay.addWidget(self.summa)
                        self.v_lay.addWidget(self.btn)
                        self.setLayout(self.v_lay)

    def Submit2(self):
        summa = int(self.summa.text())
        son = True
        for i in self.summa.text():
            if i.isalpha():
                son = False
        if son == False: 
            self.summa.clear()
            self.msg.setText('Summada sonlar boladi!')
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.show()
        elif summa < int(self.malumot[-1]):
            self.msg.setText(f'Sizning hisobingizda {summa} dan kam mablag bor!')
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.show()
        else:
            with open ('tekshiruv.txt', 'a+') as f:
                self.malumot = f"{self.malumot[:-1]},{int(self.malumot[-1]) - summa}"
                self.boshqa_malumot = f"{self.boshqa_malumot[:-1]},{int(self.boshqa_malumot[-1]) + summa}"
                for i in f.read().split('\n'):
                    if i:
                        i = i.split(',')
                        if i[1] == self.malumot[1]:
                            f.write(f"{self.malumot}\n")
                        elif i[1] == self.boshqa_malumot[1]:
                            f.write(f'{self.boshqa_malumot}\n')
                        else:
                            f.write(f"{i}\n")