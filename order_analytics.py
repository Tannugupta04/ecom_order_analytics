import json
from collections import defaultdict, Counter
from datetime import datetime, timedelta

with open("orders.json") as f:
    orders = json.load(f)

total_orders = len(orders)
revenue = 0
order_values = []
product_counter = Counter()
cancelled_count = 0
revenue_by_day = defaultdict(float)
user_spend = defaultdict(float)

for order in orders:
    amount = order["order_amount"]
    order_date = datetime.fromisoformat(order["order_date"])

    if order["order_status"] == "delivered":
        revenue += amount
        revenue_by_day[order_date.date()] += amount
        user_spend[order["user_id"]] += amount

    if order["order_status"] == "cancelled":
        cancelled_count += 1

    order_values.append(amount)

    for item in order["items"]:
        product_counter[item["name"]] += item["qty"]

avg_order_value = round(sum(order_values) / total_orders, 2)
cancellation_rate = round((cancelled_count / total_orders) * 100, 2)
most_popular_product = product_counter.most_common(1)[0]
top_users = sorted(user_spend.items(), key=lambda x: x[1], reverse=True)[:5]

daily_revenue_last_7 = {
    str((datetime.now() - timedelta(days=i)).date()): round(revenue_by_day.get((datetime.now() - timedelta(days=i)).date(), 0), 2)
    for i in range(7)
}

summary = {
    "total_orders": total_orders,
    "total_revenue": round(revenue, 2),
    "average_order_value": avg_order_value,
    "most_popular_product": {
        "name": most_popular_product[0],
        "quantity": most_popular_product[1]
    },
    "cancellation_rate": cancellation_rate,
    "daily_revenue_last_7_days": daily_revenue_last_7,
    "top_5_users_by_spend": top_users
}

with open("analytics_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("✅ Analytics summary written to 'analytics_summary.json'")
