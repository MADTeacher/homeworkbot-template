from sqlalchemy import Boolean,Column, Integer
from database.main_db.database import Base


class Admin(Base):
    __tablename__ = 'admins'

    telegram_id = Column(Integer, primary_key=True)
    teacher_mode = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f'Admin [ID: {self.telegram_id}, Mode: {self.teacher_mode}'
    