import sqlite3
import os

def get_db_connection():
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'inventory.db')
    return sqlite3.connect(db_path)

def view_all_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, price, stock_quantity FROM products")
    products = cursor.fetchall()
    
    print("\n" + "="*50)
    print(f"{'ID':<5} | {'Product Name':<20} | {'Price':<10} | {'Stock':<5}")
    print("="*50)
    
    for p in products:
        print(f"{p[0]:<5} | {p[1]:<20} | ₹{p[2]:<9.2f} | {p[3]:<5}")
    
    print("="*50 + "\n")
    conn.close()

def add_new_product(pid, name, price, stock):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO products (id, name, price, stock_quantity) VALUES (?, ?, ?, ?)", 
                      (pid, name, price, stock))
        conn.commit()
        print(f"Success: {name} added to the database.")
    except sqlite3.IntegrityError:
        print("Error: A product with that ID already exists.")
    finally:
        conn.close()