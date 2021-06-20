print("Deepanshu Mishra")
print("1900300130029")
a = int(input("Enter the size of list "))

def multiply(n):
    b = 1
    lst = []
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
        b *= ele
    print(lst)
    print(b)
multiply(a)