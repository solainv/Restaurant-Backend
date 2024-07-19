# app\create_tables.py
import psycopg2
from psycopg2 import sql

connection_info = {
    "host": "localhost",
    "port": "2222",
    "database": "my-imbiss",
    "user": "postgres",
    "password": "0808"
}

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL DEFAULT 'user'
);
"""

create_dishes_table = """
CREATE TABLE IF NOT EXISTS dishes (
    id SERIAL PRIMARY KEY AUTO INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    image TEXT,
);
"""

create_orders_table = """ 
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    dish_id INT NOT NULL,
    quantity INT NOT NULL,
    total_price NUMERIC(10, 2) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (dish_id) REFERENCES dishes (id)
);
"""

create_reservations_table = """
CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    reservation_date TIMESTAMP NOT NULL,
    guests_count INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

try:
    conn = psycopg2.connect(**connection_info)
    cur = conn.cursor()
    cur.execute(create_users_table)
    cur.execute(create_dishes_table)
    cur.execute(create_orders_table)
    cur.execute(create_reservations_table)
    conn.commit()
    print("Tables created successfully")
except Exception as e:
    print(f"Error creating tables: {e}")
finally:
    if conn:
        cur.close()
        conn.close()
