from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://sit722part3_ej22_user:MfKbzju6x8WwCEFSPtm3u1VLALLS8Cjh@dpg-crok5723esus73c2ajog-a.oregon-postgres.render.com/sit722part3_ej22" 

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
