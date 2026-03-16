from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ChapterBase(BaseModel):
    title: str
    content: str
    chapter_number: int

class ChapterCreate(ChapterBase):
    novel_id: int

class Chapter(ChapterBase):
    id: int
    novel_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class NovelBase(BaseModel):
    title: str
    genre: str
    style: Optional[str] = None
    outline: str

class NovelCreate(NovelBase):
    pass

class Novel(NovelBase):
    id: int
    created_at: datetime
    chapters: List[Chapter] = []
    
    class Config:
        from_attributes = True
