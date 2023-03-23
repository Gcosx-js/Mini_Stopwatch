from PyQt5.QtWidgets import *
from main import Ui_Form
from PyQt5.QtCore import QTimer

class Anaekran(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.app = Ui_Form()
        self.app.setupUi(self)
        self.app.baslat_button.clicked.connect(self.baslat)
        self.gecikdir = QTimer(self)
        self.gecikdir.timeout.connect(self.say)
        self.app.dayandir_button.clicked.connect(self.dayandir)
        self.app.sifirla_button.clicked.connect(self.sifirla)
        self.saniye = 0
        self.deqiqe = 0
        self.saat = 0
    def dayandir(self):
        self.gecikdir.stop()
    def sifirla(self):
        self.saniye = 0
        self.deqiqe = 0
        self.saat = 0
        self.gecikdir.stop()
        self.app.main_vaxt.setText("00:00:00")
    def baslat(self):
        self.say()
        self.gecikdir.start(1000)
    def say(self):
        self.saniye += 1
        if self.saniye >= 60:
            self.saniye = 0
            self.deqiqe += 1
        if self.deqiqe >= 60:
            self.deqiqe = 0
            self.saat += 1
        self.app.main_vaxt.setText(f"{self.saat:02d}:{self.deqiqe:02d}:{self.saniye:02d}")
app = QApplication([])
ekran = Anaekran()
ekran.show()
app.exec_()
