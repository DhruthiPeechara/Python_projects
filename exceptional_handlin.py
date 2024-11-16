try:
    number= int(input("Enetr a number:"))
    print("The number entered is", number)

except ValueError as ex: 
    print("Exception:", ex)