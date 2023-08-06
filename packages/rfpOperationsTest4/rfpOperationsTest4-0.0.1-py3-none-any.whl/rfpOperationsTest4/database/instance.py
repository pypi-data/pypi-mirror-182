from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

connection_url = "postgresql://postgres:postgres@localhost:5432"

engine = create_engine(connection_url, echo=True)

Session = sessionmaker()


class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer(), primary_key=True)
    price = Column(Integer())
    beds = Column(Integer())
    baths = Column(Integer())
    liv_rooms = Column(Integer())
    address = Column(String(255))


class Feature(Base):
    __tablename__ = "hashed_features"
    id = Column(Integer(), primary_key=True)
    prev_hash = Column(String(255))
    hash = Column(String(255))
