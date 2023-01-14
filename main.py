from random import randint

# list of playing options 
playingOptions = ["Rock", "Paper", "Scissors"]

# get a random playing option from the list, assign it to the pc
pc = playingOptions[randint(0,2)]

player = False 

while player == False:
    player = input("Enter one of the following options: Rock, Paper or Scissors:" + " ")

    if player == pc:
        print("Both you, and computer had the same guess, it is a tie!")

    elif player == "Rock":
        if pc == "Paper": 
            print("You lose!", pc, "is stronger than", player)
        else:
            print("You win!", player, "destroys", pc)

    elif player == "Paper":
        if pc == "Scissors":
            print("You lose!", pc, "destroys", player)
        else:
            print("You win!", player, "is better than", pc)

    elif player == "Scissors":
        if pc == "Rock":
            print("You lose", pc, "smashes", player)
        else:
            print("You win!", player, "cut", pc)

    else:
        print("You have entered wrong option, check your spelling and try that again!")

    player = False
    pc = playingOptions[randint(0,2)]

