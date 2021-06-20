print("Deepanshu Mishra")
print("1900300130029")
n = int(input("Enter  no. of words : "))
l = []
i=0
while i < n:
    x = input("Enter a string : ")
    l.append(len(x))
    i = i+1
print(max(l))