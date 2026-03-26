from pydantic import BaseModel

class Create_User(BaseModel):
    username: str
    password: str
    email: str
class Create_Expense(BaseModel):
    title: str
    description: str
    amount: int
    category: str