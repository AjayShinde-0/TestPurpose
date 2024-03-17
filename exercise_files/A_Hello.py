hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def hexToDec(hexNum):  
     decValue=0
     length = len(hexNum)
     for C in hexNum:
        if C not in hexNumbers:
            return None
     expo=0
     for C in hexNum[::-1]:
         decValue = decValue + hexNumbers[C]*(16**expo)
         expo = expo + 1
     return decValue
print(hexToDec('A'))
print(hexToDec('A0'))
print(hexToDec('200'))
print(hexToDec('100'))