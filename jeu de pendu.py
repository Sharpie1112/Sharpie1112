from random import randrange
def chooseaword():
    liste_mots = ["armoire","boucle","buisson","bureau",
                 "chaise","carton","couteau","fichier",
                 "garage","glace","journal","kiwi","lampe",
                 "liste","montagne","remise","sandale","taxi",
                 "vampire","volant"]
    i = randrange(0,20)
    return liste_mots[i]

    
def main():
    word = chooseaword()
    n = len(word)
    p = n-1
    position = 1
    message = word[0]
    
    print(message + p *"*")
    
    tentative = 0
    while tentative != 8:
        guess = input("Enter the next caracter: ")
        if guess == word[position]:
            p -=1
            message = message + guess
            print(message+ p * "*")
            position+=1
        tentative +=1

        if word == message :
            print("You guessed the word")
            break
    if tentative ==8 :
        print("You lost, the word was "+ word +".")

main()
        

