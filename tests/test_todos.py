import pytest

from todo_service.main import app
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from todo_service.database import Base, get_db
from todo_service.models import Todos

SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:nsx%40123@localhost/Task_Todo2'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# # Dependency override
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture
def test_db():
    # Create test data
    db = TestingSessionLocal()
    # Adding multiple todos for testing
    todos = [
        Todos(title="Test Todo 1", description="Description 1", completed=False,
                     create_date="01-01-2021", create_time="00:00:00", update_date="01-01-2021", update_time="00:00:00"),
        Todos(title="Test Todo 2", description="Description 2", completed=False,
                     create_date="01-01-2021", create_time="00:00:00", update_date="01-01-2021", update_time="00:00:00"),
        Todos(title="Test Todo 3", description="Description 3", completed=False,
                     create_date="01-01-2021", create_time="00:00:00", update_date="01-01-2021", update_time="00:00:00")
    ]
    db.add_all(todos)
    db.commit()
    yield db
    db.close()

def test_get_todos(test_db):
    response = client.get("/")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3  # We added 3 todos
    
    # Check the structure of the first todo
    todo = data[0]
    assert "title" in todo
    assert "description" in todo
    assert "completed" in todo
    assert "create_date" in todo
    assert "create_time" in todo
    assert "update_date" in todo
    assert "update_time" in todo

def test_get_todos_with_limit():
    response = client.get("/?limit=2")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2  # Limit is set to 2

def test_get_todos_with_offset():
    response = client.get("/?offset=1")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2  # Offset is set to 1, so we should get 2 todos

def test_get_todos_with_limit_and_offset():
    response = client.get("/?limit=1&offset=1")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1  # Limit is set to 1 and offset is set to 1
    assert data[0]["title"] == "Test Todo 2" # The second todo should be returned


def test_create_todo():
    new_todo = {
        "title": "Test Todo",
        "description": "Test Description",
        "completed": False
    }
    
    response = client.post("/create", json=new_todo)
    assert response.status_code == 201
    
    data = response.json()
    assert data["title"] == new_todo["title"]
    assert data["description"] == new_todo["description"]
    assert data["completed"] == new_todo["completed"]
    assert "create_date" in data
    assert "create_time" in data
    assert "update_date" in data
    assert "update_time" in data



def test_sort_by_date_created():
    date  = "01-01-2021"
    response = client.get(f"/filter/%7Bfilter_by_date_created%7D?date_craeted_at={date}")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    # assert len(data) == 1  # We added 3 todos, filtering by '29-06-2024' should return 1 todo
    
    # Check the structure of the returned todo
    todo = data[0]
    assert todo["create_date"] == date
    # assert todo["title"] == "Test Todo 2"  # Check if the correct todo is returned




def test_update_todo_success(test_db):

    # Updated todo data
    updated_todo_data = {
        "title": "Updated Title",
        "description": "Updated Description",
        "completed": True
    }
    todo_id = 1
    response = client.put(f"/update/{todo_id}", json=updated_todo_data)
    assert response.status_code == 202
    
    # Check response JSON data
    updated_todo = response.json()
    assert updated_todo["title"] == updated_todo_data["title"]
    assert updated_todo["description"] == updated_todo_data["description"]
    assert updated_todo["completed"] == updated_todo_data["completed"]
    
    # Check database changes
    updated_todo_in_db = test_db.query(Todos).filter(Todos.id == todo_id).first()
    assert updated_todo_in_db.title == updated_todo_data["title"]
    assert updated_todo_in_db.description == updated_todo_data["description"]
    assert updated_todo_in_db.completed == updated_todo_data["completed"]


def test_delete_todo_success(test_db):
    response = client.delete(f"/delete?todo_id=1")
    assert response.status_code == 204
    # Check response content
    assert response.content == b''


def test_find_delete_todo(test_db):
    deleted_todo = test_db.get(Todos, 1)
    print(deleted_todo)
    assert deleted_todo is None