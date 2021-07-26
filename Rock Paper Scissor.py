from random import randrange
class Ordichoice:
    def __init__(self):
        self.value = 0

    def choose(self):
        n = randrange(0,3)
        choice = ["rock","paper","scissor"]
        return choice[n]

def printSummary(rounds, scoreO, scoreU, draw):
    print("Rounds played: ",rounds)
    print("You won {0} times, the computer won {1} times , and it was a draw {2} times".
          format(scoreU, scoreO, draw))
def ending():
    print("See you next time")
    print(";)")
    
def main():
    print("This is a rock/paper/scissor game")
    print("The game will keep running until you quit>")
    print("Have FUN :)")
    print()
    scoreO = scoreU = draw = 0
    choice = ["rock","paper","scissor"]
    ordi = Ordichoice()
    rounds = 0

    while True:
        user = input("Choose between (Rock/Paper/Scissor) or press q to quit: ")
        if user.lower() == "q":
            break

       
        while user.lower() not in choice :
            user = input("Enter a valid option: ")
            if user == "q" : break
        if user == "q" : break

           
        play = ordi.choose()
        print("The computer choose", play)

        if (user.lower()== "rock" and play == "scissor") or (user.lower()== "scissor" and play=="paper") or (user.lower() == "paper" and play =="rock"):
            scoreU +=1
            print("you win this round")
        elif user.lower() == play:
            draw +=1
            print("It s a draw")
        else:
            scoreO +=1
            print("You lost this round")

        print()
        rounds += 1
        
    print()  
    if rounds == 0:
        ending()
    else:
        printSummary(rounds, scoreO, scoreU, draw)
        ending()

main()

        
    
