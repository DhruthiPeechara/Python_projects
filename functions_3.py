def add (P,Q):
    return P+Q

def subtract (P,Q): 
    return P-Q

def multiply (P,Q):
    return P*Q

def divide (P,Q):
    return P/Q

#Giving options for choices 

print ("Select operation")

print(a= "Add")
print(b="Subtract")
print(c="Multiply")
print(d = "Divide")

choice= input("PLease choose a/b/c/d ")

choice_1 = int(input("Enter a number "))
choice_2 = int(input("Enter 2nd number "))

if (choice==a):
    print("The sum is " + choice_1+choice_2)

elif (choice==b):
    print("The difference is "+ choice_1-choice_2)
