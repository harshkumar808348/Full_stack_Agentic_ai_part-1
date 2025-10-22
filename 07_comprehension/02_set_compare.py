favourite_chai = [
    "Masala Chai" , "Green Tea" , "Masala Chai",
    "Lemaon Tea" , "Green Tea" , "Elaichi Tea"
]

unique_chai = {chai for chai in favourite_chai if len(chai) > 8 }
print(unique_chai)

recipes = {
    "Masala Chai" : ["Ginger" , "cardamon" , "clove"],
    "Elaichi chai":["cardamon" , "milk"],
    "Spicy Chai": ["ginger" , "black peeper" , "clove"]
    
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)