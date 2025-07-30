# pseudo-code for the activity:
# Generate a random number -- random modules
# do while - Python doesn't have this built in
# do something once -- possibly repeat it
# ask us for a number. If we get it wrong, ask again
# logic for right / wrong: guessed == correct value

from random import randint

# lowest and highest number inclusive
# need to convert into an int, otherwise it's a str
# low = 0
# high = 100
# correct = int(randint(0, 100))
# print(f"Guess a number between {low} and {high}.")
# print(type(correct))
# print(correct)

# Choose game's difficulty
difficulty = int(input("Choose the game's difficulty: 1, 2 or 3\n"))
while True:
    if difficulty == 1:
        correct = int(randint(0 ,10))
        print("From 0 to 10.")
        break
    elif difficulty == 2:
        correct = int(randint(0, 50))
        print("From 0 to 50.")
        break
    elif difficulty == 3:
        correct = int(randint(0, 100))
        print("From 0 to 100.")
        break
    else:
        print("Choose a correct difficulty")


# need to convert into an int, otherwise it's a str
while True:
    guess = int(input("Guess a number: "))
    if guess < correct:
        print("Guess higher")
    elif guess > correct:
        print("Guess lower")
    else: 
        break

print("You win!")
