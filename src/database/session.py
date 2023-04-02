from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sqlite.db', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Subscriber(Base):
    __tablename__ = 'subscribers'

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
    occupation = Column(String)
    description = Column(String)
    date_of_birth = Column(String)
    created_at = Column(String)


Base.metadata.create_all(engine)
