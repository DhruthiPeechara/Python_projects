numberLargest = int(input("Enter the largest number"))
numberSamllest = int(input("Enetr the smallest number"))

while (numberSamllest):
    numberStore = numberSmallest 
    numberSmallest = numberLargest % numberSmallest 
    numberLargest = numberStore 

    print("HCF is " , numberLargest)
    
