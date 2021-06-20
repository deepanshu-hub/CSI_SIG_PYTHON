print("Deepanshu Mishra")
print("1900300130029")
print("press @ to stop the input")
x = ""
l = []
x = input("Enter element in a list : ")
while(x != "@"):
    l.append(x)
if(len(l) == 0):
    print("List is empty")
else:
    print("List is not empty")