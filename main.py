from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


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


@app.get("/")
async def index():
    return {"message": "Success"}


@app.post("/users")
async def users(users: User):
    return {"users": users}


@app.post("/rooms")
async def rooms(rooms: Room):
    return {"rooms": rooms}


@app.post("/bookings")
async def bookings(bookings: Booking):
    return {"bookings": bookings}
