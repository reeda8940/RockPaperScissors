import random
print("""Welcome to rock paper scissors. I will ask for an input and you will input either rock, paper or scissors. 
The first person to 5 points wins the game""")
p1 = 0
computor = 0

#  play function (Infinite mode)
while True:

    userInput = input("What do you want to do. Rock, Paper, or scisors: ") 
    userInput = userInput.lower()
    computorInput = random.choice(["paper", "scissors", "rock"])

    if userInput == "paper" and computorInput == "rock":

        p1 += 1
        print(f"Your input: {userInput}. Computor input: {computorInput}")
        print(f"""You win this round.
        SCORE: {p1}:{computor}""")

    elif userInput == computorInput:

        print(f"Your Input: {userInput}. Computor input: {computorInput}")
        print(f"""This round is a tie. No points awarded. 
        SCORE. P1:{p1}:Computor:{computor}""")