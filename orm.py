from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey


db_string = "postgres://postgres:123456@localhost/nqueens"

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