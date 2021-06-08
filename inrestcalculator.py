amount=int(input("enter the amount:"))
intrest=int(input("enter the interst:"))
years=int(input("enter the number of years:"))
permonth=(amount*intrest)/100
peryears=permonth*12*years
print("final intrest that you earn::::::::::::::::::::",peryears)
print("total amount that he have to give::::::::",amount+peryears)
