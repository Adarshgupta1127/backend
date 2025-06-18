from pydantic import BaseModel
from typing import List

class GroupCreate(BaseModel):
    name: str
    user_ids: List[int]

class GroupOut(BaseModel):
    id: int
    name: str
    user_ids: List[int]

    class Config:
        orm_mode = True
