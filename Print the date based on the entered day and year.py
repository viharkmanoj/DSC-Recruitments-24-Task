from datetime import datetime
day_year = eval(input("Enter day,year:"))
day_num = str(day_year[1])
year = str(day_year[0])
day_num.rjust(3 + len(day_num), '0')
res = datetime.strptime(year + "-" + day_num, "%j-%Y").strftime("%d %B,%Y")
print("Resolved date : " + str(res))