class ChaiUtils:
    @staticmethod  #decorator 
    def clean_ingredients(text):
       return  [item.strip() for item in text.split(",")]
  
 
raw = "Water , milk   , ginger   , honey"

# object = ChaiUtils()

# obj  = ChaiUtils()
# obj.clean_ingredients(raw)

cleaned = ChaiUtils.clean_ingredients(raw)

print(cleaned)

# static method does not require any object creation