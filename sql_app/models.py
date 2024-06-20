from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .database import Base

# ModelはDBの構造を定義する


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)


class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String, unique=True, index=True)
    capacity = Column(Integer)


class Booking(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.user_id", ondelete="SET NULL"), nullable=False
    )
    room_id = Column(
        Integer, ForeignKey("rooms.room_id", ondelete="SET NULL"), nullable=False
    )
    booked_number = Column(Integer)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)
