from sqlalchemy import Column, Integer, String

from database.queue_db.database import Base


class QueueIn(Base):
    __tablename__ = 'input'

    id = Column(Integer, primaryKey=True, autoincrement=True)
    telegram_id = Column(Integer, nullable=False)
    chat_id = Column(integer, nullable=False)
    data = Column(JSON, nullable=True)


    def __repr__ (self) -> str:
        return f'QueueInput [TelegramID: {self.telegram_id}, ChatID: {self.chat_id}, Data: {self.data}]'
