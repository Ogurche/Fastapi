from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, Date, BigInteger, DateTime, SmallInteger
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData
from config import Base
from config import engine

metadata = MetaData()

class User (Base):
    