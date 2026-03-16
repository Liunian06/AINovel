"""
数据库初始化脚本
运行此脚本以创建所有数据库表
"""
from database import engine, Base
from models import Novel, Chapter

def init_db():
    print("正在创建数据库表...")
    Base.metadata.create_all(bind=engine)
    print("数据库表创建完成！")

if __name__ == "__main__":
    init_db()
