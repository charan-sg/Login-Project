from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base           #in order to define base class and map to relational database table

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    register_number = Column(Integer, primary_key=True)
    firstname = Column(String)
    middlename = Column(String)
    lastname = Column(String)
    emailid = Column(String)
    phonenumber = Column(String)
    dob = Column(Date)
    branch = Column(String)
    admission_date = Column(Date)
    bloodgroup = Column(String)
    city = Column(String)
    state = Column(String)
    addr1 = Column(String)
    addr2 = Column(String)
    zipcode = Column(String)
    gender = Column(String)

