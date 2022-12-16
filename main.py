import sys
import random
import string
import pyperclip
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PasswordGenerator import Ui_MainWindow_PasswordGenerator


class Ui_PasswordGenerator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_passwordgenerator = Ui_MainWindow_PasswordGenerator()
        self.ui_passwordgenerator.setupUi(self)
        self.ui_passwordgenerator.symbols_2.setChecked(True)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()
        self.pushbutton()
        self.passmake()

    def mousePressEvent(self, evt):
        self.oldpos = evt.globalPos()

    def mouseMoveEvent(self, evt) :
        delta = QPoint(evt.globalPos() - self.oldpos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldpos = evt.globalPos()

    def pushbutton(self):
        self.ui_passwordgenerator.pushButton.clicked.connect(self.allclicl)
        self.ui_passwordgenerator.pushButtonrefresh.clicked.connect(self.passwordgeneratore)
        self.ui_passwordgenerator.pushButtoncopy.clicked.connect(self.copyhash)

    def copyhash(self):
        if ((self.ui_passwordgenerator.lineEdit.text()) != ""):
            try:
                pyperclip.copy(self.ui_passwordgenerator.lineEdit.text())
                QMessageBox.information(self, "Copy Password", "Password Copied")
            except:
                pass
        else:
            QMessageBox.information(self, "Copy Password", "Please wait until Password is generated")

    def allclicl(self):
        if(self.ui_passwordgenerator.symbols_2.isChecked() == True):
            self.ui_passwordgenerator.uppercase.setChecked(True)
            self.ui_passwordgenerator.lowercase.setChecked(True)
            self.ui_passwordgenerator.numbers.setChecked(True)
            self.ui_passwordgenerator.symbols.setChecked(True)

        else:
            self.ui_passwordgenerator.uppercase.setChecked(False)
            self.ui_passwordgenerator.lowercase.setChecked(False)
            self.ui_passwordgenerator.numbers.setChecked(False)
            self.ui_passwordgenerator.symbols.setChecked(False)



    def passwordgeneratore(self):
        Length = int(self.ui_passwordgenerator.length.text())
        all = self.ui_passwordgenerator.symbols_2.isChecked()
        u = self.ui_passwordgenerator.uppercase.isChecked()
        l = self.ui_passwordgenerator.lowercase.isChecked()
        n = self.ui_passwordgenerator.numbers.isChecked()
        s = self.ui_passwordgenerator.symbols.isChecked()

        Uppercase = string.ascii_uppercase
        Lowercase = string.ascii_lowercase
        Numbers = string.digits
        Symbols = string.punctuation

        self.All = ""
        if (self.ui_passwordgenerator.horizontalSlider.value() >= 1 and self.ui_passwordgenerator.horizontalSlider.value() <= 15):
            self.ui_passwordgenerator.progressBar_2.setStyleSheet("QProgressBar\n"
            "{\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#ffffff, stop:1 #abbaab);\n"
            "border: 1px solid #000;\n"
            "}\n"
            "QProgressBar::chunk \n"
            "{\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #e65c00,stop:1 #ffaf19);\n"
            "\n"
            "border: 1px solid #000;\n"
            "\n"
            "}    ")
        elif ((self.ui_passwordgenerator.horizontalSlider.value() > 15) and (self.ui_passwordgenerator.horizontalSlider.value() <= 30)):
            self.ui_passwordgenerator.progressBar_2.setStyleSheet("QProgressBar\n"
            "{\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#ffffff, stop:1 #abbaab);\n"
            "border: 1px solid #000;\n"
            "}\n"
            "QProgressBar::chunk \n"
            "{\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #ffff00,stop:1 #ffa733);\n"
            "\n"
            "border: 1px solid #000;\n"
            "\n"
            "}    ")
        elif ((self.ui_passwordgenerator.horizontalSlider.value() > 30) and (self.ui_passwordgenerator.horizontalSlider.value() <= 55)):
            self.ui_passwordgenerator.progressBar_2.setStyleSheet("QProgressBar\n"
            "{\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#ffffff, stop:1 #abbaab);\n"
            "border: 1px solid #000;\n"
            "}\n"
            "QProgressBar::chunk \n"
            "{\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #5488ff,stop:1 #a5fecb);\n"
            "\n"
            "border: 1px solid #000;\n"
            "\n"
            "}    ")
        elif ((self.ui_passwordgenerator.horizontalSlider.value() > 55) and (self.ui_passwordgenerator.horizontalSlider.value() <= 100)):
            self.ui_passwordgenerator.progressBar_2.setStyleSheet("QProgressBar\n"
            "{\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0#ffffff, stop:1 #abbaab);\n"
            "border: 1px solid #000;\n"
            "}\n"
            "QProgressBar::chunk \n"
            "{\n"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,stop:0 #fdfc47, stop:1 #24fe41);\n"
            "\n"
            "border: 1px solid #000;\n"
            "\n"
            "}    ")
        if (all == True):

            self.All = Uppercase + Lowercase + Numbers + Symbols
            password = ""
            for index in range(Length):
                password = password + random.choice(self.All)
            self.ui_passwordgenerator.lineEdit.setText(password)
            # ----------------------------------------------------------------------------

        elif(all == False) :
            self.All = ""
            if ((u == True)):
                self.All += Uppercase
                password = ""
                for index in range(Length):
                    password = password + random.choice(self.All)
                self.ui_passwordgenerator.lineEdit.setText(password)
            # ----------------------------------------------------------------------------
            if ((l == True)):
                self.All += Lowercase
                password = ""
                for index in range(Length):
                    password = password + random.choice(self.All)
                self.ui_passwordgenerator.lineEdit.setText(password)
            # ----------------------------------------------------------------------------
            if ((n == True)):
                self.All += Numbers
                password = ""
                for index in range(Length):
                    password = password + random.choice(self.All)
                self.ui_passwordgenerator.lineEdit.setText(password)
            # ----------------------------------------------------------------------------
            if ((s == True)):
                self.All += Symbols
                password = ""
                for index in range(Length):
                    password = password + random.choice(self.All)
                self.ui_passwordgenerator.lineEdit.setText(password)

    def passmake(self):
        self.ui_passwordgenerator.horizontalSlider.sliderMoved['int'].connect(self.passwordgeneratore)


if __name__ == "__main__":
    qApp = QApplication(sys.argv)
    root = Ui_PasswordGenerator()
    sys.exit(qApp.exec_())
