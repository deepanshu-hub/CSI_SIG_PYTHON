f = open("C:/users/Dell/desktop/text.txt", mode='r', encoding='utf-8')
n = int(input("Enter the no. line you want to read : "))
x = 0
for line in f:
    x = x + 1
    print(x,")",line, end='')
    if x==n:
      break