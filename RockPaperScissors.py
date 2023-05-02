import random
# Rules
start = input("""Welcome to rock paper scissors. I will ask for an input and you will input either rock, paper or scissors or end to stop the game. 
The rules are rock beats scissors, paper beats rock, and scissors beats paper. The first one to the selected amount of rounds win
Press <ENTER> to continue """)
# Variables
p1 = 0
computor = 0
play = 0
infinitePlay = 0
# used to wait untill the user clicks enter to continue to the game to say that they have read the rules  
if start == "":

    # asking user how many rounds they want to play
    numOfRounds = int(input("How many rounds do you want to play (type <0> if you want to play infinite mode): "))

    if numOfRounds != 0:
        #  play function (Selected mode)
        while play < numOfRounds:

            userInput = input("What do you want to do. Rock, Paper, scisors: ") 
            userInput = userInput.lower()
            computorInput = random.choice(["paper", "scissors", "rock"])
             
            if userInput == "paper" and computorInput == "rock":

                p1 += 1
                print(f"""
Your input: {userInput}. Computor input: {computorInput}""")
                print(f"""
You win this round.
SCORE: {p1}:{computor}
                """)
                play += 1

            elif userInput == computorInput:

                print(f"""
Your Input: {userInput}. Computor input: {computorInput}""")
                print(f"""
This round is a tie. No points awarded. 
SCORE: P1:{p1} Computor:{computor}
                """)
                play += 1

            elif userInput == "rock" and computorInput == "scissors":

                p1 += 1
                print(f"""
Your input: {userInput}. Computor input: {computorInput}""")
                print(f"""
You win this round.
SCORE: {p1}:{computor}
                """)
                play += 1
    
            elif userInput == "scissors" and computorInput == "paper":
                p1 += 1
                print(f"""
Your input: {userInput}. Computor input: {computorInput}""")
                print(f"""
You win this round.
SCORE: {p1}:{computor}
                """)
                play += 1

            else:
                computor += 1
                print(f"""
Your input: {userInput}. Computor input: {computorInput}""")
                print(f"""
You lost this round.
SCORE: {p1}:{computor}
                """)
                play += 1
        print(f"""Game over
SCORES: P1:{p1} Computor:{computor}""")
        if p1 > 0:
            print("Your won the game")
        elif p1 < computor:
            print("The computor won the game")
        elif p1 == computor:
            print("This game is a tie")
    elif numOfRounds == 0:
        #play function (infinite mode)
        while infinitePlay < 1:

            userInput = input("What do you want to do. Rock, Paper, scisors or end: ") 
            userInput = userInput.lower()
            computorInput = random.choice(["paper", "scissors", "rock"])

            if userInput == "end":
                print(f"Final score: P1:{p1} Computor:{computor}")
                if p1 > computor:
                    print("The computor won the game")
                elif p1 < computor:
                    print("You won the game")
                elif p1 == computor:
                    print("This game is a tie")
                break 
    
            if userInput == "paper" and computorInput == "rock":

                p1 += 1
                print(f"""
Your input: {userInput}. Computor input: {computorInput}""")
                print(f"""
You win this round.
SCORE: {p1}:{computor}
                """)

            elif userInput == computorInput:

                print(f"""
Your Input: {userInput}. Computor input: {computorInput}""")
                print(f"""
This round is a tie. No points awarded. 
SCORE: P1:{p1} Computor:{computor}
                """)

            elif userInput == "rock" and computorInput == "scissors":

                p1 += 1
                print(f"""
Your input: {userInput}. Computor input: {computorInput}""")
                print(f"""
You win this round.
SCORE: {p1}:{computor}
                """)
    
            elif userInput == "scissors" and computorInput == "paper":
                p1 += 1
                print(f"""
Your input: {userInput}. Computor input: {computorInput}""")
                print(f"""
You win this round.
SCORE: {p1}:{computor}
                """)

            else:
                computor += 1
                print(f"""
Your input: {userInput}. Computor input: {computorInput}""")
                print(f"""
You lost this round.
SCORE: {p1}:{computor}
                """)

