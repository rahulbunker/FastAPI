def insert_patient_data(name : str , age : int):
    if type(name) == str and type(age) == int:
        if age >0:
            print(name)
            print(age)
            print("inseted into database")
        else:
            raise ValueError("age con't be negative")


    else:
        raise TypeError("Incorrect data type")
    

insert_patient_data("rahul" , 24)

def update_patient_data(name : str , age : int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("inseted into database")


    else:
        raise TypeError("Incorrect data type")
    
    # 1 problem typle validation
    # 2 data validation
