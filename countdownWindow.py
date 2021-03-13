from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
import random

from checker import Checker
from errorWindow import ErrorWindow

class CountdownWindow(QMainWindow,uic.loadUiType("countdownWindow.ui")[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Countdown")
        self.combinations = []
        self.initUI()

    def initUI(self):
        self.generateButton.clicked.connect(self.generateButtonClicked)
        self.solveButton.clicked.connect(self.solveButtonClicked)
        self.sLineEdits = [self.s1,self.s2,self.s3,self.s4,self.s5,self.s6]
        for inp in self.sLineEdits:
            inp.textEdited.connect(self.valuesChanged)
        self.bigNo.textEdited.connect(self.valuesChanged)
        self.generateButtonClicked()


    def valuesChanged(self):
        for inp in self.sLineEdits:
            initalInput = inp.text()
            try:
                initalInput = int(initalInput)
                if initalInput > 10:
                    print(0/0) #so creates error
                elif initalInput < 1:
                    print(0/0) #so creates error
            except:
                self.errorWindow = ErrorWindow("The value you have entered is not valid. Please try again")
                inp.setText(str(1))
        initalInput = self.bigNo.text()
        try:
            initalInput = int(initalInput)
            if initalInput > 999:
                print(0/0) #so creates error
            elif initalInput < 1:
                print(0/0) #so creates error
        except:
            self.errorWindow = ErrorWindow("The value you have entered is not valid. Please try again")
            self.bigNo.setText(str(100))


    def solveButtonClicked(self):
        numbers = []
        for no in self.sLineEdits:
            numbers.append(int(no.text()))
        print(numbers)
        bigNumber = int(self.bigNo.text())
        self.checker = Checker(bigNumber,numbers,parentWindow=self)
        if len(self.combinations) == 0:
            self.solutions.setText("There are no solutions")


    def generateButtonClicked(self):
        self.smallNumbers = []
        for i in range(6):
            self.smallNumbers.append(random.randint(1,10))
            self.sLineEdits[i].setText(str(self.smallNumbers[i]))
        self.bigNumber = random.randint(1,999)
        if self.bigNumber < 10:
            self.bigNumber = "00"+str(self.bigNumber)
        elif self.bigNumber < 100:
            self.bigNumber = "0"+str(self.bigNumber)
        self.bigNo.setText(str(self.bigNumber))

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Return:
            self.solve()

    def solve(self):
        pass


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = CountdownWindow()
    win.show()
    sys.exit(app.exec_())
