class employee:
    def __init__(self):
        print("Employee created") 

    def __del__(self):
        print("Destructor called ")

    def Create_obj():
        print("Making object ....")
        obj= employee()
        print('function end ...')
        return obj 
    
print('calling Create_obj() function ')
obj = create_obj()
print('program end')