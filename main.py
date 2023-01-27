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
    else:   
        match player:
            case "Rock":
                if pc == "Paper": 
                    print("You lose!", pc, "is stronger than", player)
                else:
                    print("You win!", player, "destroys", pc)

            case "Paper":
                if pc == "Scissors":
                    print("You lose!", pc, "destroys", player)
                else:
                    print("You win!", player, "is better than", pc)

            case "Scissors":
                if pc == "Rock":
                    print("You lose", pc, "smashes", player)
                else:
                    print("You win!", player, "cut", pc)

            case _:
                print("Invalid Input")

player = False
pc = playingOptions[randint(0,2)]
