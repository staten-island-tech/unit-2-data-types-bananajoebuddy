#If I get greater than 0 for my open door (x) and got to school (y) then I wont get a beating from my mom 

x = int(input("how many times did you open your door today?: "))
y = input("did somehow get to school?: ")

if x > 0 and y == "True":
    print("you met barack obama!")
else:
    print("Your mom gave you a belting.")