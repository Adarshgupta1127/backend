from app.database import Base, engine
from app.models import user, group, expense

Base.metadata.create_all(bind=engine)
print("Database tables created successfully.")