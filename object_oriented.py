class A:
        def __init__(self,a):
            self.a = a 
        def __It__(self,other):
              if(self.a<other.a):
                    return "ob1 is less than ob2"
              else:
                    return "ob2 is less than ob1"
        def __eq__ (self,other):
              if(self.a == other.a): 
                    