import random
randomNumber = random.randint(1,10)
guesses = 0
while guesses < 5:
    number = int(input("Guess the number :"))
    if randomNumber == number:
        print("you win")
        break
    elif number < randomNumber:
        print("Your guess was low")
    else:
        print("Your guess was too high")
    guesses = guesses+1
if guesses == 5:
    print("You Lose")