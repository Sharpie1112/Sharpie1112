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
    
    list = []
    for i in range(n):
        list.append("*")
    message = n *"*"
    
    print(message)
    print("Your word have {} letters.".format(n))
    print()
    
    tentative = 0
    while tentative != 8:
        guess = input("Enter a letter: ")
    
        if guess in word:
            
            v = word.count(guess)
            
            if v==1:
                pos = word.find(guess)
                list[pos] = guess
                message = "".join(list)
                print(message)
            else:
                pos = word.find(guess)
                list[pos] = guess
                pos = word.rfind(guess)
                list[pos] = guess
                message = "".join(list)
                print(message)
                

        tentative +=1

        if word == message :
            print("You guessed the word")
            break
    if tentative ==8 :
        print("You lost, the word was "+ word +".")

main()
        

