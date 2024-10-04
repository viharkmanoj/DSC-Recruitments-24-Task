num_bottle = int(input("Enter the number of bottles : "))
xlqty = 0
largeqty = 0
mediumqty = 0
smallqty = 0
res = ""

#xl
while(num_bottle>48):
    num_bottle -= 48
    xlqty += 1
else:
    res += "{} xl, ".format(xlqty)

#large
while(num_bottle>24):
    num_bottle -= 24
    largeqty += 1 
else:
    res += "{} larege, ".format(largeqty)  

#medium
while(num_bottle>12):
    num_bottle -= 12
    mediumqty += 1
else: 
    res += "{} medium, ".format(mediumqty)

#small
while(num_bottle>6 or num_bottle>0):
    num_bottle -= 6
    smallqty += 1 
else:
    res += "{} small".format(smallqty)   

print(res)