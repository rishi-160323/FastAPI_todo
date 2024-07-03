from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Main database for performing operation and store data
# DATABASE_URL = 'mysql+mysqlconnector://root:nsx%40123@localhost/Task_Todo'

# Separate database for unit tests.
DATABASE_URL = 'mysql+mysqlconnector://root:nsx%40123@localhost/Task_Todo2'

engine = create_engine(DATABASE_URL)

# Create a SessionLocal class for handling database sessions.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for your data models.
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