class InvalidChaiError(Exception):
    pass

def bill(flavour , cups):
    menu = {"masala":20 , "ginger":40}
    try:
        if flavour not in menu :
            raise InvalidChaiError("That chai is not available")
        if not isinstance(cups , int):
            raise TypeError("Number of cups must be in integer")
        
        total = menu[flavour] * cups
        
        print(f"YOur bill for {cups} cups of {flavour}chai: rupees {total}")
    except Exception as e:
        print("Error",e)
        
    finally:
        print("Thank you for visiting chai code!")
        
bill("mint" , 2)
bill("Masala" , "three")
bill("ginger" , 3)