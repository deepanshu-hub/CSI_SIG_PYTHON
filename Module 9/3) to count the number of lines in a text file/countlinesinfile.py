f = open("C:/users/Dell/desktop/text.txt", 'r')
x = 0
for line in f:
    x = x + 1
    print(x,")",line, end='')
print("Total lines in a file are ", x)