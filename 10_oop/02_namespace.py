class Chai:
    origin = "India"
    
print(Chai.origin)

#when the varibale go inside the class it refer as object

Chai.is_hot = True
print(Chai.is_hot)

# creating object from class chai

masala = Chai()
print(masala.origin)
print(masala.is_hot)

#each object  has a seperate namespace

