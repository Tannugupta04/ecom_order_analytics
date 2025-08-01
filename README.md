# 📊 E-Commerce Order Analytics

## 🔧 Setup Instructions

### Step 1: Install Flask
```bash
pip install flask

🚀 How to Run the Scripts
1. Generate Synthetic Orders
Creates orders.json with 1000–5000 randomly generated e-commerce orders.

bash
Copy code
python data_generator.py
2. Run Order Analytics
Analyzes the orders and outputs key metrics to analytics_summary.json.

bash
Copy code
python order_analytics.py
3. (Optional) Run the Flask API
Serves the analytics via HTTP endpoints.

bash
Copy code
python app.py

🌐 API Endpoints (via app.py)
Endpoint	Description
/summary	Returns all computed metrics (JSON)
/user/<user_id>	Returns all orders placed by the specified user
/daily_revenue	Returns daily revenue for the last 7 days

Example:

http://127.0.0.1:5000/summary


http://127.0.0.1:5000/user/U102 (Replace U102 with a real user ID)

http://127.0.0.1:5000/daily_revenue

📊 Output Files
orders.json – Contains all generated order data.

analytics_summary.json – Contains all calculated metrics including:

Total number of orders

Total revenue (from delivered orders)

Average order value

Most popular product

Cancellation rate

Daily revenue (last 7 days)

Top 5 users by spend

📌 Notes
Data is randomly generated, so results will vary each time.

All dates are in ISO format and reflect the past 0–10 days.


