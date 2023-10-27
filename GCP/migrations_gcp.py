from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

GCP_URL = os.getenv("GCP_URL")

Base = declarative_base()

class Doctor(Base):
    __tablename__ = 'doctor'
    id = Column(Integer, primary_key=True)
    NPI = Column(String(50), nullable=False)
    department = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    
conn_string = (f"{GCP_URL}")
engine = create_engine(conn_string)

inspector = inspect(engine)
inspector.get_table_names()

Base.metadata.create_all(engine)