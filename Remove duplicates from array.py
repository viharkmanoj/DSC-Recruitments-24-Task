input_lst = eval(input("Enter the array with duplicate elements:"))
newlst = []
for i in input_lst:
    if i not in newlst:
        newlst.append(i)
print(newlst)