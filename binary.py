def swap (a,b): 

    a = a ^b 
    b = a ^ b 
    a = a ^ b 
    print (" After swapping  a = ", a, " b =", b )

def swap (a,b):
    a = (a&b) + (a | b )
    b = a + (~b)+ 1 
    a = a + (~b) + 1 
    print (" After swapping  a = ",a, "b = ", b  )

swap(1,2)
swap(1,2)

