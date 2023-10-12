import random
correct = "false"
guess = 0
num = random.randint(1,10)
while correct == "false":
    history = list()
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == num:
        print("Correct!")
        correct = "true"
    elif guess > num:
        print("Lower")
    elif guess < num:
        print("Higher")
    else:
        print("huh")
history += guess
print(history)