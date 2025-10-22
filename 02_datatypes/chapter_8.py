# list 


ingredients = ["water" , "milk" , "black tea " ]
ingredients.append("sugar")
print(f"Ingredients are :{ingredients}")
ingredients.remove("milk")
print(f"Ingredients are :{ingredients}")

spice_options = ["ginger" , "cardon"]
chai_ingredients = ["water" , "milk"]

chai_ingredients.extend(spice_options)
print(f"chai : {chai_ingredients}")

chai_ingredients.insert(2,"black tea")
print(f"chai : {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"Remove {last_added}")

chai_ingredients.sort()
print(chai_ingredients)


sugar_level = [1,2,3,4,5]
print(f"Maximum sugar level : {max(sugar_level)}")
print(f"Mi sugar level : {min(sugar_level)}")


base_liquid  = ["water " , "milk"]
extra_flavour = ["ginger"]

full_liquid = base_liquid + extra_flavour # operator overloading 
print(f"liquid mix:{full_liquid}")


# operator overloading 
strong_brue = ["black tea" , "water"] * 3
print(f"Strong breq: {strong_brue}")

# from operator import itemgetter


raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA" , b"CARD")

print(f"Bytes:{raw_spice_data}")