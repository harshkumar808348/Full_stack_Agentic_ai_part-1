class Chaicup:
    size = 150 # ml
    
    
    
    def describe(self):
        return f"A {self.size} ml cup chai"
    
    
    
cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two_size = 100
print(Chaicup.describe(cup_two))