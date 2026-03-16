import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { generateChapter, getNovel } from '../services/api'
import { useSSE } from '../hooks/useSSE'

interface Novel {
  id: string
  title: string
  chapters: Chapter[]
}

interface Chapter {
  id: string
  title: string
  content: string
}

export default function NovelEditor() {
  const { id } = useParams()
  const [novel, setNovel] = useState<Novel | null>(null)
  const [generating, setGenerating] = useState(false)
  const [streamContent, setStreamContent] = useState('')
  
  const { connect, disconnect } = useSSE((data) => {
    setStreamContent(prev => prev + data)
  })

  useEffect(() => {
    if (id) {
      loadNovel(id)
    }
  }, [id])

  const loadNovel = async (novelId: string) => {
    try {
      const data = await getNovel(novelId)
      setNovel(data)
    } catch (error) {
      console.error('加载小说失败:', error)
    }
  }

  const handleGenerate = async () => {
    if (!id) return
    
    setGenerating(true)
    setStreamContent('')
    
    try {
      connect(`/api/novels/${id}/generate`)
      await generateChapter(id)
    } catch (error) {
      console.error('生成章节失败:', error)
    } finally {
      setGenerating(false)
      disconnect()
      if (id) loadNovel(id)
    }
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-4xl mx-auto py-8 px-4">
        <div className="bg-white rounded-lg shadow-md p-6">
          <h1 className="text-3xl font-bold mb-6">{novel?.title || '加载中...'}</h1>
          
          <button
            onClick={handleGenerate}
            disabled={generating}
            className="mb-6 px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 disabled:bg-gray-400"
          >
            {generating ? '生成中...' : '生成新章节'}
          </button>

          {streamContent && (
            <div className="mb-6 p-4 bg-blue-50 rounded-md">
              <h3 className="font-semibold mb-2">实时生成:</h3>
              <p className="whitespace-pre-wrap">{streamContent}</p>
            </div>
          )}

          <div className="space-y-6">
            {novel?.chapters.map((chapter) => (
              <div key={chapter.id} className="border-b pb-4">
                <h2 className="text-xl font-semibold mb-2">{chapter.title}</h2>
                <p className="text-gray-700 whitespace-pre-wrap">{chapter.content}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
