wordlen = []
newstr = ""
input_string = input("Enter the string:").split()
for i in input_string:
     wordlen.append(len(i))
wordlen.sort()

for i in wordlen:
    for n in input_string:
        if(len(n)==i):
              newstr = newstr + n + " "
              input_string.remove(n)
print(newstr)
