from typing import List, Optional

from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str
    
    
class User(BaseModel):
    id: int
    name: str
    address: Address
    
    
address = Address(
    street="123",
    city="jaipur",
    postal_code="1000002"
)

user = User(
    id=1,
    name="hitesh",
    address=address,
)


user_data = {
    "id": 1,
    "name": "hitesh",  # Fixed: added missing comma here
    "address": {
        "street": "31 something",
        "city": "paris",
        "postal_code": "20002"
    }
}


user = User(**user_data)
print(user)
