value = input("Type 8 digit binary: ")

def bin2dec():
    
    binNum = int(value)
    decNum = 0
    power = 0

    while binNum > 0:
        decNum += 2 ** power * (binNum % 10)
        binNum //= 10
        power += 1

    if power > 8:
        return print("Wrong number of digits")
    else:
        return print(decNum)

bin2dec()