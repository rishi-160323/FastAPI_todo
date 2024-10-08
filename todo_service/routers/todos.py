from fastapi import APIRouter, HTTPException, Depends, Path, Query
from starlette import status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from todo_service.database import SessionLocal
from todo_service.models import Todos
from todo_service import schemas


router = APIRouter(
    prefix='/todo',
    tags=['todo']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()


# Endpoint to get the list of todos.
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.TodoResponse])
def get_todos(db: Session = Depends(get_db), limit: int = Query(default=10, ge=1, le=100),
              offset: int = Query(default=0, ge=0)
):
    todos = db.query(Todos).offset(offset).limit(limit).all()
    return todos


# Endpoint to get the list of todos created on a same date. 
@router.get('/filter/{filter_by_date_created}', status_code=status.HTTP_200_OK, response_model=List[schemas.TodoResponse])
def sort_by_date_created(date_craeted_at: str, db: Session = Depends(get_db), limit: int = Query(default=10, ge=1, le=100),
              offset: int = Query(default=0, ge=0)):
    todos = db.query(Todos).filter(Todos.create_date == date_craeted_at).offset(offset).limit(limit).all()
    return todos


# Endpoint to create new todo.
@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_todo(new_todo: schemas.TodoRequest, db: Session = Depends(get_db)):
    date_time = datetime.now()
    current_date = date_time.strftime("%d-%m-%Y")
    current_time = date_time.strftime("%H:%M:%S")
    # Inside the docker model_dump() was not working so we used dict() which is depriciated.
    todo_model = Todos(**new_todo.dict(), create_date=current_date, create_time=current_time,
                        update_date=current_date, update_time=current_time)
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)  # Refresh to get the id and other fields
    return todo_model


# Endpoint to update the existing todo.
@router.put('/update/{todo_id}', status_code=status.HTTP_202_ACCEPTED)
def update_todo(new_todo: schemas.TodoRequest, db: Session = Depends(get_db), todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    date_time = datetime.now()
    todo_model.title = new_todo.title
    todo_model.description = new_todo.description
    todo_model.completed = new_todo.completed
    todo_model.update_date = date_time.strftime("%d-%m-%Y")
    todo_model.update_time = date_time.strftime("%H:%M:%S")

    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model


# Endpoint to delete the existing todo.
@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    
    todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo doesn't exist with this id")
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()



