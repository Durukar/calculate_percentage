# Created by Durukar


def x():
    x = float(input('Enter the percentage you want to check: '))
    return x

def percent():
    trys = 0
    while(trys <= 0):
        n1 = float(input('Enter the number you want to withdraw the percentage: '))
        n2 = x()
        calc = n2 / 100 * n1
        print(f'\nThe{n2:.2f}% of {n1:.2f} is {calc:.2f}')
        pressContinue = input('\nPress Enter to calculate another percentage')
if(__name__) == '__main__':
    percent()