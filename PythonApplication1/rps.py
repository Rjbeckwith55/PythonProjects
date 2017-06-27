import random

rps = ["Rock","Paper", "Scissors"]
score = 0
while True:
    choice = random.choice(rps)

    yourChoice = input("Choose Rock, Paper or Scissors: ")
    yourChoice = yourChoice.title()
    if(yourChoice == "p" or yourChoice == "P"):
        yourChoice = rps[1]
    if(yourChoice == "r" or yourChoice == "R"):
        yourChoice = rps[0]
    if(yourChoice == "S" or yourChoice == "s"):
        yourChoice = rps[2]
    if (yourChoice == choice):#Rock vs Rock or Scissors vs Scissors or Paper vs Paper
        print(choice)
        print("Tie")
    elif(choice == rps[0] and yourChoice == rps[1]): #Rock vs Paper
        print(choice)
        print("You Win")
        score+=1
    elif(choice ==rps[1] and yourChoice == rps[2]): #Paper vs Scissors
        print(choice)
        print("You Win")
        score+=1
    elif(choice == rps[0] and yourChoice == rps[2]): #Rock vs Scissors
        print(choice)
        print("You Lose")
        score-=1
    elif(choice == rps[1] and yourChoice == rps[0]): #Paper vs Rock
        print(choice)
        print("You Lose")
        score-=1
    elif(choice == rps[2] and yourChoice == rps[0]): #Scissors vs Rock
        print(choice)
        print("You Win")
        score+=1
    elif(choice ==rps[2] and yourChoice == rps[1]): #Scissors vs Paper
        print(choice)
        print("You Lose")
        score-=1
    else:
        print("invalid input")
    print("Score:",score)