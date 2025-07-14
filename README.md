# 🛒 Personalized Smart Cart Recommender

**Team Project | Walmart Sparkathon**

Welcome to our Personalization Tool — a hybrid recommendation engine built using **Neo4j Knowledge Graphs**, fuzzy matching, and smart user profiling. Our solution enables seamless, intelligent product recommendations, auto-populated carts, and optimized in-store navigation.

---

## 🚀 Project Overview

Our tool automatically **recommends and adds products to a user's cart** based on their personal preferences. The moment a user logs in and completes a short quiz, our system constructs a personalized profile and uses it to curate their shopping experience.

---

## 🔧 How It Works

### 1. **User Quiz & Profile Generation**
- On login, users take a quiz.
- We extract 4 key personalization parameters:
  - **Brand Loyalty**
  - **Price Sensitivity**
  - **Health Consciousness**
  - **Adventurousness**
- These traits are stored in the **User Node** in a Neo4j Knowledge Graph.

### 2. **Knowledge Graph Structure**
- The graph has interconnected nodes:
  - `User` → `Traits`
  - `User` → `Likes` → `Brands`
  - `User` → `Purchased` → `Products`
  - `Products` → `Belongs_To` → `Category`
  - `Products` → `Located_At` → `Aisle`
- We log interactions such as:
  - Views
  - Purchases
  - Brand affinity

### 3. **Recommendation Pipeline**
- Input: JSON with product name and category.
- Steps:
  1. **Fuzzy Match** product name in the selected category.
  2. Filter by user’s purchase history (if a product is bought >5 times, we recommend that).
  3. If not, we rank and apply trait filters:
     - Sort personalization parameters (brand, price, health).
     - Sequentially filter products by each trait.
     - Use **Adventurousness** to decide between known and new items.
  4. **Final recommendation is added to the user’s cart**.

### 4. **Smart In-Store Navigation**
- If user chooses in-store pickup:
  - Product aisle locations are included.
  - Aisles are sorted for efficient path planning.
  - Reduces store time and budget overspend.

---

## 🔮 Future Enhancements

- **User Clustering** (based on age, region, preferences) for even smarter suggestions.
- **Real-Time Notifications** for new or on-sale items users might love.
- **Auto-Cart Integration** with Walmart’s system via APIs.
- Support for **image or natural language input** to trigger cart recommendations.

---
## 📬 Contact
Have questions or want to collaborate?
- Aparimeya Tiwari: https://www.linkedin.com/in/aparimeya-tiwari-76a252252/
- Vinayak Khavare: https://www.linkedin.com/in/vinayak-khavare-542821257/
- Richa Rathi: https://www.linkedin.com/in/richa-rathi-775871257/
- Sahil Adit: https://www.linkedin.com/in/sahiladit/


