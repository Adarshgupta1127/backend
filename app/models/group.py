from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.user import User

# Association table for many-to-many
group_user = Table(
    "group_user", Base.metadata,
    Column("group_id", ForeignKey("groups.id")),
    Column("user_id", ForeignKey("users.id"))
)

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    users = relationship("User", secondary=group_user)
