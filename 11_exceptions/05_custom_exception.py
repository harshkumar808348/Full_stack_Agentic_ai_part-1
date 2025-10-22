def brew_chai(flavour):
   if flavour not in ["masala" , "ginger" , "elaichai" ]:
       raise ValueError("Unsupported chai flavour...")
   print(f"brewing {flavour} chai...")
    
    
brew_chai("masala")