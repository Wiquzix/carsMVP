import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):  
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String) 
    cars = relationship("Car", backref="owner")


class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))
    comments = relationship("Comment", backref="car")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    car_id = Column(Integer, ForeignKey("cars.id"))
    author_id = Column(Integer, ForeignKey("users.id"))


engine = create_engine("sqlite:///./main.db")

Base.metadata.create_all(bind=engine)

