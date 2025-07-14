import React from 'react';
import { 
  ShoppingCart, 
  Laptop, 
  Shirt, 
  Home, 
  Baby, 
  Gamepad2, 
  Car, 
  Heart,
  Gift,
  Camera,
  Wrench,
  Book
} from 'lucide-react';

const Categories = () => {
  const categories = [
    {
      id: 1,
      name: 'Groceries',
      icon: ShoppingCart,
      color: 'bg-green-500',
      image: 'https://images.pexels.com/photos/264636/pexels-photo-264636.jpeg?auto=compress&cs=tinysrgb&w=400'
    },
    {
      id: 2,
      name: 'Electronics',
      icon: Laptop,
      color: 'bg-blue-500',
      image: 'https://images.pexels.com/photos/356056/pexels-photo-356056.jpeg?auto=compress&cs=tinysrgb&w=400'
    },
    {
      id: 3,
      name: 'Clothing',
      icon: Shirt,
      color: 'bg-purple-500',
      image: 'https://images.pexels.com/photos/996329/pexels-photo-996329.jpeg?auto=compress&cs=tinysrgb&w=400'
    },
    {
      id: 4,
      name: 'Home',
      icon: Home,
      color: 'bg-orange-500',
      image: 'https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=400'
    },
    {
      id: 5,
      name: 'Baby',
      icon: Baby,
      color: 'bg-pink-500',
      image: 'https://images.pexels.com/photos/1166473/pexels-photo-1166473.jpeg?auto=compress&cs=tinysrgb&w=400'
    },
    {
      id: 6,
      name: 'Toys',
      icon: Gamepad2,
      color: 'bg-yellow-500',
      image: 'https://images.pexels.com/photos/163064/play-stone-network-networked-interactive-163064.jpeg?auto=compress&cs=tinysrgb&w=400'
    },
    {
      id: 7,
      name: 'Auto',
      icon: Car,
      color: 'bg-gray-500',
      image: 'https://images.pexels.com/photos/116675/pexels-photo-116675.jpeg?auto=compress&cs=tinysrgb&w=400'
    },
    {
      id: 8,
      name: 'Health',
      icon: Heart,
      color: 'bg-red-500',
      image: 'https://images.pexels.com/photos/356040/pexels-photo-356040.jpeg?auto=compress&cs=tinysrgb&w=400'
    },
    {
      id: 9,
      name: 'Gifts',
      icon: Gift,
      color: 'bg-indigo-500',
      image: 'https://images.pexels.com/photos/264917/pexels-photo-264917.jpeg?auto=compress&cs=tinysrgb&w=400'
    },
    {
      id: 10,
      name: 'Sports',
      icon: Camera,
      color: 'bg-teal-500',
      image: 'https://images.pexels.com/photos/863988/pexels-photo-863988.jpeg?auto=compress&cs=tinysrgb&w=400'
    },
    {
      id: 11,
      name: 'Tools',
      icon: Wrench,
      color: 'bg-amber-500',
      image: 'https://images.pexels.com/photos/162553/keys-workshop-mechanic-tools-162553.jpeg?auto=compress&cs=tinysrgb&w=400'
    },
    {
      id: 12,
      name: 'Books',
      icon: Book,
      color: 'bg-emerald-500',
      image: 'https://images.pexels.com/photos/159711/books-bookstore-book-reading-159711.jpeg?auto=compress&cs=tinysrgb&w=400'
    }
  ];

  return (
    <section className="py-12 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4">
        <h2 className="text-3xl font-bold text-center mb-8 text-gray-800">
          Shop by Category
        </h2>
        
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-6">
          {categories.map((category) => {
            const IconComponent = category.icon;
            return (
              <div
                key={category.id}
                className="group bg-white rounded-lg shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer transform hover:-translate-y-1"
              >
                <div className="relative overflow-hidden rounded-t-lg">
                  <img
                    src={category.image}
                    alt={category.name}
                    className="w-full h-32 object-cover group-hover:scale-110 transition-transform duration-300"
                  />
                  <div className="absolute inset-0 bg-black bg-opacity-20 group-hover:bg-opacity-10 transition-all duration-300"></div>
                  <div className={`absolute top-2 right-2 ${category.color} p-2 rounded-full`}>
                    <IconComponent size={20} className="text-white" />
                  </div>
                </div>
                <div className="p-4">
                  <h3 className="font-semibold text-gray-800 group-hover:text-blue-600 transition-colors">
                    {category.name}
                  </h3>
                  <p className="text-sm text-gray-600 mt-1">Shop now</p>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default Categories;