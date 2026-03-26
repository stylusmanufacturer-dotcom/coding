from fastapi import FastAPI, Request

from routers import user, expense

from database import Base, engine
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/")
def test(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
app.include_router(user.router)
app.include_router(expense.router)
