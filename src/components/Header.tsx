import React, { useState } from 'react';
import { Search, ShoppingCart, Menu, MapPin, User, Heart, X, ChevronDown } from 'lucide-react';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [showSearchSuggestions, setShowSearchSuggestions] = useState(false);

  const searchSuggestions = [
    'iPhone 15',
    'Samsung TV',
    'Nike shoes',
    'Instant pot',
    'Bluetooth headphones',
    'Laptop',
    'Groceries',
    'Toys'
  ];

  const departments = [
    'Groceries', 'Electronics', 'Clothing', 'Home', 'Toys', 'Sports', 'Auto', 'Health'
  ];

  return (
    <header className="bg-white shadow-md relative z-50">
      {/* Top bar */}
      <div className="bg-blue-600 text-white text-sm py-2">
        <div className="max-w-7xl mx-auto px-4 flex justify-between items-center">
          <div className="flex items-center space-x-4">
            <span>Free shipping on orders $35+</span>
            <span className="hidden md:block">|</span>
            <span className="hidden md:block">Save with Walmart+</span>
          </div>
          <div className="flex items-center space-x-4">
            <button className="hover:text-blue-200 transition-colors">Sign in</button>
            <span className="hidden md:block">|</span>
            <button className="hover:text-blue-200 transition-colors hidden md:block">Create account</button>
          </div>
        </div>
      </div>

      {/* Main header */}
      <div className="max-w-7xl mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          {/* Logo and Menu */}
          <div className="flex items-center space-x-4">
            <button 
              className="md:hidden p-2 hover:bg-gray-100 rounded-full transition-colors"
              onClick={() => setIsMenuOpen(!isMenuOpen)}
            >
              <Menu size={24} />
            </button>
            <div className="flex items-center space-x-1">
              <div className="w-10 h-10 bg-blue-600 rounded-full flex items-center justify-center">
                <span className="text-white font-bold text-lg">W</span>
              </div>
              <span className="text-2xl font-bold text-blue-600">Walmart</span>
            </div>
          </div>

          {/* Search */}
          <div className="flex-1 max-w-xl mx-4 relative">
            <div className="relative">
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                onFocus={() => setShowSearchSuggestions(true)}
                placeholder="Search everything at Walmart online and in store"
                className="w-full pl-4 pr-12 py-3 border border-gray-300 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
              <button className="absolute right-2 top-1/2 transform -translate-y-1/2 bg-yellow-400 p-2 rounded-full hover:bg-yellow-500 transition-colors">
                <Search size={20} />
              </button>
            </div>

            {/* Search suggestions */}
            {showSearchSuggestions && (
              <div className="absolute top-full left-0 right-0 bg-white border border-gray-200 rounded-lg mt-1 shadow-lg max-h-60 overflow-y-auto z-50">
                {searchSuggestions.map((suggestion, index) => (
                  <button
                    key={index}
                    className="w-full text-left px-4 py-2 hover:bg-gray-100 transition-colors"
                    onClick={() => {
                      setSearchQuery(suggestion);
                      setShowSearchSuggestions(false);
                    }}
                  >
                    {suggestion}
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Right side icons */}
          <div className="flex items-center space-x-4">
            <button className="hidden md:flex items-center space-x-1 hover:text-blue-600 transition-colors">
              <MapPin size={20} />
              <span className="text-sm">Store finder</span>
            </button>
            <button className="flex items-center space-x-1 hover:text-blue-600 transition-colors">
              <Heart size={20} />
              <span className="text-sm hidden md:block">Reorder</span>
            </button>
            <button className="flex items-center space-x-1 hover:text-blue-600 transition-colors">
              <User size={20} />
              <span className="text-sm hidden md:block">Account</span>
            </button>
            <button className="flex items-center space-x-1 hover:text-blue-600 transition-colors relative">
              <ShoppingCart size={20} />
              <span className="text-sm hidden md:block">Cart</span>
              <span className="absolute -top-2 -right-2 bg-yellow-400 text-black text-xs rounded-full w-5 h-5 flex items-center justify-center">3</span>
            </button>
          </div>
        </div>
      </div>

      {/* Departments navigation */}
      <nav className="bg-gray-50 border-t border-gray-200 hidden md:block">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex items-center space-x-8 py-3">
            <button className="flex items-center space-x-1 text-gray-700 hover:text-blue-600 transition-colors">
              <Menu size={18} />
              <span>Departments</span>
              <ChevronDown size={16} />
            </button>
            {departments.map((dept) => (
              <button
                key={dept}
                className="text-gray-700 hover:text-blue-600 transition-colors whitespace-nowrap"
              >
                {dept}
              </button>
            ))}
          </div>
        </div>
      </nav>

      {/* Mobile menu */}
      {isMenuOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-50 z-50 md:hidden">
          <div className="bg-white w-80 h-full overflow-y-auto">
            <div className="p-4 border-b border-gray-200 flex justify-between items-center">
              <h2 className="text-lg font-semibold">Menu</h2>
              <button
                onClick={() => setIsMenuOpen(false)}
                className="p-2 hover:bg-gray-100 rounded-full"
              >
                <X size={20} />
              </button>
            </div>
            <div className="p-4 space-y-4">
              {departments.map((dept) => (
                <button
                  key={dept}
                  className="block w-full text-left py-2 text-gray-700 hover:text-blue-600 transition-colors"
                >
                  {dept}
                </button>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Overlay for search suggestions */}
      {showSearchSuggestions && (
        <div 
          className="fixed inset-0 z-40"
          onClick={() => setShowSearchSuggestions(false)}
        />
      )}
    </header>
  );
};

export default Header;