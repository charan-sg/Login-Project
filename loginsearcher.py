from fetchlogindb import Session
from loginmodel import User

def authenticate_user(userid, password):
    session = Session()
    try:
        user = session.query(User).filter_by(userid=userid, password=password).first()
        return user is not None
    finally:
        session.close()
