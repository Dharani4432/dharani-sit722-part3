from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://dharani722w7_user:RaOLEb1BZrCeFLgknSxKfKX8DeOERxWs@dpg-crnk5el6l47c73ahk390-a.oregon-postgres.render.com/dharani722w7" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
