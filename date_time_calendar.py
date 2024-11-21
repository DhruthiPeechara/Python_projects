from datetime import date , time,  datetime

#calling today 
# func of date class 
today = date.today()
now = datetime.now()
print("Today's date is", now)

#printing date's components 
print ("\nCurrent Date and time is", now)

#Printing date's components 
print ("\nDate components", today.year , today.month , today.day)
