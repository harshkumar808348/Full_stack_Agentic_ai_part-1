def process_order(item,quantity):
    try:
        price = {"masala": 20}[item]
        cost = price*quantity
        print(f"total cose id {cost}")
        
    except KeyError:
        print("Sorry that chai is not in the menu")
        
    except TypeError:
        print("Quantity  must be in number")
        
process_order("ginger" , 2)
        
process_order("masala" , "two")
