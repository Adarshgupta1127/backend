from fastapi import FastAPI
from app.routes import group, expense, user  # ✅ Import the new user router

app = FastAPI(
    title="Splitwise Clone API",
    version="1.0.0"
)

# ✅ Include all routes under /api
app.include_router(user.router, prefix="/api", tags=["User"])
app.include_router(group.router, prefix="/api", tags=["Group"])
app.include_router(expense.router, prefix="/api", tags=["Expense"])

@app.get("/")
def root():
    return {"message": "Welcome to Splitwise Clone Backend"}
