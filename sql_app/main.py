from typing import List
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 許可するオリジンを指定
origins = [
    "http://localhost:3000",
]

# CORSミドルウェアを追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/")
# async def index():
#     return {"message": "Success"}


# Read
@app.get(
    "/users", response_model=List[schemas.User]
)  # response_modelを指定することで、レスポンスのJSONの形式を指定できる
async def read_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):  # ユーザー一覧を取得するエンドポイント
    users = crud.get_user(
        db=db, skip=skip, limit=limit
    )  # get_user関数を呼び出し、ユーザー一覧を取得
    return users


@app.get("/rooms", response_model=List[schemas.Room])
async def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = crud.get_room(db=db, skip=skip, limit=limit)
    return rooms


@app.get("/bookings", response_model=List[schemas.Booking])
async def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = crud.get_booking(db=db, skip=skip, limit=limit)
    return bookings


# Create
@app.post("/users", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.post("/rooms", response_model=schemas.Room)
async def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    return crud.create_room(db=db, room=room)


@app.post("/bookings", response_model=schemas.Booking)
async def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.create_booking(db=db, booking=booking)
