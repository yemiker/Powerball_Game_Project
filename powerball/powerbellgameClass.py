#First Class
class PowerBallGame:
    def __init__(self, fullName, age, LotteryDate):
        self.fullName = fullName
        self.age = age
        self.LotteryDate = LotteryDate

    def __str__(self):
        return self.fullName + " " + str(self.age) + " " + str(self.LotteryDate)
