from sqlalchemy import Column, ForeignKey, Integer

from database.main_db.database import Base


class TeacherGroup(Base):
    __tablename__ = 'teacher_group'
 
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)


    def __repr__ (self) -> str:
        return f'TeacherGroup [GroupID: {self.group_id}, TeacherID: {self.teacher_id}]'
