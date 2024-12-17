# creating the class 

class vehicle:
    def __init__(self,max_speed,mileage):

        #binding the arguments 
        self.max_speed = max_speed 
        self.mileage = mileage 

        #object creation 

modelX = vehicle(240, 18)

    # access the variables inside init method 

print("Model Max speed:",modelX.max_speed)
print("model mileage:", modelX.mileage)

