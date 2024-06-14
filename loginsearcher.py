from sqlalchemy.orm import sessionmaker
from loginmodel import User
from sqlalchemy import create_engine

# create a SQLAlchemy engine
engine = create_engine('sqlite:///users.db')

# create a sessionmaker
Session = sessionmaker(bind=engine)

def authenticate_user(userid, password):
    """
    Check weather the userid and Password is correct
    """
    session = Session()
    try:
        user = session.query(User).filter_by(userid=userid, password=password).first()
        return user is not None
    finally:
        session.close()
