x = input("Enter your bill value: ")
tip = input("Enter how your service was, bad, okay, good, great:  ")
if tip == "bad":
    print("your tip is 0%, lucky")
elif tip == "okay":
    print("your tip is 15%")
elif tip == "good":
    print("your tip is 20%")
elif tip == "great":
    print("your tip is 25%")
else:
    print("That's not what I asked")
