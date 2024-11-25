import random 
import time 

def getRandomDate (startDate, endDate):
    print("Printing random date between ", startDate, 'and',endDate )
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime