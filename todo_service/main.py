from fastapi import FastAPI
from todo_service.database import engine
from todo_service import models
from todo_service.routers import todos

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todos.router)