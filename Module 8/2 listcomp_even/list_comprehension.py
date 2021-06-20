lst = [int(var) for var in input("Enter the list items : ").split()]
lst_comp = [var for var in lst if var % 2 == 0]
print(lst)
print(lst_comp)