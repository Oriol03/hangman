from picture import *
from random import *

game_on =True
while game_on:
    life=-1


    print(logo )
    word_choosen=choice(hangman_words).lower()

    blank=[]
    for i in range(len(word_choosen)):
        blank.append("_")
    print(blank)
    while life<6 and "_" in blank:
        letter=input("Guess a letter please   ").lower()
        if letter in blank:
                print(f"{letter} is  already choosen")
        elif  letter in word_choosen:
            for position in range(len(word_choosen)) :
            
                if  word_choosen[position]== letter:
                    blank[position]=letter
            
            print(blank)
        else:
            print (f"You lose one life . You have {5-life} live left ")
            life+=1
            print(HANGMAN_PICS[life])
    if not ("_" in blank):
        print("congratulations, you win  ")
    else :
        print (f"The country  was {word_choosen} ")
        print ("You lose !!               Game Over ")
    ask_cont=input ("\n\nTo try again ,type 1 , to stop 0   \n")
    if ask_cont=="0":
        game_on=False