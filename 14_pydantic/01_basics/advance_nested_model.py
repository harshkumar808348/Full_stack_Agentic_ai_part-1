from pydantic import  BaseModel
from typing import Optional ,Union

class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    

class Company(BaseModel):
    name:str
    address:Optional[Address] = None
    
    
class Employee(BaseModel):
    name:str
    company:Optional[Company] = None
    
    
class TextConent(BaseModel):
    type:str = "text"
    content:str
    
class ImageContent(BaseModel):
    type:str = "Image"
    url:str

class Article(BaseModel):
    title:str
    sections:list[Union[TextConent,ImageContent]]
    