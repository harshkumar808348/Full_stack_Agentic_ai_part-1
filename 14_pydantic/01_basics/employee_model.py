from typing import Optional

from pydantic import BaseModel,Field

class Employee(BaseModel):
    id:int
    name:str = Field(
        ...,  ##  ... denotes denotes the requird filed 
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Hitesh Choudhry"
    )
    department:Optional[str] = 'General'
    salary:float = Field(
        ...,
        ge=10000    # ge means(greater) the salary are greater than 10000 
        
    )
    
class User(BaseModel):
    email:str = Field(
        ...,
        regex=r''
    )
    phone:str =Field(
        ...,
        regex = r''
    )
    age:int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in Years",
    )
    discount:float = Field(
        ...,
        ge=0,
        le=100,
        description="discount percentage"
    )
    