number = 9
chances = 0
guess = None

while guess != number:
    guess = input("Guess a number between 1 and 10: ") 
    guess = int(guess)

    if guess == number:
        print("Congrats! You Won!")
        break
    else:
        print("You lose! Try again!")
