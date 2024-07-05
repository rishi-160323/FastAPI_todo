from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

# engine is a comman interface between database and application to interact.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# Create a SessionLocal class for handling database sessions.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for your data models.
Base = declarative_base()

# Function to open db as session starts then close as end.
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
