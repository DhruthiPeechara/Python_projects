def paren(s,l,r,p,n): 
    if(p==2*n)
        for ss in s 
            print(ss,end='')

        print("\n")
        return
    if(l>r): 
        s[p]= "}"
        paren(s,l,r+1,p+1,n)

    if(l>n)
        s[p]= "{"
     
