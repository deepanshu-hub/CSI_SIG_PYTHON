print("Deepanshu Mishra")
print("1900300130029")
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a > b:
    if a < c:
        m = a
    elif b > c:
        m = b
    else:
        m = c
else:
    if a > c:
        m = a
    elif b < c:
        m = b
    else:
        m = c

print("The meadian is", m)