import sqlite3
import os

def get_db_connection():
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'inventory.db')
    return sqlite3.connect(db_path)

def check_low_stock(threshold=5):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, stock_quantity FROM products WHERE stock_quantity <= ?", (threshold,))
    low_stock_items = cursor.fetchall()
    
    if low_stock_items:
        print("\n" + "!"*50)
        print(" WARNING: LOW STOCK ALERTS ".center(50, "!"))
        print("!"*50)
        for item in low_stock_items:
            print(f" -> {item[0]} is running low! Only {item[1]} left in stock.")
        print("!"*50 + "\n")
        
    conn.close()