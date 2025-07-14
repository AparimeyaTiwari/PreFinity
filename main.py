import requests
import json
import os
from dotenv import load_dotenv
import base64
import re

# Load API key
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

image_path = "./sample images/sample1.jpg"

# Read and encode the image
with open(image_path, "rb") as img_file:
    image_data = base64.b64encode(img_file.read()).decode("utf-8")

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "WalmartShoppingListCLI"
}

payload = {
    "model": "qwen/qwen2.5-vl-32b-instruct:free",
    "messages": [
        {
            "role": "system",
            "content": """You are a smart Walmart shopping assistant. Your job is to read images or text containing shopping lists (including groceries, household supplies, personal care items, etc.) and extract all relevant items. 

                        Please return the results in the following JSON format:
                        {
                            "items": [
                                { 
                                    "name": "Item name", 
                                    "category": "Category ["Hummus, Dips, & Salsa", "Energy Drinks", "Oils & Shortening", "Fresh Soups & Salads", "Game Time Faves", "Sparkling Water", "Better for you", "Healthy Snacks", "Pudding & Gelatin", "Pretzels", "Granola Bars", "Baking Nuts & Seeds", "Yeast", "Milk", "Cheese", "Halloween candy", "Canned & Powdered Milks", "Specialty Cheeses & Meats", "Bacon, Hot Dogs, Sausage", "Variety Pack Snacks", "Drink Mixes", "Eggs", "Orange Juice & Chilled", "Cream & Creamers", "Beverage Deals", "Hard candy & lollipops", "Meat Sticks", "Fruit Snacks", "Chocolate", "Fresh Pizza", "Sugars & Sweeteners", "New Arrivals", "Biscuits, Cookies, Doughs", "Top baking brands", "Mints", "Prepared Meals & Sides", "Yogurt", "Popcorn", "Chips", "Rotisserie Chicken", "Juices", "Deli Meat & Cheese", "Gummy & chewy candy", "Non-Alcoholic Mixers", "Butter & Margarine", "Sports Drinks", "Multipacks & bags", "Crackers", "Fresh Pasta", "Flours & Meals", "Easy to make", "Snack Nuts", "Snacks & Fresh Sandwiches", "Great Value Beverages", "Sour Cream & Chilled Dips", "Kids\' Multi-Packs", "Gum", "Beef Jerky", "Baking Soda & Starch", "Tea", "Fresh Bakery Breads", "Breakfast Meats", "Breakfast Breads", "Cookies & Brownies", "Grilling", "Fresh Food", "Rolls & Buns", "Cakes & Cupcakes", "Emergency & Institutional food", "Cereal & Granola", "Dairy & Eggs", "Breakfast Beverages", "Coffee Accessories", "Tortillas", "Pies", "Donuts, Muffins & Pastries", "Roast Type", "Muffins & Pastries", "Sweet Treats", "Sliced Bread", "Pancakes, Waffles & Syrups", "Herbs, spices & seasonings", "Frozen Meals & Snacks", "Fresh Vegetables", "Salad Kits & Bowls", "Frozen Potatoes", "Organic Produce", "Fresh Dressings", "Condiments", "Salsa & Dips", "Cooking oils & vinegars", "Plant-based Protein & Tofu", "Soup", "Fresh Fruits", "Frozen Meat & Seafood", "Frozen Desserts", "Canned goods", "Frozen Breakfast", "Cut Fruits & Vegetables", "Pasta & pizza", "International foods", "Coffee Additives", "Fresh Herbs", "Frozen Pizza, Pasta, & Breads", "Rice, grains & dried beans", "Frozen Produce", "Coffee By Type", "Canned vegetables", "Hot Cereals", "Packaged meals & side dishes", "Wine", "Spirits", "Beer"]", 
                                    "quantity": "Quantity (e.g., 1, 2, kg, lb, grams, oz, etc.)", 
                                    "price": "Price (if available, otherwise leave empty)" 
                                }
                            ]
                        }
                        Ensure that each item is categorized correctly and into one of the given categories only and includes the name, category, quantity, and price if available.
                        Avoid including items that are stroked off.
                        Avoid non-shopping items. ONLY return the JSON object, nothing else."""
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Extract a structured shopping list from this image and categorize each item appropriately."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_data}"
                    }
                }
            ]
        }
    ]
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(payload))

try:
    result = response.json()
    raw_content = result['choices'][0]['message']['content']

    # Remove code block wrappers like ```json ... ```
    json_str = re.sub(r"^```json\s*|```$", "", raw_content.strip(), flags=re.IGNORECASE).strip()
    
    # If it starts with json: prefix (without backticks)
    if json_str.lower().startswith("json"):
        json_str = json_str[4:].strip()
    
    parsed_json = json.loads(json_str)

    print("\n🧾 Parsed Shopping List:\n")
    print(json.dumps(parsed_json, indent=2))

except Exception as e:
    print("❌ Error parsing response:", e)
    print("Raw response:", response.text)
