import random
correct = "false"
guess = 0
history = []
num = random.randint(1,10)
while correct == "false":
    guess = int(input("Guess a number between 1 and 10: "))
    history.append(guess)
    if guess == num:
        print("Correct!")
        correct = "true"
    elif guess > num:
        print("Lower")
    elif guess < num:
        print("Higher")
    else:
        print("huh")
print(history)