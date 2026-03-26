from fastapi import FastAPI

from routers import user, expense

from database import Base, engine


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(expense.router)
