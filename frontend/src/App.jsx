import { useState, useEffect } from 'react'

function App() {
  const [status, setStatus] = useState('Проверка...')

  useEffect(() => {
    // Делаем запрос к нашему API
    fetch('http://127.0.0.1:8000/api/health/')
      .then(response => response.json())
      .then(data => {
        setStatus(data.status) // Ожидаем "ok"
      })
      .catch(error => {
        console.error("Ошибка:", error)
        setStatus('Ошибка подключения')
      })
  }, [])

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>CookAI - Генератор рецептов</h1>
      <div style={{ padding: '10px', border: '1px solid #ccc', borderRadius: '5px' }}>
        <h3>Статус бэкенда:</h3>
        <p style={{ color: status === 'ok' ? 'green' : 'red', fontWeight: 'bold' }}>
          {status}
        </p>
      </div>
    </div>
  )
}

export default App