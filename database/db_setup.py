import sqlite3
import os

# Creates the database in the root folder
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'inventory.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    stock_quantity INTEGER
)
''')

# Insert sample data for testing
cursor.execute("INSERT OR IGNORE INTO products (id, name, price, stock_quantity) VALUES (101, 'Wireless Mouse', 850.00, 50)")
conn.commit()
conn.close()
print("Database and tables initialized successfully!")