from models import User, Expense
from auth import hashed_password
def fetch_by_email(db, email):
    return db.query(User).filter(User.email == email).first()
def create_user(db, email: str, password: str):
    user = User(email=email, password=hashed_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
def create_expense(db, email: str):
    email = fetch_by_email(db, email)
    expense = Expense(title=email.title, description=email.description, amount=email.amount, category=email.category, user=email.user)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

