from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic import ValidationError

class User(BaseModel):
    id: int
    name = 'Jahid Hassan'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

external_data = {
    'id': '123',
    'signup_ts': '2022-08-05 12:40',
    'friends': [1, 2, '3'],
}

user = User(**external_data)

print(user.id)
print(repr(user.signup_ts))
print(user.friends)
print(user.dict())
