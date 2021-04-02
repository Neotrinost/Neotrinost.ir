from sqlalchemy.util.langhelpers import string_or_unprintable
from main import db
from sqlalchemy import Column, Integer, String


#create User table in our database
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key = True)
    username = Column(String(320), nullable = False, unique = True)
    email = Column(String(128), nullable = False, unique = True)
    password = Column(String(128), nullable = False, unique = False)
    role = Column(Integer(), nullable = False, default = 0)


