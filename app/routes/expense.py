

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.expense import ExpenseCreate, ExpenseResponse
from app.models.expense import Expense
from app.database import get_db

router = APIRouter()

@router.post("/expenses", response_model=ExpenseResponse)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(
        amount=expense.amount,
        description=expense.description,
        group_id=expense.group_id,
        paid_by=expense.paid_by
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense
