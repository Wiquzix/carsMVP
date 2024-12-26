from sqlalchemy.orm import Session
from models import Car, Comment, User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_cars(db: Session):
    return db.query(Car).all()

def get_car(db: Session, car_id: int):
    return db.query(Car).filter(Car.id == car_id).first()

def create_car_crud(db: Session, car: dict, user_id: int):
    db_car = Car(**car, owner_id=user_id)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def update_car_crud(db: Session, car_id: int, car: dict, user_id: int):
    db_car = db.query(Car).filter(Car.id == car_id, Car.owner_id == user_id).first()
    if db_car:
        for key, value in car.items():
            if value is not None:
                setattr(db_car, key, value)
        db.commit()
        db.refresh(db_car)
    return db_car


def delete_car_crud(db: Session, car_id: int, user_id: int):
    db_car = db.query(Car).filter(Car.id == car_id, Car.owner_id == user_id).first()
    if db_car:
        db.delete(db_car)
        db.commit()


def get_comments(db: Session, car_id: int):
    return db.query(Comment).filter(Comment.car_id == car_id).all()


def create_comment_crud(db: Session, car_id: int, comment: dict, user_id: int):
    db_comment = Comment(**comment, car_id=car_id, author_id=user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user_crud(db: Session, user: dict):
    hashed_password = pwd_context.hash(user["password"])
    db_user = User(username=user["username"], password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

