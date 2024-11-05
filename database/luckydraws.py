from .core import Base

from sqlalchemy import Column, BOOLEAN, Enum
from sqlalchemy.dialects.mysql import VARCHAR, BIGINT, DATETIME
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql import func
import enum

class SchoolEnum(enum.Enum):
    HANSEI = "한세사이버보안고등학교"
    SEMYEONG = "세명컴퓨터고등학교"

class Luckydraws(Base):
    __tablename__ = "esports_luckydraws"
    __table_args__ = {"mysql_charset": "utf8mb4"}
    
    id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    userSchool = Column(Enum(SchoolEnum, native_enum=False), nullable=False)
    userStudentNumber = Column(VARCHAR(10), nullable=False)
    userName = Column(VARCHAR(10), nullable=False)
    isWinner = Column(BOOLEAN, default=False) 
    
    drawFieldId = Column(BIGINT(unsigned=True), ForeignKey('esports_draw_field.id'), nullable=False)
    drawField = relationship("DrawField", back_populates="luckydraws")