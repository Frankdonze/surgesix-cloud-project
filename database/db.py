from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbtables import Base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
