#Get 2 numbers from the user.
#If the multiplaction of them is smaller than 100,
# print "Small result"

num1 = int(input("Enter number"))
num2 = int(input("Enter number"))


#Option 1
num3 = num1 * num2
if num3 < 100:
    print("Small result")

#Option 2
if num1*num2 < 100:
    print("Small result")