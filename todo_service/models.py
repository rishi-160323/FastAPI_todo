from todo_service.database import Base
from sqlalchemy import Column, Integer, Boolean, String


# Models structured to save the data in database within given format.
class Todos(Base):

    __tablename__ = 'todos'
    # Lets the code to chnage in existing table's schema.
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    title = Column(String(255))
    description = Column(String(255))
    completed = Column(Boolean, default=False)
    create_date = Column(String(255))
    create_time = Column(String(255))
    update_date = Column(String(255))
    update_time = Column(String(255))