import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json'
  }
})

export const createNovel = async (data: any) => {
  const response = await api.post('/novels', data)
  return response.data
}

export const getNovel = async (id: string) => {
  const response = await api.get(`/novels/${id}`)
  return response.data
}

export const generateChapter = async (novelId: string) => {
  const response = await api.post(`/novels/${novelId}/generate`)
  return response.data
}

export default api
