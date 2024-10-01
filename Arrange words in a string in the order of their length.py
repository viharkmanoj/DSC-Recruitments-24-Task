dict1 = {}
newstr = ""
input_string = input("Enter the string:").split()
for i in input_string:
     dict1[i]=len(i)
     wordlen = list(dict1.values())
wordlen.sort()

for i in wordlen:
    for n in dict1:
        if(dict1[n]==i):
            if (n not in newstr):
              newstr = newstr + n + " " 
print(newstr)