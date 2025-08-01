import random
import json
from datetime import datetime, timedelta

PRODUCTS = [
    {"name": "T-shirt", "price": 499},
    {"name": "Jeans", "price": 1299},
    {"name": "Shoes", "price": 1999},
    {"name": "Cap", "price": 299},
    {"name": "Socks", "price": 99},
    {"name": "Jacket", "price": 2499},
    {"name": "Shirt", "price": 899}
]

STATUS = ["delivered", "cancelled", "returned", "pending"]
NUM_ORDERS = random.randint(1000, 5000)

def generate_order():
    items = []
    total = 0
    for _ in range(random.randint(1, 4)):
        product = random.choice(PRODUCTS)
        qty = random.randint(1, 3)
        total += product["price"] * qty
        items.append({
            "name": product["name"],
            "qty": qty,
            "price": product["price"]
        })

    return {
        "order_id": f"ORD{random.randint(10000, 99999)}",
        "user_id": f"U{random.randint(100, 999)}",
        "order_amount": round(total, 2),
        "items": items,
        "order_status": random.choice(STATUS),
        "order_date": (datetime.now() - timedelta(days=random.randint(0, 10))).isoformat()
    }

orders = [generate_order() for _ in range(NUM_ORDERS)]

with open("orders.json", "w") as f:
    json.dump(orders, f, indent=2)

print(f"✅ Generated {NUM_ORDERS} orders into 'orders.json'")
