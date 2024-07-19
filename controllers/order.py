# # app/controllers/order.py
# from utils.database import get_db_connection 
# from schemas.order import OrderCreate, OrderResponse
# from datetime import datetime

# def get_all_orders():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM orders")
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return [OrderResponse(**dict(row)) for row in rows]

# def create_order(order: OrderCreate):
#     conn = get_db_connection()
#     cur = conn.cursor()

#     # Fetch dish price from dishes table
#     cur.execute("SELECT price FROM dishes WHERE id = %s", (order.dish_id,))
#     dish_price = cur.fetchone()[0]

#     # Calculate total price
#     total_price = dish_price * order.quantity

#     # Insert order into orders table
#     cur.execute(
#         "INSERT INTO orders (user_id, dish_id, quantity, total_price, order_date) VALUES (%s, %s, %s, %s, %s) RETURNING *",
#         (order.user_id, order.dish_id, order.quantity, total_price, datetime.now())
#     )
#     row = cur.fetchone()
#     conn.commit()
#     cur.close()
#     conn.close()

#     return OrderResponse(**dict(row))

# def get_order(order_id: int):
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
#     row = cur.fetchone()
#     cur.close()
#     conn.close()
#     if row:
#         return OrderResponse(**dict(row))
#     return None

# def delete_order(order_id: int):
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("DELETE FROM orders WHERE id = %s RETURNING *", (order_id,))
#     row = cur.fetchone()
#     conn.commit()
#     cur.close()
#     conn.close()
#     if row:
#         return OrderResponse(**dict(row))
#     return None

# def get_all_orders_for_user(user_id: int):
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM orders WHERE user_id = %s", (user_id,))
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return [OrderResponse(**dict(row)) for row in rows]
