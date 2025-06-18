from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class SplitSchema(BaseModel):
    user_id: int
    percentage: Optional[float] = None

class ExpenseCreate(BaseModel):
    description: str
    amount: float
    paid_by: int
    split_type: str  # 'equal' or 'percentage'
    splits: List[SplitSchema]

class ExpenseResponse(BaseModel):
    id: int
    description: str
    amount: float
    paid_by: int
    split_type: str
    splits: List[SplitSchema]
    group_id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2 replacement for orm_mode = True
