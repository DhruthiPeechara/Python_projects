import math; 

def printPowerSet(set,SetSize): 
    PowerSetSize = (int) (math.pow(2, SetSize))
    outer = 0 
    inner = 0 

    for outer in range (0, PowerSetSize): 
        for inner in range (0, SetSize): 

element from set 

            if ((outer & (1 << inner)) >0): 
                print(set[inner], end = "")
        
        print("") 