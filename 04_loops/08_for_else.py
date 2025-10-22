staff = [("Amit" , 16) , ("Zara" , 17) , ("Raj" , 15)]

for name,age in staff:
    if age<= 18:
        print(f"{name} is eligibe to manage the staff or hiring ")
        break
else:
    print(f"No one is eligible to manage the staff")