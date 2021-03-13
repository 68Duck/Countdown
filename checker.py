class Checker(object):
    def __init__(self,startNumber,numbers,path=[],parentWindow=None):
        self.path = path
        self.parentWindow = parentWindow
        self.numbers = numbers
        self.startNumber = startNumber
        self.check()

    def check(self):
        for number in self.numbers:
            self.checkDivide(number)
            self.checkMinus(number)
            self.checkAdd(number)
            self.checkMultiply(number)

    def checkDivide(self,number):
        if number == 1:
            return
        newPath = self.path[:]
        if len(newPath) != 0:
            if newPath[len(newPath)-1][0:1] == "*":
                return
        newValue = self.startNumber/number
        newNumbers = self.numbers[:]
        newNumbers.remove(number)
        newPath.append("/"+str(number))
        if newValue == 0:
            self.convertPath(newPath)
        else:
            self.newChecker = Checker(newValue,newNumbers,newPath,parentWindow = self.parentWindow)
    def checkMinus(self,number):
        newValue = self.startNumber-number
        newNumbers = self.numbers[:]
        newNumbers.remove(number)
        newPath = self.path[:]
        newPath.append("-"+str(number))
        if newValue == 0:
            self.convertPath(newPath)
        else:
            self.newChecker = Checker(newValue,newNumbers,newPath,parentWindow = self.parentWindow)
    def checkAdd(self,number):
        newPath = self.path[:]
        if len(newPath) != 0:
            if newPath[len(newPath)-1][0:1] == "-":
                return
            elif newPath[len(newPath)-1][0:1] == "+":
                if number < int(newPath[len(newPath)-1][1:len(newPath)+1]):
                    return

        newPath.append("+"+str(number))
        newValue = self.startNumber+number
        newNumbers = self.numbers[:]
        newNumbers.remove(number)

        if newValue == 0:
            self.convertPath(newPath)
        else:
            # print(newPath)
            self.newChecker = Checker(newValue,newNumbers,newPath,parentWindow = self.parentWindow)
    def checkMultiply(self,number):
        if number == 1:
            return
        newPath = self.path[:]
        if len(newPath) != 0:
            if newPath[len(newPath)-1][0:1] == "*":
                if number < int(newPath[len(newPath)-1][1:len(newPath)+1]):
                    return
        newValue = self.startNumber*number
        newNumbers = self.numbers[:]
        newNumbers.remove(number)
        newPath.append("*"+str(number))
        if newValue == 0:
            self.convertPath(newPath)
        else:
            self.newChecker = Checker(newValue,newNumbers,newPath,parentWindow = self.parentWindow)

    def convertPath(self,path):
        correctOrder = []
        for i in range(len(path)):
            symbol = path[len(path)-i-1][0:1]
            number = path[len(path)-i-1][1:len(path[len(path)-i-1])+1]
            if symbol == "+":
                newSymbol = "-"
            elif symbol == "-":
                newSymbol = "+"
            elif symbol == "*":
                newSymbol = "/"
            else:
                newSymbol = "*"
            correctOrder.append(newSymbol+str(number))
        # print(correctOrder)
        if __name__ == "__main__":
            global combinations
            combinations.append(correctOrder)
        if self.parentWindow is None:
            pass
        else:
            self.parentWindow.combinations.append(correctOrder)


if __name__ == "__main__":
    ## OPTIMIZED version
    bigNumber = int(input("enter big number"))
    numbers = []
    for i in range(6):
        newNo = int(input("enter a small number"))
        numbers.append(newNo)
    # bigNumber = 315
    # numbers = [75,100,25,1,6,9]
    combinations = []
    numbers.sort()
    checker = Checker(bigNumber,numbers)
    print(len(combinations))
