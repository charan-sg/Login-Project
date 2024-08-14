from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from studentRegistermodel import Base

# Create a SQLAlchemy engine
engine = create_engine('sqlite:///students.db')

# Create the users table if it doesn't exist
Base.metadata.create_all(engine)

# Create a sessionmaker
Session = sessionmaker(bind=engine)