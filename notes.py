#Taking total amount as input from user 
Amount = int (input ("Please Enter Amount for withdraw:"))

#Calculating the number of notes of different demonations 
note_1 = Amount/100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print ("NOTES OF 100 RUPEES", note_1)
print ("NOTES OF 50 RUPEES", note_2)
print ("NOTES OF 10 RUPEES", note_3)
