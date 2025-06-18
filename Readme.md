# Splitwise Clone – Backend

This is a simplified Splitwise Clone backend built using **FastAPI** and **PostgreSQL** for the Neurix Full-Stack SDE Intern Assignment.

##  Features

- Group creation and member assignment
- Adding expenses with equal or percentage split
- Tracking balances within a group
- User-wise balance summaries

##  Tech Stack

- **FastAPI** – Modern Python API framework
- **SQLAlchemy** – ORM for database interaction
- **PostgreSQL** – Relational database

##  Folder Structure


## API Endpoints

### Group Management
- `POST /api/groups` – Create a new group
- `GET /api/groups/{group_id}` – Get group details (name, users, total expenses)

### Expense Management
- `POST /api/groups/{group_id}/expenses` – Add a new expense to a group

### Balance Tracking
- `GET /api/groups/{group_id}/balances` – See group-wise balances
- `GET /api/users/{user_id}/balances` – See user's balances across groups

