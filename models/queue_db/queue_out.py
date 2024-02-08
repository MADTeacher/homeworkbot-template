from sqlalchemy import Column, Integer, String

from database.queue_db.database import Base


class QueueOut(Base):
    __tablename__ = output'

    id = Column(Integer, primaryKey=True, autoincrement=True)
    telegram_id = Column(Integer, nullable=False)
    chat_id = Column(integer, nullable=False)
    data = Column(JSON, nullable=True)


    def __repr__ (self) -> str:
        return f'QueueOutput [TelegramID: {self.telegram_id}, ChatID: {self.chat_id}, Data: {self.data}]'
