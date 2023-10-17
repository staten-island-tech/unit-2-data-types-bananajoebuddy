
lastname = input("Enter your last name with Captial: ")
firstinitial = list(lastname)
homeroom = ["101,102,103"]

if firstinitial[0] == ("A"):
    print("you're in 101")
elif firstinitial[0] == ("B"):
    print("you're in 102")
else:
    print("you're in 103, congrats on the largely populated class.")

#program 2

lastname2 = input("Enter your last name:  ")
firstinitial2 = list(lastname2)
homeroom2 = ["101,102,103"]
if firstinitial2[0] in ["A,","B,","C,","D,","E,","F,","G"]:
    print("you're in homeroom 101")
elif firstinitial2[0] in ["H","I,","J,","K,","L,","M,","N,","O,","P"]:
    print("you're in 102")
else:
    print("you're in homeroom 103, good luck")

