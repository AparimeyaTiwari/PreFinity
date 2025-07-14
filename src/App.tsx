import React from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import Categories from './components/Categories';
import ProductSection from './components/ProductSection';
import Footer from './components/Footer';
import { featuredProducts, dealsProducts, groceryProducts } from './data/products';

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <Hero />
      <Categories />
      <ProductSection 
        title="Featured Products" 
        products={featuredProducts} 
        backgroundColor="bg-white"
      />
      <ProductSection 
        title="Today's Deals" 
        products={dealsProducts} 
        backgroundColor="bg-red-50"
      />
      <ProductSection 
        title="Grocery Essentials" 
        products={groceryProducts} 
        backgroundColor="bg-green-50"
      />
      <Footer />
    </div>
  );
}

export default App;