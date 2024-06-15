from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from loginmodel import Base

# Create a SQLAlchemy engine
engine = create_engine('sqlite:///users.db')

# Create the users table if it doesn't exist
Base.metadata.create_all(engine)

# Create a sessionmaker
Session = sessionmaker(bind=engine)
