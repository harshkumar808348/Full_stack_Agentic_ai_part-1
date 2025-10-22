from pydantic import BaseModel , field_validator , model_validator

class User(BaseModel):
    username:str
    
    
    
    @field_validator('username')
    def username_length(cls , v):
        if len(v) < 4:
            raise ValueError("user name must be atleast 4 character")
        
        return v
    
    
    
class SignupData(BaseModel):
    password:str
    confirm_password: str
    
    
    @model_validator(mode='after')
    def password_match(cls,value): #first parameter alwyas call itself
        if value.password !=value.confirm_password:
            raise ValueError("Password not match")
            
        return value
    