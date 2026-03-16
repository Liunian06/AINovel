from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sse_starlette.sse import EventSourceResponse
import asyncio

from database import get_db, engine, Base
from models import Novel as NovelModel, Chapter as ChapterModel
from schemas import Novel, NovelCreate, Chapter
from ai_service import AIService

app = FastAPI(title="AI Novel Generator API")

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 创建数据库表
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "AI Novel Generator API"}

@app.post("/api/novels", response_model=Novel)
def create_novel(novel: NovelCreate, db: Session = Depends(get_db)):
    db_novel = NovelModel(**novel.model_dump())
    db.add(db_novel)
    db.commit()
    db.refresh(db_novel)
    return db_novel

@app.get("/api/novels/{novel_id}", response_model=Novel)
def get_novel(novel_id: int, db: Session = Depends(get_db)):
    novel = db.query(NovelModel).filter(NovelModel.id == novel_id).first()
    if not novel:
        raise HTTPException(status_code=404, detail="Novel not found")
    return novel

@app.get("/api/novels", response_model=list[Novel])
def list_novels(db: Session = Depends(get_db)):
    return db.query(NovelModel).all()

@app.get("/api/novels/{novel_id}/generate")
async def generate_chapter_stream(novel_id: int, db: Session = Depends(get_db)):
    novel = db.query(NovelModel).filter(NovelModel.id == novel_id).first()
    if not novel:
        raise HTTPException(status_code=404, detail="Novel not found")
    
    chapter_count = len(novel.chapters)
    chapter_num = chapter_count + 1
    
    novel_info = {
        "title": novel.title,
        "genre": novel.genre,
        "style": novel.style,
        "outline": novel.outline
    }
    
    ai_service = AIService()
    
    async def event_generator():
        full_content = ""
        try:
            async for chunk in ai_service.generate_chapter(novel_info, chapter_num):
                full_content += chunk
                yield {"data": chunk}
                await asyncio.sleep(0.01)
            
            # 生成完成后保存章节
            new_chapter = ChapterModel(
                novel_id=novel_id,
                title=f"第{chapter_num}章",
                content=full_content,
                chapter_number=chapter_num
            )
            db.add(new_chapter)
            db.commit()
            
            yield {"data": "[DONE]"}
        except Exception as e:
            yield {"data": f"[ERROR]: {str(e)}"}
    
    return EventSourceResponse(event_generator())

@app.post("/api/novels/{novel_id}/generate")
async def generate_chapter(novel_id: int, db: Session = Depends(get_db)):
    novel = db.query(NovelModel).filter(NovelModel.id == novel_id).first()
    if not novel:
        raise HTTPException(status_code=404, detail="Novel not found")
    
    return {"status": "generating", "message": "Chapter generation started"}

@app.delete("/api/novels/{novel_id}")
def delete_novel(novel_id: int, db: Session = Depends(get_db)):
    novel = db.query(NovelModel).filter(NovelModel.id == novel_id).first()
    if not novel:
        raise HTTPException(status_code=404, detail="Novel not found")
    
    db.delete(novel)
    db.commit()
    return {"message": "Novel deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
