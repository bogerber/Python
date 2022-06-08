s1 = ""
s2 = ""
x = 0
z = 0
y = 0

s1 = input("enter text")
s2 = input("enter text")
x = int(input("enter number"))

if (len(s1) + len(s2)) > x:
    y = int(input("enter number"))
    z = int(input("enter number"))
    if y > z:
        print(y)
    else:
        print(z)


