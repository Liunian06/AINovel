import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { createNovel } from '../services/api'

export default function HomePage() {
  const navigate = useNavigate()
  const [formData, setFormData] = useState({
    title: '',
    genre: '',
    style: '',
    outline: ''
  })

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      const novel = await createNovel(formData)
      navigate(`/editor/${novel.id}`)
    } catch (error) {
      console.error('创建小说失败:', error)
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-8">AI 自动写小说系统</h1>
        
        <form onSubmit={handleSubmit} className="bg-white rounded-lg shadow-md p-6 space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2">小说标题</label>
            <input
              type="text"
              value={formData.title}
              onChange={(e) => setFormData({...formData, title: e.target.value})}
              className="w-full px-3 py-2 border rounded-md"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-2">题材类型</label>
            <select
              value={formData.genre}
              onChange={(e) => setFormData({...formData, genre: e.target.value})}
              className="w-full px-3 py-2 border rounded-md"
              required
            >
              <option value="">请选择</option>
              <option value="fantasy">玄幻</option>
              <option value="romance">言情</option>
              <option value="scifi">科幻</option>
              <option value="mystery">悬疑</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium mb-2">写作风格</label>
            <input
              type="text"
              value={formData.style}
              onChange={(e) => setFormData({...formData, style: e.target.value})}
              className="w-full px-3 py-2 border rounded-md"
              placeholder="例如：轻松幽默、严肃深沉"
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-2">故事大纲</label>
            <textarea
              value={formData.outline}
              onChange={(e) => setFormData({...formData, outline: e.target.value})}
              className="w-full px-3 py-2 border rounded-md h-32"
              placeholder="简要描述故事情节..."
              required
            />
          </div>

          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700"
          >
            开始创作
          </button>
        </form>
      </div>
    </div>
  )
}
