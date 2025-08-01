# 📊 E-Commerce Order Analytics

## 🔧 Setup Instructions

### Step 1: Install Flask

pip install flask

🚀 How to Run the Scripts
1. Generate Synthetic Orders
Creates orders.json with 1000–5000 randomly generated e-commerce orders.


# python data_generator.py
2. Run Order Analytics
Analyzes the orders and outputs key metrics to analytics_summary.json.

# python order_analytics.py
3. (Optional) Run the Flask API
Serves the analytics via HTTP endpoints.


# python app.py

🌐 API Endpoints (via app.py)
Endpo int	Description
/summary	Returns all computed metrics (JSON)
/user/<user_id>	Returns all orders placed by the specified user
/daily_revenue	Returns daily revenue for the last 7 days

Example:

http://127.0.0.1:5000/summary
when visit on this we  get what i attached in screenshot:
<img width="732" height="1034" alt="Screenshot 2025-08-01 221205" src="https://github.com/user-attachments/assets/972ddcb2-d86d-4927-8f6b-d86af7995a95" />


http://127.0.0.1:5000/user/U102 (Replace U102 with a real user ID)

<img width="952" height="1572" alt="Screenshot 2025-08-01 221213" src="https://github.com/user-attachments/assets/f3c372e8-3f3d-42d2-afcf-73c9c4deeea1" />

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


