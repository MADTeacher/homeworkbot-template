from dataclasses import dataclass
from sqlalchemy import Column, Integer, String

from database.main_db.database import Base


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    telegram_id = Column(Integer, nullable=True, unique=True)


    def __repr__ (self) -> str:
        return f'Student [ID: {self.id}, Full_name: {self.full_name}, '\
               f'TelegramID: {self.telegram_id}]'
    

@dataclass
class TeacherRaw:
    full_name: str
