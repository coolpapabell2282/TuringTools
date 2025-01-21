import math
import random

LESSTHAN = -1
EQUAL = 0
GREATERTHAN = 1
INCREASING = 1
DECREASING = -1
CHAOTIC = 0
NUMOFTRIALS = 1000
cardPossibilities = [[LESSTHAN,GREATERTHAN,EQUAL],[LESSTHAN,GREATERTHAN,EQUAL],[LESSTHAN,GREATERTHAN,EQUAL],[LESSTHAN,GREATERTHAN,EQUAL],[True,False],[True,False],[True,False],[0,1,2],[0,1,2],[0,1,2],[LESSTHAN,GREATERTHAN,EQUAL],[LESSTHAN,GREATERTHAN,EQUAL],[LESSTHAN,GREATERTHAN,EQUAL],[True,False],[True,False],[True,False],[True,False],[True,False],[True,False],[True,False],[0,1,2,3],[True,False],[LESSTHAN,GREATERTHAN,EQUAL],[0,1,2],[True,False],[INCREASING,DECREASING,CHAOTIC],[LESSTHAN,GREATERTHAN,EQUAL]]


def compareToRaw(code,position,raw):
    if(code[position] < raw):
        return LESSTHAN
    elif(code[position] > raw):
        return GREATERTHAN
    else:
        return EQUAL

def compareToPos(code,pos1,pos2):
    return compareToRaw(code,pos1,code[pos2])

def isEvenPos(code,position):
    return(code[position] % 2 == 0)

def numberOf(code,num):
    return code.count(num)

def isMin(code,pos):
    return code[pos] < code[(pos+1)%3] and code[pos] < code[(pos+2)%3]

def isMax(code,pos):
    return code[pos] > code[(pos+1)%3] and code[pos] > code[(pos+2)%3]

def moreEvens(code):
    return (code[0]%2 + code[1]%2 + code[2]%2 < 2)

def countEvens(code):
    return 3-(code[0]%2 + code[1]%2 + code[2]%2)

def totalEven(code):
    return (code[0]+code[1]+code[2]) % 2 == 0

def sumToRaw(code,pos1,pos2,raw):
    if(code[pos1]+code[pos2] < raw):
        return LESSTHAN
    elif(code[pos1]+code[pos2] > raw):
        return GREATERTHAN
    else:
        return EQUAL
        
def countDups(code):
    count = 0
    if(code[0] == code[1]):
        count +=1
    if(code[0] == code[2]):
        count +=1
    if(code[1] == code[2]):
        count +=1
    if(count == 3):
        count = 2
    return count

def exactPair(code):
    return (countDups(code)==1)

def monotonic(code):
    if(code[0] < code[1] and code[1] < code[2]):
        return INCREASING
    elif(code[0] > code[1] and code[1] > code[2]):
        return DECREASING
    else:
        return CHAOTIC
    
def totalToRaw(code,raw):
    total = code[0] + code[1] + code[2]
    if(total < raw):
        return LESSTHAN
    elif(total > raw):
        return GREATERTHAN
    else:
        return EQUAL

def cardCheck(cardno,code):
    if cardno==0:
        return compareToRaw(code,0,1)
    elif cardno==1:
        return compareToRaw(code,0,3)
    elif cardno==2:
        return compareToRaw(code,1,3)
    elif cardno==3:
        return compareToRaw(code,1,4)
    elif cardno==4:
        return isEvenPos(code,0)
    elif cardno==5:
        return isEvenPos(code,1)
    elif cardno==6:
        return isEvenPos(code,2)
    elif cardno==7:
        return numberOf(code,1)
    elif cardno==8:
        return numberOf(code,3)
    elif cardno==9:
        return numberOf(code,4)
    elif cardno==10:
        return compareToPos(code,0,1)
    elif cardno==11:
        return compareToPos(code,0,2)    
    elif cardno==12:
        return compareToPos(code,1,2)
    elif cardno==13:
        return isMin(code,0)
    elif cardno==14:
        return isMin(code,1)
    elif cardno==15:
        return isMin(code,2)
    elif cardno==16:
        return isMax(code,0)
    elif cardno==17:
        return isMax(code,1)
    elif cardno==18:
        return isMax(code,2)
    elif cardno==19:
        return moreEvens(code)
    elif cardno==20:
        return countEvens(code)
    elif cardno==21:
        return totalEven(code)
    elif cardno==22:
        return sumToRaw(code,0,1,6)
    elif cardno==23:
        return countDups(code)
    elif cardno==24:
        return exactPair(code)
    elif cardno==25:
        return monotonic(code)
    elif cardno==26:
        return totalToRaw(code,6)

def comboCheck(combo):
    firstPoss = cardPossibilities[(combo[0])]
    secondPoss = cardPossibilities[(combo[1])]
    thirdPoss = cardPossibilities[(combo[2])]
    fourthPoss = cardPossibilities[(combo[3])]
    fifthPoss = cardPossibilities[(combo[4])]
    flag = 0;
    for one in firstPoss:
        for two in secondPoss:
            for three in thirdPoss:
                for four in fourthPoss:
                    for five in fifthPoss:
                        printarr = []
                        for thecode in possibleCodes:
                            if(cardCheck(combo[0],thecode)==one and cardCheck(combo[1],thecode)==two and cardCheck(combo[2],thecode)==three and cardCheck(combo[3],thecode)==four and cardCheck(combo[4],thecode)==five):
                                printarr.append(thecode)
                        if(len(printarr)==1):
                            flag +=1
                            saveone = one
                            savetwo = two
                            savethree = three
                            savefour = four
                            savefive = five
                            print("%s %s %s %s %s %s" % (combo, one,two,three,four,five))
                            print(printarr)
    print(flag)
    newcomboone = [combo[1],combo[2],combo[3],combo[4]]
    newcombotwo = [combo[0],combo[2],combo[3],combo[4]]
    newcombothree = [combo[0],combo[1],combo[3],combo[4]]
    newcombofour = [combo[0],combo[1],combo[2],combo[4]]
    newcombofive = [combo[0],combo[1],combo[2],combo[3]]
    if(flag==1 and fourComboCheck(newcomboone,savetwo,savethree,savefour,savefive) and fourComboCheck(newcombotwo,saveone,savethree,savefour,savefive) and fourComboCheck(newcombothree,saveone,savetwo,savefour,savefive) and fourComboCheck(newcombofour,saveone,savetwo,savethree,savefive) and fourComboCheck(newcombofive,saveone,savetwo,savethree,savefour)):
        print("Candidate found")
        choice = input()

def fourComboCheck(combo,one,two,three,four):
    printarr = []
    for thecode in possibleCodes:
        if(cardCheck(combo[0],thecode)==one and cardCheck(combo[1],thecode)==two and cardCheck(combo[2],thecode)==three and cardCheck(combo[3],thecode)==four):
            printarr.append(thecode)
    print(printarr)
    if(len(printarr)>1):
        return True

possibleCodes = []
for first in range(5):
    for second in range(5):
        for third in range(5):
            possibleCodes.append([first+1,second+1,third+1])
cardCombos =[]
for first in range(23):
    for second in range(max(first+1,2),24):
        for third in range(max(second+1,4),25):
            for fourth in range(third+1,26):
                for fifth in range(fourth+1,27):
                    cardCombos.append([first,second,third,fourth,fifth])
for loop in range(NUMOFTRIALS):
    index = random.randrange(len(cardCombos))
    comboCheck(cardCombos[index])