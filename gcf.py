a=int(input("Enter an integer: "))
b =int(input("Enter another integer: "))
r = a%b
q = int(a/b)
while(r!=0):
    a = b
    b = r
    q = int(a/b)
    r = a - (b * q)
print(b)
