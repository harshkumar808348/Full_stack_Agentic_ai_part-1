essential_species = {"cardom" , "ginger" , "cinnamon"}
optional_species = {"cloves" , "ginger" , "blackpepper"}

all_spices = essential_species | optional_species
print(f"All Spices {all_spices}")

common_spies = essential_species & optional_species
print(f"common spices : {common_spies}")

only_in_essential = essential_species-optional_species
print(f"only in essential spices : {only_in_essential}")