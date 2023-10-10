import random


x = input("Guess a number: ")
ans = random.choice(1,20)
while(x!=ans):
    if x == ans:
        print ("correct")
print(ans)
