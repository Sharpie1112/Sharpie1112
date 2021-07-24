from random import random

def gameover_rally(a,b,d):
    return (a>=25 and d>= 2) or (b>=25 and d>= 2)

def simOnegame_rally(a,b):
    serving = "A"
    scoreA = scoreB = d = 0
    while not gameover_rally(scoreA, scoreB, d):
        if serving == "A":
            if random()<a:
                scoreA +=1
            else:
                serving = "B"
                scoreB +=1
        else:
            if random()<b:
                scoreB +=1
            else:
                serving = "A"
                scoreA +=1
        d = abs(scoreA-scoreB)
    return scoreA, scoreB

def gameover(a,b,d):
    return (a>=15 and d>= 2) or (b>=15 and d>= 2)


def simOnegame(a,b):
    serving = "A"
    scoreA = scoreB = d = 0
    while not gameover(scoreA, scoreB, d):
        if serving == "A":
            if random()<a:
                scoreA +=1
            else:
                serving = "B"
              
        else:
            if random()<b:
                scoreB +=1
            else:
                serving = "A"
        d = abs(scoreA-scoreB)
    return scoreA, scoreB

def getInputs():
    a = float(input("Enter the probability of Team A: "))
    b = float(input("Enter the probability of Team B: "))
    n = int(input("How many game should be simulated? "))
    return a, b, n

def simNgames(n, probA, probB):
    winsA = winsB = 0
    for i in range (n):
        scoreA, scoreB = simOnegame(probA, probB)
    
        if scoreA >scoreB :
            winsA +=1
        else:
            winsB +=1
    return winsA, winsB

def simNgames_rally(n, probA, probB):
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOnegame_rally(probA, probB)

        if scoreA>scoreB:
            winsA +=1
        else:
            winsB +=1
    return winsA, winsB

def advantage(a,b):
    if a>b:
        print("Playing in a rally format reduces on the relative advantage enjoyed by the better team.")
    elif a<b:
        print("Playing in a rally format magnifies on the relative advantage enjoyed by the better team.")
    else:
        print("Playing in a rally format has no effect on the relative advantage enjoyed by the better team.")
    
def printTotalwins(winsA1, winsA2, winsB1, winsB2):
    n = winsA1 + winsB1
    print("\n Numbers of games simulated : ",n)
    print("In a normal format")
    print("Team A : {0} and Team B : {1}".format(winsA1, winsB1))
    print()
    print("In a rally format")
    print("Team A : {0} and Team B : {1}".format(winsA2, winsB2))
    
def printSummary(a, b, c, d, probA, probB):
    if probA>probB:
        advantage(a,b)
    else:
        advantage(c,d)

def main():
    probA, probB, n= getInputs()
    winsA1, winsB1 = simNgames(n, probA, probB)
    winsA2, winsB2 = simNgames_rally(n, probA, probB)
    printTotalwins(winsA1, winsA2, winsB1, winsB2)
    print()
    printSummary(winsA1, winsA2, winsB1, winsB2, probA, probB)
main()
    
        
    













        
        
    
        
                    
                
