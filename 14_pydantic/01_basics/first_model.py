from pydantic import BaseModel

class User(BaseModel):
    id: int
    name:str
    is_active: bool
    
input_data = {'id':101 , 'name':"chaiCode" , 'is_active':True}

user = User(**input_data) ## all  the inside value scattered around
print(user)


# pydantic try to convert it or it raise the validation error 