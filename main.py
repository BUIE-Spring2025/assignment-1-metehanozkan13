def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    alfa = num % 1000
    beta = num // 1000
    teta = alfa // 100
    tena = teta % 5
    meta = num % 100
    nisa = meta // 10
    nine = nisa % 5
    niga = num % 10
    nega = niga % 5
    print(beta*"M", end='')
    if teta == 9:
        print("CM", end='')
    if 9 > teta > 3:
        if teta == 4:
            print("CD", end='')
        else:
            print("D", end='')
            print(tena*"C", end='')
    if teta < 4:
        print(teta*"C", end='')
    if nisa == 9:
        print("XC", end='')
    if 9 > nisa > 3:
        if nisa == 4:
            print("XL", end='')
        else:
            print("L", end='')
            print(nine*"X", end='')
    if nisa < 4:
        print(nisa*"X",end='')
    if niga == 9:
        print("IX", end='')
    if 9 > niga > 3 :
        if niga == 4:
            print("IV", end='')
        else:
            print("V", end='')
            print(nega*"I", end='')
    if niga < 4:
        print(niga*"I", end='')
