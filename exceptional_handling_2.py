try: 
    num1,num2= eval(input("Enter 2 numbers, seperated by comma " ))
    result= num1/num2 
    print("Result is", result)

except ZeroDivisionError: 
    print ("Division by zero is error!!!")

except SyntaxError:
    print ("Comma is missing, Enter numbers seperated by comma like this. 1,2 ")

except:
    print ("Wrong input")

else:
    print("No excepttions ")

final:
    print("This will excecute no matter what")