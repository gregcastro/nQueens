from sqlalchemy.orm import sessionmaker
from settings import db_password, db_user, db_name
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey


db_string = "postgresql://"+db_user+":"+db_password+"@appdb:5432/"+db_name
try:
    db = create_engine(db_string)
except Exception as ex:
    print('Tipo: ', type(ex), '\nError: ', ex )
    db_string = "postgresql://"+db_user+":"+db_password+"@localhost:5432/"+db_name
    db = create_engine(db_string)
base = declarative_base()


class QueenCase(base):
    __tablename__ = 'queen_case'

    id = Column(Integer, primary_key=True)
    n = Column(Integer)
    number_of_solutions = Column(Integer)


class Solution(base):
    __tablename__ = 'solution'

    id = Column(Integer, primary_key=True)
    queen_case_id = Column(Integer, ForeignKey('queen_case.id'))
    solution = Column(String)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)
