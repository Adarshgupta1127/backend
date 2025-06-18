from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.group import Group, group_user
from app.models.user import User
from app.schemas.group import GroupCreate

router = APIRouter()

@router.post("/groups")
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    db_group = Group(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)

    for user_id in group.user_ids:
        user = db.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail=f"User {user_id} not found")
        db.execute(group_user.insert().values(group_id=db_group.id, user_id=user_id))

    db.commit()
    return {"id": db_group.id, "name": db_group.name, "user_ids": group.user_ids}
