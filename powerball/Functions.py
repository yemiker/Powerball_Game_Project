from powerbellgameClass import PowerBallGame
import random
import random as ran


# Class of functions

class Functions(PowerBallGame):
    def __init__(self, fullName, age, LotteryDate, guessing, winningAmount):
        super().__init__(fullName, age, LotteryDate)
        self.guessing = guessing
        self.winningAmount = winningAmount

    def getFullName(self):
        return (self.fullName)

    def setFullName(self,fullname):
        set.fullname=input(fullname)


    def __str__(self):
        return super(Functions, self).__str__() + " " + str(self.guessing) + " " + str(self.winningAmount)


# Definition of 2 arrays

whiteBalls = []
strongNumber = []


# Function The winning balls, I defined an array of white balls and a strong number and inserted them
def powerballWin():
    for i in range(5):
        number = ran.randint(1, 20)
        while number in whiteBalls:
            number = ran.randint(1, 20)
        whiteBalls.append(number)
    for i in range(1):
        strongNumber.append(random.randrange(1, 10))
    return f'{sorted(whiteBalls)} {strongNumber} '


luckyWhiteBalls = []
luckyStrongNumber = []


# Function of your lucky balls, I set up an array of white balls and a strong number and inserted them
def luckyPowerball():
    for i in range(5):
        number = ran.randint(1, 20)
        while number in luckyWhiteBalls:
            number = ran.randint(1, 20)
        luckyWhiteBalls.append(number)
    for i in range(1):
        luckyStrongNumber.append(random.randrange(1, 10))
    return f'{sorted(luckyWhiteBalls)} {luckyStrongNumber} '
