
def get_input():
    
    try:
        input_value = int(input("Enter Your Selection Number: "))
        return input_value
    
    except:
        print("Please Enter Decimal Number")
        get_input()