from pydantic import BaseModel

# Define Pydantic model for Todos
class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    create_date: str
    create_time: str
    update_date: str
    update_time: str
    
    # class Config:
    #     orm_mode = True

class TodoRequest(BaseModel):
    title: str
    description: str
    completed: bool