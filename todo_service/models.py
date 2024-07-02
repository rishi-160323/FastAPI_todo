from database import Base
from sqlalchemy import Column, Integer, Boolean, String


class Todos(Base):

    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    title = Column(String(255))
    description = Column(String(255))
    completed = Column(Boolean, default=False)
    create_date = Column(String(255))
    create_time = Column(String(255))
    update_date = Column(String(255))
    update_time = Column(String(255))