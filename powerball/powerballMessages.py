from Functions import *


# The function of the winning balls according to the lottery result

def ResultWin():
    result = 0
    for x in whiteBalls:
        for y in luckyWhiteBalls:
            if x == y:
                result += 1
    if result == 5 and strongNumber == luckyStrongNumber:
        return 'Correct White Balls and the Powerball you won: 320000000$'
    elif result == 5 and strongNumber != luckyStrongNumber:
        return '5 Correct White Ball & strong number you won: 1000000'
    elif result == 4 and strongNumber == luckyStrongNumber:
        return '4 Correct White Ball & strong number you won: 10000$'
    elif result == 4 and strongNumber != luckyStrongNumber:
        return '4 Correct White Ball you won: 100$'
    elif result == 3 and strongNumber == luckyStrongNumber:
        return '3 Correct White Ball & strong number you won: 100$'
    elif result == 3 and strongNumber != luckyStrongNumber:
        return '3 Correct White Ball  you won: 7$'
    elif result == 2 and strongNumber == luckyStrongNumber:
        return '2 Correct White Ball & strong number you won:  7$'
    elif result == 1 and strongNumber == luckyStrongNumber:
        return '1 Correct White Ball & strong number you won:  4$'
    elif result == 0 and strongNumber == luckyStrongNumber:
        return 'only strong number: 1$'
    else:
        return 'Try again'


print('Today’s Powerball Winning Numbers\n', PowerballWin())
print('Your lucky numbers\n', LuckyPowerball())

print('-----------------------')
print(ResultWin())
