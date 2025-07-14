import React from 'react';
import { Facebook, Twitter, Instagram, Youtube, Mail, Phone, MapPin } from 'lucide-react';

const Footer = () => {
  const footerSections = [
    {
      title: 'Customer Service',
      links: [
        'Contact Us',
        'Help Center',
        'Returns & Exchanges',
        'Shipping Info',
        'Track Your Order',
        'Product Recalls',
        'Accessibility'
      ]
    },
    {
      title: 'Get to Know Us',
      links: [
        'About Walmart',
        'Careers',
        'News & Media',
        'Sustainability',
        'Investor Relations',
        'Supplier Inclusion',
        'Store Directory'
      ]
    },
    {
      title: 'Make Money with Us',
      links: [
        'Sell on Walmart',
        'Marketplace',
        'Advertise with Us',
        'Become an Affiliate',
        'Supply Chain',
        'Corporate Sales',
        'Walmart Business'
      ]
    },
    {
      title: 'Walmart Payment Options',
      links: [
        'Walmart Credit Card',
        'Walmart Mastercard',
        'Walmart Pay',
        'Gift Cards',
        'Pharmacy',
        'Financial Services',
        'Money Services'
      ]
    }
  ];

  const socialLinks = [
    { icon: Facebook, href: '#', label: 'Facebook' },
    { icon: Twitter, href: '#', label: 'Twitter' },
    { icon: Instagram, href: '#', label: 'Instagram' },
    { icon: Youtube, href: '#', label: 'YouTube' }
  ];

  return (
    <footer className="bg-gray-800 text-white">
      {/* Newsletter signup */}
      <div className="bg-blue-600 py-8">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex flex-col md:flex-row items-center justify-between">
            <div className="mb-4 md:mb-0">
              <h3 className="text-2xl font-bold mb-2">Stay Connected</h3>
              <p className="text-blue-100">Get the latest deals and updates delivered to your inbox</p>
            </div>
            <div className="flex w-full md:w-auto">
              <input
                type="email"
                placeholder="Enter your email"
                className="flex-1 md:w-80 px-4 py-3 rounded-l-lg text-gray-800 focus:outline-none focus:ring-2 focus:ring-yellow-400"
              />
              <button className="bg-yellow-400 text-black px-6 py-3 rounded-r-lg font-semibold hover:bg-yellow-500 transition-colors">
                Subscribe
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Main footer content */}
      <div className="py-12">
        <div className="max-w-7xl mx-auto px-4">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {footerSections.map((section, index) => (
              <div key={index}>
                <h4 className="text-lg font-semibold mb-4">{section.title}</h4>
                <ul className="space-y-2">
                  {section.links.map((link, linkIndex) => (
                    <li key={linkIndex}>
                      <a
                        href="#"
                        className="text-gray-300 hover:text-white transition-colors"
                      >
                        {link}
                      </a>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>

          {/* Contact info and social */}
          <div className="mt-12 pt-8 border-t border-gray-700">
            <div className="flex flex-col lg:flex-row justify-between items-center">
              <div className="mb-6 lg:mb-0">
                <div className="flex items-center space-x-1 mb-4">
                  <div className="w-10 h-10 bg-blue-600 rounded-full flex items-center justify-center">
                    <span className="text-white font-bold text-lg">W</span>
                  </div>
                  <span className="text-2xl font-bold">Walmart</span>
                </div>
                <div className="space-y-2 text-gray-300">
                  <div className="flex items-center space-x-2">
                    <Phone size={16} />
                    <span>1-800-WALMART</span>
                  </div>
                  <div className="flex items-center space-x-2">
                    <Mail size={16} />
                    <span>help@walmart.com</span>
                  </div>
                  <div className="flex items-center space-x-2">
                    <MapPin size={16} />
                    <span>702 SW 8th Street, Bentonville, AR 72716</span>
                  </div>
                </div>
              </div>

              <div className="flex flex-col items-center lg:items-end">
                <div className="flex space-x-4 mb-4">
                  {socialLinks.map((social, index) => {
                    const IconComponent = social.icon;
                    return (
                      <a
                        key={index}
                        href={social.href}
                        className="bg-gray-700 p-3 rounded-full hover:bg-gray-600 transition-colors"
                        aria-label={social.label}
                      >
                        <IconComponent size={20} />
                      </a>
                    );
                  })}
                </div>
                <div className="text-sm text-gray-300">
                  <p>Download our app for exclusive deals</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom footer */}
      <div className="bg-gray-900 py-6">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex flex-col md:flex-row justify-between items-center text-sm text-gray-400">
            <div className="mb-4 md:mb-0">
              <p>&copy; 2024 Walmart Inc. All rights reserved.</p>
            </div>
            <div className="flex space-x-6">
              <a href="#" className="hover:text-white transition-colors">Privacy Policy</a>
              <a href="#" className="hover:text-white transition-colors">Terms of Service</a>
              <a href="#" className="hover:text-white transition-colors">Cookie Policy</a>
              <a href="#" className="hover:text-white transition-colors">California Privacy</a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;