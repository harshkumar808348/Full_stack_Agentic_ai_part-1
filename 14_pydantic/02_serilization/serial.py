from pydantic import BaseModel, ConfigDict
from typing import List

from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    
class User(BaseModel):
    id: int
    name: str
    email: str
    createdAt: datetime
    is_active: bool = True
    address: Address
    tags: List[str] = []
    
    
    model_config = ConfigDict(
        
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )
    
user = User(
    id=1,
    name="Hitesh",
    email="h@tesh.ai",
    createdAt=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="Something",
        city="jabalput",
        zip_code="0000234"
    ),
    is_active=False,
    tags=["premium", "Subscriber"]
)
    
    
python_dict = user.model_dump()
print(user)
print("="*30)
print(python_dict)

json_str = user.model_dump_json()
print("="*30)
print(json_str)