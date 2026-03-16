<div align="center">

# 🤖 AI Novel Generator

### *AI 驱动的自动小说创作系统*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688.svg)](https://fastapi.tiangolo.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[English](README_EN.md) | 简体中文

[快速开始](#-快速开始) • [功能特性](#-功能特性) • [技术架构](#-技术架构) • [API 文档](#-api-文档) • [贡献指南](#-贡献指南)

</div>

---

## 📖 项目简介

**AI Novel Generator** 是一个基于大语言模型的自动小说创作系统，支持 **OpenAI GPT-4**、**Anthropic Claude 3** 和 **Google Gemini Pro** 三种主流 AI 模型。通过实时流式生成技术，让用户可以即时看到章节内容的生成过程，提供流畅的创作体验。

### ✨ 为什么选择 AI Novel Generator？

- 🎯 **多模型支持** - 灵活切换 OpenAI、Anthropic、Gemini，选择最适合的 AI 引擎
- ⚡ **实时流式生成** - 基于 SSE 技术，实时展示章节生成过程
- 🎨 **现代化界面** - React + Tailwind CSS 打造的响应式 UI
- 🔧 **易于扩展** - 清晰的架构设计，轻松添加新的 AI 提供商
- 📦 **开箱即用** - 一键启动脚本，快速部署运行
- 🔒 **类型安全** - 前端 TypeScript + 后端 Pydantic 全栈类型检查

---

## 🚀 快速开始

### 方式一：一键启动（推荐）

```bash
# Windows CMD
start.bat

# Windows PowerShell
.\start.ps1
```

或直接双击 `start.bat` 文件，脚本会自动完成：
- ✅ 创建 Python 虚拟环境
- ✅ 安装所有依赖
- ✅ 启动后端服务（http://localhost:8000）
- ✅ 启动前端服务（http://localhost:3000）

### 方式二：手动启动

#### 1️⃣ 环境准备

确保已安装：
- **Node.js** 18+
- **Python** 3.10+
- **PostgreSQL** 14+

#### 2️⃣ 数据库配置

```sql
CREATE DATABASE ainovel;
CREATE USER ainovel_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE ainovel TO ainovel_user;
```

#### 3️⃣ 后端设置

```bash
cd backend

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
copy .env.example .env
# 编辑 .env 文件，填入配置
```

编辑 `.env` 文件：

```env
DATABASE_URL=postgresql://ainovel_user:your_password@localhost:5432/ainovel
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=...
DEFAULT_AI_PROVIDER=openai
```

初始化数据库并启动：

```bash
python init_db.py
python main.py
```

#### 4️⃣ 前端设置

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

访问 **http://localhost:3000** 开始使用！

---

## 🎯 功能特性

### 核心功能

| 功能 | 描述 |
|------|------|
| 🎨 **小说创作** | 设置标题、题材、风格、大纲，AI 自动生成章节内容 |
| 🔄 **实时生成** | 基于 SSE 技术，实时展示章节生成过程 |
| 🤖 **多模型支持** | 支持 OpenAI GPT-4、Anthropic Claude 3、Google Gemini Pro |
| 📚 **章节管理** | 查看、编辑、删除章节，完整的内容管理 |
| 💾 **数据持久化** | PostgreSQL 数据库存储，数据安全可靠 |
| 📱 **响应式设计** | 完美适配桌面端和移动端 |

### 技术亮点

- **AI 服务抽象层** - 统一接口设计，轻松扩展新的 AI 模型
- **SSE 实时流式** - Server-Sent Events 技术，流畅的实时体验
- **类型安全** - 前端 TypeScript + 后端 Pydantic，减少运行时错误
- **现代化技术栈** - Vite 快速构建 + FastAPI 高性能异步处理

---

## 🏗️ 技术架构

### 项目结构

```
AINovel/
├── 📁 frontend/              # React 前端应用
│   ├── src/
│   │   ├── pages/           # 页面组件
│   │   │   ├── HomePage.tsx      # 创建小说页面
│   │   │   └── NovelEditor.tsx   # 编辑器页面
│   │   ├── services/        # API 服务层
│   │   │   └── api.ts
│   │   ├── hooks/           # 自定义 Hooks
│   │   │   └── useSSE.ts         # SSE 连接 Hook
│   │   ├── App.tsx          # 路由配置
│   │   └── main.tsx         # 应用入口
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.js
│
├── 📁 backend/               # FastAPI 后端服务
│   ├── main.py              # 主应用（API 路由 + SSE）
│   ├── ai_service.py        # AI 服务抽象层
│   ├── models.py            # SQLAlchemy 数据库模型
│   ├── schemas.py           # Pydantic 数据验证
│   ├── database.py          # 数据库连接配置
│   ├── config.py            # 配置管理
│   ├── init_db.py           # 数据库初始化
│   └── requirements.txt
│
├── start.bat                # Windows 一键启动脚本
├── start.ps1                # PowerShell 启动脚本
├── LICENSE                  # MIT 许可证
└── README.md
```

### 技术栈

#### 前端
- **框架**: React 18 + TypeScript
- **构建工具**: Vite
- **样式**: Tailwind CSS
- **路由**: React Router v6
- **HTTP 客户端**: Axios
- **实时通信**: Server-Sent Events (SSE)

#### 后端
- **框架**: FastAPI
- **数据库**: PostgreSQL + SQLAlchemy
- **数据验证**: Pydantic
- **AI 集成**: OpenAI API、Anthropic API、Google Gemini API
- **实时通信**: SSE-Starlette

### 架构图

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  HomePage    │  │ NovelEditor  │  │   useSSE     │     │
│  │  (创建小说)   │  │  (编辑器)     │  │   (SSE Hook) │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│           │                │                  │             │
│           └────────────────┴──────────────────┘             │
│                            │                                │
│                    ┌───────▼────────┐                       │
│                    │   API Service   │                       │
│                    └───────┬────────┘                       │
└────────────────────────────┼──────────────────────────────┘
                             │ HTTP/SSE
┌────────────────────────────┼──────────────────────────────┐
│                    ┌───────▼────────┐                       │
│                    │   FastAPI      │                       │
│                    │   (main.py)    │                       │
│                    └───────┬────────┘                       │
│                            │                                │
│         ┌──────────────────┼──────────────────┐            │
│         │                  │                  │            │
│  ┌──────▼──────┐  ┌────────▼────────┐  ┌─────▼─────┐     │
│  │  Database   │  │   AI Service    │  │    SSE    │     │
│  │ (PostgreSQL)│  │  (抽象层)        │  │  (实时流)  │     │
│  └─────────────┘  └────────┬────────┘  └───────────┘     │
│                            │                               │
│              ┌─────────────┼─────────────┐                │
│              │             │             │                │
│       ┌──────▼──────┐ ┌────▼────┐ ┌─────▼─────┐          │
│       │   OpenAI    │ │Anthropic│ │  Gemini   │          │
│       │   GPT-4     │ │ Claude  │ │   Pro     │          │
│       └─────────────┘ └─────────┘ └───────────┘          │
│                         Backend                            │
└─────────────────────────────────────────────────────────────┘
```

---

## 📡 API 文档

### RESTful API 端点

| 方法 | 端点 | 描述 |
|------|------|------|
| `POST` | `/api/novels` | 创建新小说 |
| `GET` | `/api/novels` | 获取所有小说列表 |
| `GET` | `/api/novels/{id}` | 获取指定小说详情 |
| `GET` | `/api/novels/{id}/generate` | SSE 流式生成章节 |
| `POST` | `/api/novels/{id}/generate` | 触发章节生成 |
| `DELETE` | `/api/novels/{id}` | 删除指定小说 |

### 示例：创建小说

```bash
curl -X POST http://localhost:8000/api/novels \
  -H "Content-Type: application/json" \
  -d '{
    "title": "星际穿越之旅",
    "genre": "scifi",
    "style": "硬科幻",
    "outline": "一个关于人类探索未知星系的故事..."
  }'
