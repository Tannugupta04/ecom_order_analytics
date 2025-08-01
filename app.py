from flask import Flask, jsonify
import json

app = Flask(__name__)

with open("orders.json") as f:
    orders = json.load(f)

with open("analytics_summary.json") as f:
    analytics = json.load(f)

@app.route("/summary")
def get_summary():
    return jsonify(analytics)

@app.route("/user/<user_id>")
def get_user_orders(user_id):
    user_orders = [order for order in orders if order["user_id"] == user_id]
    return jsonify(user_orders)

@app.route("/daily_revenue")
def get_daily_revenue():
    return jsonify(analytics["daily_revenue_last_7_days"])

if __name__ == "__main__":
    app.run(debug=True)
