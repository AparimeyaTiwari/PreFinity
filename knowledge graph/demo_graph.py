from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Critical Checkpoint 1: Verify Environment Variables ---
URI = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

if not URI or not username or not password:
    raise RuntimeError("Missing one or more environment variables")
print(f"URI: {URI}")
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")

# Connect to Neo4j
try:
    driver = GraphDatabase.driver(URI, auth=(username, password), connection_timeout=30)
    driver.verify_connectivity()
    print("Neo4j driver connected successfully!")
except Exception as e:
    print(f"Failed to connect to Neo4j: {e}")
    exit(1)

def threshold_loyal(loyality_score,min_thres = 2,max_thres = 15):
    return int(max_thres-loyality_score*(max_thres-min_thres))

def add_new_user(uid,name,age,gender,email,ps,hc,ad,bl):
    summary = driver.execute_query(
    """
        MERGE (u:User:USER_DB {uid: $uid})
        ON CREATE SET 
            u.name = $name, 
            u.age = $age, 
            u.gender = $gender, 
            u.email = $email
        MERGE (t:Traits:USER_DB {uid: $uid})
        ON CREATE SET 
            t.price_sensitivity = $ps, 
            t.health_conscious = $hc,
            t.adventurous = $ad,
            t.brand_loyality = $bl
        MERGE (u)-[:HAS]->(t)
        """,
        uid=uid,
        name=name,
        age=age,
        gender=gender,
        email=email,
        ps=ps,
        hc=hc,
        ad=ad,
        bl=bl
    )

def add_purchase_history(uid, upc, product_name, category, brand, price_retail, health_score, quantity):
    summary = driver.execute_query(
        """
        MATCH (u:User:USER_DB {uid: $uid})
        
        MERGE (p:Product:USER_DB {upc: $upc})
            ON CREATE SET
                p.product_name = $product_name,
                p.brand = $brand,
                p.category = $category,
                p.price_retail = $price_retail,
                p.health_score = $health_score

        MERGE (b:Brand:USER_DB {name: $brand})

        MERGE (p)-[:OF_BRAND]->(b)

        MERGE (u)-[r:PURCHASED]->(p)
            ON CREATE SET r.quantity = $quantity
            ON MATCH SET r.quantity = coalesce(r.quantity, 0) + $quantity
        """,
        {
            "uid": uid,
            "upc": upc,
            "product_name": product_name,
            "category": category,
            "brand": brand,
            "price_retail": price_retail,
            "health_score": health_score,
            "quantity": quantity
        }
    )
    return summary

def prefered_brands(uid):
    # Step 1: Get brand loyalty score
    records, _, _ = driver.execute_query(
        """
        MATCH (u:User:USER_DB {uid: $uid})-[:HAS]->(t:Traits:USER_DB)
        RETURN t.brand_loyality AS loyalty
        """,
        {"uid": uid}
    )

    if not records or not records[0]['loyalty']:
        return "User loyalty not found"

    bl = records[0]['loyalty']
    threshold = threshold_loyal(bl)

    # Step 2: Aggregate total quantity by brand
    brand_records, _, _ = driver.execute_query(
        """
        MATCH (u:User:USER_DB {uid: $uid})-[r:PURCHASED]->(p:Product:USER_DB)-[:OF_BRAND]->(b:Brand:USER_DB)
        RETURN b.name AS brand, SUM(r.quantity) AS total_quantity
        """,
        {"uid": uid}
    )

    # Step 3: Create LIKES relationships
    for record in brand_records:
        if record["total_quantity"] >= threshold:
            driver.execute_query(
                """
                MATCH (u:User:USER_DB {uid: $uid}), (b:Brand:USER_DB {name: $brand})
                MERGE (u)-[:LIKES]->(b)
                """,
                {"uid": uid, "brand": record["brand"]}
            )

    return f"Updated brand preferences for user {uid}."



# --- Usage Example ---



add_new_user("U2512","Richa Rathi","22",'f','rr@microsoft.com',0.8,0.4,0.49,0.38)
add_purchase_history(uid="U2512", upc="491214", product_name="Chef Boyardee Chicken Alfredo Pasta, Microwaveable Pasta, 15 oz", brand="Chef Boyardee", price_retail=1.24, health_score=7, category="Pasta & pizza", quantity=2)
add_purchase_history(uid="U2512", upc="417534", product_name="Fresh Cravings Mild Chunky Salsa, 16 oz", brand="Fresh Cravings", price_retail=3.32, health_score=7, category="Salsa & Dips", quantity=1)
add_purchase_history(uid="U2512", upc="186306", product_name="Great Value Deluxe Mixed Nuts, 30 oz", brand="Great Value", price_retail=14.98, health_score=5, category="Snack Nuts", quantity=3)
add_purchase_history(uid="U2512", upc="207767", product_name="Bigelow Herbal Tea, Chamomile Vanilla And Honey, 20 ct", brand="Bigelow Tea", price_retail=2.98, health_score=7, category="Tea", quantity=2)
add_purchase_history(uid="U2512", upc="491344", product_name="Ragu Old World Style Traditional Sauce, Made with Olive Oil, 24 oz", brand="Ragú", price_retail=1.96, health_score=5, category="Pasta & pizza", quantity=4)
add_purchase_history(uid="U2512", upc="186742", product_name="Planters Deluxe Lightly Salted Mixed Nuts with Sea Salt, 15.25 oz", brand="Planters", price_retail=9.98, health_score=7, category="Snack Nuts", quantity=5)
add_purchase_history(uid="U2512", upc="210744", product_name="Great Value Chamomile Herbal Tea Bags, 1.41 oz, 40 Count", brand="Great Value", price_retail=3.72, health_score=8, category="Tea", quantity=1)
add_purchase_history(uid="U2512", upc="417427", product_name="Concord Foods Concord Foods Candy Apple Kit, 5 oz", brand="Concord Foods", price_retail=1.48, health_score=7, category="Salsa & Dips", quantity=2)
add_purchase_history(uid="U2512", upc="186788", product_name="Planters Mixed Nuts Less Than 50% Peanuts with Sea Salt, 10.3 oz", brand="Planters", price_retail=5.23, health_score=7, category="Snack Nuts", quantity=2)
add_purchase_history(uid="U2512", upc="209337", product_name="Great Value Peach Tea Drink Enhancer, 1.62 Fl Oz", brand="Great Value", price_retail=2.12, health_score=8, category="Tea", quantity=3)

prefered_brands("U2512")
# --- Critical Checkpoint 3: Close Driver ---
driver.close()
print("Neo4j driver closed.")