```

### 示例：SSE 流式生成

```javascript
const eventSource = new EventSource('http://localhost:8000/api/novels/1/generate');

eventSource.onmessage = (event) => {
  console.log('收到数据:', event.data);
  if (event.data === '[DONE]') {
    eventSource.close();
  }
};
```

完整 API 文档：启动后端后访问 **http://localhost:8000/docs**

---

## 🔧 配置说明

### AI 提供商配置

在 `backend/.env` 中配置：

#### OpenAI
```env
DEFAULT_AI_PROVIDER=openai
OPENAI_API_KEY=sk-...
```

#### Anthropic Claude
```env
DEFAULT_AI_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-...
```

#### Google Gemini
```env
DEFAULT_AI_PROVIDER=gemini
GEMINI_API_KEY=...
```

### 自定义提示词

编辑 `backend/ai_service.py` 中的 `generate_chapter` 方法：

```python
prompt = f"""请为以下小说生成第{chapter_num}章内容：

标题：{novel_info['title']}
题材：{novel_info['genre']}
风格：{novel_info.get('style', '自然流畅')}
大纲：{novel_info['outline']}

要求：
1. 章节长度约2000-3000字
2. 情节连贯，符合大纲设定
3. 语言生动，符合指定风格
"""
```

---

## 🛠️ 开发指南

### 添加新的 AI 提供商

1. 在 `backend/ai_service.py` 中创建新的 Provider 类：

```python
class NewAIProvider(AIProvider):
    def __init__(self):
        self.client = NewAIClient(api_key=settings.new_ai_api_key)
    
    async def generate_stream(self, prompt: str) -> AsyncGenerator[str, None]:
        # 实现流式生成逻辑
        async for chunk in self.client.stream(prompt):
            yield chunk
