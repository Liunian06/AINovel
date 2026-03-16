# AI 自动写小说系统 - 后端

FastAPI 后端服务，提供小说生成 API 和 AI 集成。

## 安装

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 安装依赖
pip install -r requirements.txt
```

## 配置

复制 `.env.example` 为 `.env` 并填入配置：

```env
DATABASE_URL=postgresql://user:password@localhost:5432/ainovel
OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
GEMINI_API_KEY=your_key
DEFAULT_AI_PROVIDER=openai
```

## 初始化数据库

```bash
python init_db.py
```

## 运行

```bash
# 开发模式
python main.py

# 或使用 uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API 文档

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 项目结构

- `main.py` - FastAPI 应用主文件
- `models.py` - SQLAlchemy 数据库模型
- `schemas.py` - Pydantic 数据验证模式
- `database.py` - 数据库连接配置
- `config.py` - 应用配置
- `ai_service.py` - AI 服务抽象层
- `init_db.py` - 数据库初始化脚本
