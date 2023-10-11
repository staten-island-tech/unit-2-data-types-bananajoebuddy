import random
correct = "false"
guess = 0
num = random.randint(1,10)
while correct == "false":
    guess = int(input("Guess a number: "))
    history = list()
    if guess == num:
        print("Correct!")
        correct = "true"
    elif guess > num:
        print("Lower")
        history.append(guess)
    elif guess < num:
        print("Higher")
        history.append(guess)
    else:
        print("huh")
print(history)