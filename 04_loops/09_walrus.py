# value = 13
# remainder = value%5

# if remainder:
#     print(f"Not divisible , remaider is {remainder}")


  #              by Walrus operator
  
value = 13
              #walrus operator
if remaninder :=value%5:
    print(f"Not divisible , remaider is {remaninder}")
    
available_sizes = ["Small" , "medium" , "large"]

if (requested_size := input("Enter your chai cup size")) in available_sizes:
    print(f"Serving requested size {requested_size}")
else:
    print(f"Size id unlable - {requested_size}")