```

2. 在 `AIService.__init__` 中注册：

```python
if provider == "new_ai":
    self.provider = NewAIProvider()
```

### 运行测试

```bash
# 后端测试
cd backend
pytest

# 前端测试
cd frontend
npm test
```

### 构建生产版本

```bash
# 前端构建
cd frontend
npm run build

# 后端部署
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！无论是新功能、Bug 修复、文档改进还是问题反馈。

### 如何贡献

1. **Fork** 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 **Pull Request**

### 开发规范

- 遵循现有代码风格
- 添加必要的注释和文档
- 确保所有测试通过
- 更新相关文档

---

## 📝 路线图

- [ ] 章节编辑功能
- [ ] 小说导出（TXT/EPUB/PDF）
- [ ] 用户认证系统
- [ ] 生成历史记录
- [ ] 自定义提示词模板
- [ ] 批量章节生成
- [ ] 多语言支持
- [ ] Docker 容器化部署
- [ ] 云端部署方案

---

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议。

---

## 🙏 致谢

感谢以下开源项目：

- [FastAPI](https://fastapi.tiangolo.com/) - 现代化的 Python Web 框架
- [React](https://reactjs.org/) - 用户界面库
- [Tailwind CSS](https://tailwindcss.com/) - CSS 框架
- [OpenAI](https://openai.com/) - GPT 模型
- [Anthropic](https://www.anthropic.com/) - Claude 模型
- [Google AI](https://ai.google/) - Gemini 模型

---

## 📧 联系方式

- **GitHub Issues**: [提交问题](https://github.com/Liunian06/AINovel/issues)
- **Pull Requests**: [贡献代码](https://github.com/Liunian06/AINovel/pulls)

---

<div align="center">

**如果这个项目对你有帮助，请给一个 ⭐️ Star！**

Made with ❤️ by [Liunian06](https://github.com/Liunian06)

</div>
