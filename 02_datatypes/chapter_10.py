chai_order  = dict(type="Masala Chai" , size = "Large" , sugar = 2)
print(chai_order)

chai_recipe = {} 
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipi base: {chai_recipe['base']}")
del chai_recipe["liquid"]
print(f"Recipi base: {chai_recipe}")

print(f"Is Sugar in  the order? {'sugar' in chai_order} ")

chai_order  = dict(type="Masala Chai" , size = "Large" , sugar = 2)

# print(f"order details (key):{chai_order.keys()}")
# print(f"order details (value):{chai_order.values()}")

last_item = chai_order.popitem() # just remove the item 

extra_spices = {"cardom" :"crushed" , "ginger" : "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated {chai_recipe}")
