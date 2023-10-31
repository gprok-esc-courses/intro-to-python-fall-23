import random

secret = random.randint(1, 100)
print(secret)

efforts = 0
guess = 0
while secret != guess:
    efforts = efforts + 1
    guess = int(input("Guess: "))
    if guess < secret:
        print("GO UP")
    elif guess > secret:
        print("GO DOWN")
    else:
        print("CONGRATS! Found in", efforts, " guesses." )
print("GAME OVER")