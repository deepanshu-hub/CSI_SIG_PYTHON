print("DEEPANSHU MISHRA")
print("1900300130029")
a = int(input("Enter a side "))
b = int(input("Enter b side "))
c = int(input("Enter c side "))
check = False
if(a+b>c):
   check = True
   if(b+c>a):
      check = True
      if(a+c>b):
         check = True
if(check == False):
    print("Triangle cannot be formed")
    exit()
if(a == b == c):
    print("Triangle is Equilateral")
    exit()
if(a == b or b == c or c==a):
    print("Triangle is Isosceles")
    exit()
if(a != b != c):
    print("Triangle is Scalene")