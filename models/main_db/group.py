from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey

from database.main_db.database import Base


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String, nullable=False, unique=True)


    def __repr__ (self) -> str:
        return f'Student [ID: {self.id}, Name: {self.group_name}]'
    

@dataclass
class TeacherRaw:
    full_name: str
