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
        self.numberSlider.valueChanged.connect(self.numberSliderChanged)
        self.numberSliderChanged()
        self.generateButtonClicked()

    def numberSliderChanged(self):
        self.numberOfBigNos = self.numberSlider.value()
        self.numberOfSmallNos = 6-self.numberOfBigNos
        numberOfNumbersText = "Big Numbers: " + str(self.numberOfBigNos) + " Small numbers: " + str(self.numberOfSmallNos)
        self.numberOfNumbers.setText(numberOfNumbersText)

    def validateInputs(self):
        valid = True
        for inp in self.sLineEdits:
            initalInput = inp.text()
            try:
                initalInput = int(initalInput)
                if initalInput > 100:
                    print(0/0) #so creates error
                elif initalInput < 1:
                    print(0/0) #so creates error
            except:
                valid = False
                inp.setText(str(1))
        initalInput = self.bigNo.text()
        try:
            initalInput = int(initalInput)
            if initalInput > 999:
                print(0/0) #so creates error
            elif initalInput < 1:
                print(0/0) #so creates error
        except:
            valid = False
            self.bigNo.setText(str(100))
        if not valid:
            self.errorWindow = ErrorWindow("The value you have entered is not valid. Please try again")


    def solveButtonClicked(self):

        if len(self.combinations) == 0:
            self.solutions.setText("There are no solutions")
        else:
            solutions = ""
            for combination in self.combinations:
                solution = ""
                if combination[0][0:1] == "+":
                    combination[0] = combination[0][1:len(combination[0])]#
                previousSign = None
                startBrackets = 0
                for i in range(len(combination)):
                    if i != len(combination)-1:
                        nextSign = combination[i+1][0:1]
                    sign = combination[i][0:1]
                    numberPart = combination[i][1:len(combination[i])]
                    if sign == "*":
                        sign = "x"
                    elif sign == "/":
                        sign = "÷"
                    if i != 0: #can only be the first as doesn't have the sign
                        # if i == 1:
                        if sign == "+" or sign == "-":
                            if nextSign == "+" or nextSign == "-":
                                number = sign + " " + numberPart + " "
                            else:
                                number = sign + " " + numberPart + ") "
                                startBrackets += 1
                        else:
                            number = sign + " " + numberPart + " "

                    else:
                        if sign == "+":
                            number = numberPart + " "
                        else:
                            number = sign + numberPart + " "
                    previousSign = sign[:]
                    solution = solution + number

                for j in range(startBrackets):
                    solution = "(" + solution
                solutions = solutions + solution + "\n"
            self.solutions.setText(solutions)


    def generateButtonClicked(self):
        self.smallNumbers = []
        bigNos = [25,50,75,100]
        i=-1
        for i in range(self.numberOfBigNos):
            chosenNumber = random.choice(bigNos)
            self.smallNumbers.append(chosenNumber)
            bigNos.remove(chosenNumber)
            self.sLineEdits[i].setText(str(self.smallNumbers[i]))
        for j in range(self.numberOfSmallNos):
            self.smallNumbers.append(random.randint(1,10))
            self.sLineEdits[i+j+1].setText(str(self.smallNumbers[i+j+1]))
        self.bigNumber = random.randint(1,999)
        if self.bigNumber < 10:
            self.bigNumber = "00"+str(self.bigNumber)
        elif self.bigNumber < 100:
            self.bigNumber = "0"+str(self.bigNumber)
        self.bigNo.setText(str(self.bigNumber))
        self.solve()

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Return:
            self.solveButtonClicked()

    def solve(self):
        self.validateInputs()
        self.solutions.setText("Calculating...")
        self.update()
        QApplication.processEvents()
        numbers = []
        for no in self.sLineEdits:
            numbers.append(int(no.text()))
        bigNumber = int(self.bigNo.text())
        self.combinations = []
        self.checker = Checker(bigNumber,numbers,parentWindow=self)
        if len(self.combinations) == 0:
            self.solutions.setText("There are no solutions")
        else:
            self.solutions.setText(f"There are {len(self.combinations)} solutions")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = CountdownWindow()
    win.show()
    sys.exit(app.exec_())
