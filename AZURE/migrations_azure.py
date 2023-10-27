from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

AZURE_URL = os.getenv("AZURE_URL")

Base = declarative_base()

class Doctor(Base):
    __tablename__ = 'doctor'
    id = Column(Integer, primary_key=True)
    MRN = Column(String(50), nullable=False)
    specialty = Column(String(50), nullable=False)
    
    records = relationship('DoctorDemographic', back_populates='doctor')

class DoctorDemographic(Base):
    __tablename__ = 'doctor_demographics'
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctor.id'))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    doctor = relationship('Doctor', back_populates='records')

conn_string = (f"{AZURE_URL}")
engine = create_engine(conn_string)

inspector = inspect(engine)
inspector.get_table_names()

Base.metadata.create_all(engine)