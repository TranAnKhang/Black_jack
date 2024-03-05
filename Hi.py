import random #import to random oste na mporei na parei kati tixaio
score = 0
round = 0

def welcome():#friendly introduction
    print("Lets begin!")
    print("Your choices are:")
    print("1. 'rock' or 'r' for ROCK")
    print("2. 'paper' or 'p' for PAPER")
    print("3. 'scissors' or 's' for SCISSORS")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")   
welcome()

def rounds():
    global round
    round += 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> " + "ROUNDS: " + str(round))


def output():
    print("Your choice was {}".format(playerChoice.upper()))
    print("The computer chose {}".format(computerChoice.upper()))
    


def gameStart(playerChoice, computerChoice, score):
    botScore = 0
    if (playerChoice == "rock" or playerChoice == "r") and computerChoice == "rock":
        output()
        print("This round is drawn!")
    elif (playerChoice == "rock" or playerChoice == "r") and computerChoice == "paper":
        output()
        print("Close one! You'll get me next time!")
        botScore += 1
    elif (playerChoice == "rock" or playerChoice == "r") and computerChoice == "scissors":
        output()
        print("You won this round congrats!")
        score += 1
    elif (playerChoice == "scissors" or playerChoice == "s") and computerChoice == "scissors":
        output()
        print("This round is drawn!")
    elif (playerChoice == "scissors" or playerChoice == "s") and computerChoice == "rock":
        output()
        print("Close one! You'll get me next time!")
        botScore += 1
    elif (playerChoice == "scissors" or playerChoice == "s") and computerChoice == "paper":
        output()
        print("You won this round congrats!")
        score += 1
    elif (playerChoice == "paper" or playerChoice == "p") and computerChoice == "paper":
        output()
        print("This round is drawn!")
    elif (playerChoice == "paper" or playerChoice == "p") and computerChoice == "scissors":
        output()
        print("Close one! You'll get me next time!")
        botScore += 1 
    else:
        output()
        print("You won this round congrats!")
        score += 1
    return score


#YesNo = "yes"
playerChoice = ""
while playerChoice != "stop":
    #YesNo = input("Would you like to play with me? yes/no")
    choices = ["rock", "paper", "scissors"]
    computerChoice = random.choice(choices)
    print("Ok let's play.")
    print("Score: %s" % score)
    playerChoice = input("Enter your choice here: ")
    if playerChoice.lower() == "r":
        playerChoice = "Rock"
    elif playerChoice.lower() == "p":
        playerChoice = "Paper"
    elif playerChoice.lower() == "s":
        playerChoice = "Scissors"
    #else:
        #playerChoice = "WrongWord"
    playerChoice = playerChoice.lower()
    if (not playerChoice in choices) and playerChoice != "stop":
        print("invalid word")
        break
    if playerChoice != "stop":
        score = gameStart(playerChoice, computerChoice, score)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> " + "YOUR SCORE: {}".format(score))
        rounds()
print("Ok see you next time.")





