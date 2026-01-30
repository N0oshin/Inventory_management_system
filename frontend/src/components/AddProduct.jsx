import { useState } from "react";

function AddProduct({ categories, onAdd }) {
  const [formData, setFormData] = useState({
    name: '',
    price: '',
    stock_quantity: '',
    category_id: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    const submissionData = {
      name: formData.name,
      price: parseFloat(formData.price), 
      stock_quantity: parseInt(formData.stock_quantity, 10), 
      category_id: formData.category_id,
      description: null // send null for the optional field
    };
    onAdd(submissionData);   // send the data Up to the parent
    setFormData({ name: "", price: "", stock_quantity: "", category_id: "" }); // Clear form
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: '20px', display: 'flex', gap: '10px' }}>
        <input value={formData.name} onChange={(e) => setFormData({...formData, name: e.target.value})} type="text"
        placeholder="name"/>
        <input value={formData.price} onChange={(e) => setFormData({...formData, price: e.target.value})} type="number" placeholder="price"/>
        <input value={formData.stock_quantity} onChange={(e) => setFormData({...formData, stock_quantity: e.target.value})} type="number" placeholder="stock"/>
        <select value={formData.category_id} 
            onChange={(e) => setFormData({...formData, category_id: e.target.value})}>
            <option value="">Category</option>
            {categories.map(cat => (
                <option key={cat.id} value={cat.id}>
                {cat.name}
            </option>
            ))}
        </select>
        <button type="submit">Add Product</button>
    </form>
    );
}
export default AddProduct;
