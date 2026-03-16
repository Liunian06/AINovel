# AI 自动写小说系统 - 前端

React + TypeScript + Vite 前端应用。

## 安装

```bash
npm install
```

## 开发

```bash
npm run dev
```

访问 http://localhost:3000

## 构建

```bash
npm run build
```

## 项目结构

```
src/
├── pages/          # 页面组件
│   ├── HomePage.tsx      # 首页（创建小说）
│   └── NovelEditor.tsx   # 编辑器页面
├── services/       # API 服务
│   └── api.ts
├── hooks/          # 自定义 Hooks
│   └── useSSE.ts         # SSE 连接 Hook
├── App.tsx         # 应用根组件
├── main.tsx        # 入口文件
└── index.css       # 全局样式
```

## 功能

- 创建小说（设置标题、题材、风格、大纲）
- 实时流式生成章节
- 查看和管理章节
- 响应式设计

## 技术栈

- React 18
- TypeScript
- Vite
- Tailwind CSS
- React Router
- Axios
- Server-Sent Events
