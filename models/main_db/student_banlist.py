from sqlalchemy import Column, Integer

from database.main_db.database import Base


class StudentBanList(Base):
    __tablename__ = 'studentbanlist'

    telegram_id = Column(Integer, primary_key=True)

    def __repr__(self) -> str:
        return f'Student [ID: {self.telegram_id}]'
    