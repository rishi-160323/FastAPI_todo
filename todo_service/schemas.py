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
    
    # orm_mode is needed to enabled  the from_orm method in order to create a model instance by
    #  reading attributes from another class instance.
    class Config:
        orm_mode = True

class TodoRequest(BaseModel):
    title: str
    description: str
    completed: bool