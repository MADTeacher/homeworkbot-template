from sqlalchemy import Column, ForeignKey, Float, JSON, Integer

from database.main_db.database import Base


class AssignedDiscipline(Base):
    __tablename__ = 'assigned_disciplines'
 
    id = Column(Integer, primary_key=True, autoincrement=True)
    discipline_id = Column(Integer, ForeignKey('disciplines.id'), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    point = Column(Float, defaul=0)
    homework = Column(JSON, nullable=False)

    def __repr__ (self) -> str:
        info = f'AssignedDiscipline [DisciplineID: {self.discipline_id}, '
        info += f'StudentID: {self.student_id}, Point: {self.point}, '
        info += f'Homework: {self.homework}]'
        return info
