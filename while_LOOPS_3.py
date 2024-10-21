#input a number 

n = int(input("enter a number : "))

sum = 0 

temp=n 

while temp > 0 :
    digit = temp%10
    sum+= digit**3 
    temp//=10 

    if n==n : 
        print ("This is an armstrong number ")
    else :
        print ("This is not an armstrong number ")








