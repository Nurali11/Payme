from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')

        self.h_lay = QHBoxLayout()
        self.h1_lay = QHBoxLayout()
        self.h2_lay = QHBoxLayout()
        self.h3_lay = QHBoxLayout()
        self.v_lay = QVBoxLayout()

        self.ism = QLabel('Ism: ')
        self.ism_edit = QLineEdit()

        self.nomer = QLabel('+998 ')
        self.setStyleSheet('font-size: 18px')
        self.nomer_edit = QLineEdit()

        self.karta = QLabel('Karta: ')
        self.kara_edit = QLineEdit()

        self.parol = QLabel('Parol: ')
        self.parol_edit = QLineEdit()

        self.h_lay.addWidget(self.ism)
        self.h_lay.addWidget(self.ism_edit)


        self.h1_lay.addWidget(self.nomer)
        self.h1_lay.addWidget(self.nomer_edit)
        
        self.h2_lay.addWidget(self.karta)
        self.h2_lay.addWidget(self.kara_edit)

        self.h3_lay.addWidget(self.parol)
        self.h3_lay.addWidget(self.parol_edit)

        self.submit = QPushButton('Submit')
        self.submit.setStyleSheet('background: lightgreen; font-size: 20px')
        self.submit.clicked.connect(self.Submit)

        self.v_lay.addLayout(self.h_lay)
        self.v_lay.addLayout(self.h1_lay)
        self.v_lay.addLayout(self.h2_lay)
        self.v_lay.addLayout(self.h3_lay)
        self.v_lay.addWidget(self.submit)

        self.setLayout(self.v_lay)
    def Submit(self):
        error = False
        nomer_tekshiruv = 0
        karta_tekshiruv = 0
        for i in self.nomer_edit.text():
            if i.isdigit():
                nomer_tekshiruv += 1
        for i in self.kara_edit.text():
            if i.isdigit():
                karta_tekshiruv += 1
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        if len(self.ism_edit.text()) == 0:
            self.msg.setText('Ism kiritish shart!')
            self.msg.exec_()
        if not self.kara_edit.text().isdigit():
            error = True
            self.kara_edit.clear()
            self.msg.setText('Notgri telefon raqam!')
            self.msg.exec_()
        elif not self.nomer_edit.text().isdigit():
            error = True
            self.nomer_edit.clear()
            self.msg.setText('Karta notogri!')
            self.msg.exec_()
        if nomer_tekshiruv != 9:
            if karta_tekshiruv != 16:
                self.nomer_edit.clear()
                self.kara_edit.clear()
                error = True
                self.msg.setText('Karta va telefon notogri!')
                self.msg.exec_()
            else:
                error = True
                self.nomer_edit.clear()
                self.msg.setText('Notgri telefon raqam!')
                self.msg.exec_()
        elif  karta_tekshiruv != 16:
                error = True
                self.kara_edit.clear()
                self.msg.setText('Karta notogri!')
                self.msg.exec_()
        elif len(self.parol_edit.text()) < 4:
            self.parol_edit.clear()
            error = True
            self.msg.setText('Parolda kamida 4ta elemet bolishi kerak')
            self.msg.exec_()
        else:
            with open ('tekshiruv.txt') as f:
                if self.kara_edit.text() in f.read():
                    self.kara_edit.clear()
                    error = True
                    self.msg.setText('Bu karta bant!')
                    self.msg.exec_()
        if error == False:
            self.msg.setText('Muvaffaqiyatli otildi!')
            self.msg.setIcon(QMessageBox.Information)
            self.msg.exec_()
            with open ('tekshiruv.txt', 'a') as f:
                f.write(f"{self.ism_edit.text()},{self.kara_edit.text()},{self.nomer_edit.text()},{self.parol_edit.text()}\n")
                self.close()