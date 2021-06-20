f = open("C:/users/Dell/desktop/text1.txt", mode='w', encoding='utf-8')
lst = ["Python", "Java", "C++", "HTML", "CSS"]
f.writelines(lst)
f.close()
f = open("C:/users/Dell/desktop/text1.txt", mode='r', encoding='utf-8')
print(f.read())