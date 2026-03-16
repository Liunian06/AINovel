from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Novel(Base):
    __tablename__ = "novels"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    style = Column(String)
    outline = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    chapters = relationship("Chapter", back_populates="novel", cascade="all, delete-orphan")

class Chapter(Base):
    __tablename__ = "chapters"
    
    id = Column(Integer, primary_key=True, index=True)
    novel_id = Column(Integer, ForeignKey("novels.id"))
    title = Column(String, nullable=False)
    content = Column(Text)
    chapter_number = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    novel = relationship("Novel", back_populates="chapters")
