
function CategorySidebar({ categories, selectedId, onSelect }) {
  return (
    <aside className="sidebar">
      <h2>Inventory</h2>
      <hr />
      <h3>Categories</h3>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        <li 
          onClick={() => onSelect(null)}
          style={{ 
            cursor: 'pointer', padding: '10px 0',
            fontWeight: selectedId === null ? 'bold' : 'normal',
            color: selectedId === null ? '#3498db' : 'inherit'
          }}
        >
          All Products
        </li>
        {categories.map(cat => (
          <li 
            key={cat.id} 
            onClick={() => onSelect(cat.id)}
            style={{ 
              padding: '10px 0', cursor: 'pointer', borderBottom: '1px solid #eee',
              fontWeight: selectedId === cat.id ? 'bold' : 'normal',
              color: selectedId === cat.id ? '#3498db' : 'inherit'
            }}
          >
            {cat.name}
          </li>
        ))}
      </ul>
    </aside>
  );
}
export default CategorySidebar;