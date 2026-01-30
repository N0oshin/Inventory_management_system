
import { useState, useEffect } from "react";
import axios from "axios";
import CategorySidebar from "./components/CategorySidebar";
import ProductCard from "./components/ProductCard";
import AddProduct from "./components/AddProduct";

function App() {
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);
  const [selectedCategoryId, setSelectedCategoryId] = useState(null);

  useEffect(() => {
    axios.get("http://localhost:8000/categories/").then(res => setCategories(res.data));
    axios.get("http://localhost:8000/products/").then(res => setProducts(res.data));
  }, []);

  const filteredProducts = selectedCategoryId 
    ? products.filter(p => p.category_id === selectedCategoryId)
    : products;

  const handleAddNewProduct = async(newProduct) => {
    try {
      const res = await axios.post("http://localhost:8000/products/", newProduct);
      setProducts([...products, res.data]);
    } catch (error) {
      console.error("Error adding product:", error);
    }
  };

  return (
    <div className="dashboard-container">

      <CategorySidebar 
        categories={categories} 
        selectedId={selectedCategoryId} 
        onSelect={setSelectedCategoryId} 
      />

      <main className="main-content">
        <h1>Products</h1>
        <AddProduct 
          categories={categories} 
          onAdd={handleAddNewProduct}
        />
        <div className="product-grid">
          {filteredProducts.map(prod => (
            <ProductCard key={prod.id} prod={prod} />
          ))}
        </div>
      </main>
    </div>
  );
}
export default App;


