function ProductCard({ prod }) {
  return (
    <div className="product-card">
      <h4>{prod.name}</h4>
      <p className="price-tag">${prod.price}</p>
      <p style={{ color: '#666' }}>Stock: {prod.stock_quantity}</p>
      <p style={{ color: '#666' }}>Category: {prod.category.name}</p>
      {console.log(prod)}
    </div>
  );
}
export default ProductCard;