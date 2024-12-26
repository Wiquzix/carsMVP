from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from crud import *
from schemas import CarSchema, CarUpdate,CarCreate,CommentCreate,Comment,UserCreate,UserSchema,Token
from auth import * 
from models import User
# создание ендпоинтов с приставкой для car, comment и user

router_car = APIRouter(prefix="/api/cars", tags=["Cars"])

#cars routes
@router_car.get("/", response_model=list[CarSchema]) 
def read_cars(db: Session = Depends(get_db)):
    cars = get_cars(db)
    return cars

@router_car.get("/{car_id}", response_model=CarSchema)
def read_car(car_id: int, db: Session = Depends(get_db)): # можно без аккаунта
    car = get_car(db, car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router_car.post("/", response_model=CarSchema, status_code=status.HTTP_201_CREATED)
def create_car(car: CarCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return create_car_crud(db, car.model_dump(), current_user.id)

@router_car.put("/{car_id}", response_model=CarSchema)
def update_car(car_id: int, car: CarUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    db_car = update_car_crud(db, car_id, car.model_dump(), current_user.id)
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@router_car.delete("/{car_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_car(car_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    delete_car_crud(db, car_id, current_user.id)

#Comments Routes
router_comment = APIRouter(prefix='/api/cars',tags=['Comments'])

@router_comment.get("/{car_id}/comments/", response_model=list[Comment])
def read_comments(car_id: int, db: Session = Depends(get_db)): # можно без аккаунта
    return get_comments(db, car_id)

@router_comment.post("/{car_id}/comments/", response_model=Comment, status_code=status.HTTP_201_CREATED)
def create_comment(car_id: int, comment: CommentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return create_comment_crud(db, car_id, comment.model_dump(), current_user.id)

#Users routes (Authentication)
router_user = APIRouter(prefix='/api',tags=['Users'])

@router_user.post("/token", response_model=Token) #login
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username}) #так же можно передать время "жизни" токена по умолчанию я сделал 15 минут
    return {"access_token": access_token, "token_type": "bearer"}

@router_user.post("/create_user", response_model=UserSchema) #register
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db=db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user_crud(db, user.model_dump())

