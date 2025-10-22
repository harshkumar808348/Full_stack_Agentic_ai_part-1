class Chai:
    temperature = "Hot"
    strength = "Strong"
    
cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"  # by the object we have to change
print("After Changing ", cutting.temperature)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature
print(cutting.temperature)