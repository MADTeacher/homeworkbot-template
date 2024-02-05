import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()

engine = create_engine(f'sqllite:///{os.getenv("DATABASE_NAME")}.sqlite')
Session = sessionmaker(bind=engine)

Base = declarative_base()


def create_db() -> None:
    Base.metadata.create_all(engine)
