# import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# DATABASE_URL = 'mysql+mysqlconnector://root:nsx%40123@localhost/Task_Todo'
DATABASE_URL = 'mysql+mysqlconnector://root:nsx%40123@localhost/Task_Todo2'
# DATABASE_URL = "mysql+mysqlconnector://temp_user:nsx%40123@db:3307/test_todo_db"


# DATABASE_URL= 'mysql+pymysql://MYSQL_ROOT_PASSWORD:nsx%40123@db:3306/test_todo_db'
# DATABASE_URL="mysql+pymysql://temp_user:nsx%40123@db:3307/test_todo_db"

# DATABASE_URL = "sqlite:///./test.db"

# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")

# # DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# DATABASE_URL = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8'


# create_engine() is the central object of sqlalchemy library.
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class for handling database sessions.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create a base class for your data models.
# Base = declarative_base()
Base = declarative_base()

# Function to get a database session which opens as request comes and get closed as request gets fulfilled.
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as ex:
        import traceback
        traceback.print_exc
        print("\nError At : ", str(ex))
    finally:
        db.close()