def ways(stairs):
    if staircase<0: 
        return 0 
    if stairs ==0: 
        return 1 
    twoSteps=0
    oneStep=0

    if (stairs>=2): 
        twoSteps = ways(stairs-2)

    oneStep = ways(stairs-2)
    return twoSteps+oneStep 

stairs = int(input("Enter number of steps"))

print(" Number of ways to climb" , ways(stairs))

