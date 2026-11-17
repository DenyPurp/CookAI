import { useState, useEffect } from 'react'

function App() {
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  // Загружаем продукты при монтировании компонента
  useEffect(() => {
    fetch('/api/products/')
      .then(response => {
        if (!response.ok) throw new Error('Ошибка сети')
        return response.json()
      })
      .then(data => {
        setProducts(data)
        setLoading(false)
      })
      .catch(err => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  if (loading) return <div style={{ padding: '20px' }}>Загрузка продуктов...</div>
  if (error) return <div style={{ padding: '20px', color: 'red' }}>Ошибка: {error}</div>

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>CookAI - Справочник продуктов</h1>
      <p>Всего продуктов в базе: <strong>{products.length}</strong></p>

      <table border="1" cellPadding="8" cellSpacing="0" style={{ borderCollapse: 'collapse', width: '100%', maxWidth: '800px', marginTop: '20px' }}>
        <thead style={{ backgroundColor: '#f0f0f0' }}>
          <tr>
            <th>ID</th>
            <th>Название</th>
            <th>Категория</th>
            <th>Ккал</th>
            <th>Белки</th>
            <th>Жиры</th>
            <th>Углеводы</th>
          </tr>
        </thead>
        <tbody>
          {products.map(product => (
            <tr key={product.id}>
              <td>{product.id}</td>
              <td>{product.name}</td>
              <td>{product.category_display}</td>
              <td>{product.calories}</td>
              <td>{product.protein}</td>
              <td>{product.fat}</td>
              <td>{product.carbs}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default App