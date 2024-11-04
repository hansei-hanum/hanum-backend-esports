from .core import Base

from sqlalchemy import Column, BOOLEAN
from sqlalchemy.dialects.mysql import VARCHAR, BIGINT, DATETIME
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql import func


class DrawField(Base):
    __tablename__ = "draw_field"
    __table_args__ = {"mysql_charset": "utf8mb4"}
    
    id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    vote = Column(BIGINT(unsigned=True))  
    isActive = Column(BOOLEAN, default=False)
    
    luckydraws = relationship("Luckydraws", back_populates="drawField", uselist=False)
