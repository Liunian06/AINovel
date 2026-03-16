import { BrowserRouter, Routes, Route } from 'react-router-dom'
import HomePage from './pages/HomePage'
import NovelEditor from './pages/NovelEditor'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/editor/:id?" element={<NovelEditor />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
