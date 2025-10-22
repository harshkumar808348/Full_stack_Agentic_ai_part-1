is_boiling  = True
stri_count = 5

# true representing as 1 
# false representing as 0

total_actions = stri_count + is_boiling   # upcasting

print(f"Total actions:{total_actions}")


milk_present = 0
print(f"is there milk? {bool(milk_present)}")


# logical operation 
# Three types in python and,or,not

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can serve chai?{can_serve}")
