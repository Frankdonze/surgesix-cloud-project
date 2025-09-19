from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Boolean

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

class Games(Base):
    __tablename__ = "games"
    
    id = Column(Integer, primary_key=True)
    game = Column(String(60))
    season = Column(String(4))
    team1 = Column(String(30))
    team2 = Column(String(30))
    finalscore1 = Column(Integer)
    finalscore2 = Column(Integer)
    date = Column(Date) 
