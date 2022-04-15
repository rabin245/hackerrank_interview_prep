
from math import log


def powerCheck(x, y):
    # first approach
    # num = x
    # while abs(num) > 1:
    #     num = num/y
    #     print(num)
    # return num == 1

    # using log
    # p = log(abs(x))/log(abs(y))
    p = log(abs(x), abs(y))
    print(p, int(p))

    # check for cases
    if (x > 0 and y > 0):
        print("both + sign")
        return p == int(p)
    elif x < 0 and y < 0:
        print("both - sign")
        if p % 2 == 1:
            return True
    elif x > 0 and y < 0:
        print('x + and y -')
        if p % 2 == 0:
            return True
    else:
        print('last failed case')
    return False


# p = powerCheck(18, -4)
# p = powerCheck(18, 2)
p = powerCheck(-3, -3)
# p = powerCheck(17, -2)
# p = powerCheck(16, 4)
print(p)
