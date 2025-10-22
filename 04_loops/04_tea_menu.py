#enumarate
menu = ["Green" , "lemon" , "Spiced" , "Mint"]
#name = list(enumerate(menu))

#for m in menu:
    #print(f"Mny item is {name}")
    
for idx , item in enumerate(menu , start=1):
    print(f"{idx}: {item} chai")