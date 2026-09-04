import sqlite3
import os

def get_db_connection():
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'inventory.db')
    return sqlite3.connect(db_path)

def search_product_by_name(search_term):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # The % symbol allows for partial matches (e.g., searching "mouse" finds "Wireless Mouse")
    cursor.execute("SELECT id, name, price, stock_quantity FROM products WHERE name LIKE ?", 
                  ('%' + search_term + '%',))
    results = cursor.fetchall()
    
    if not results:
        print(f"\nNo products found matching '{search_term}'.")
    else:
        print("\n" + "="*50)
        print(f"{'ID':<5} | {'Product Name':<20} | {'Price':<10} | {'Stock':<5}")
        print("="*50)
        for p in results:
            print(f"{p[0]:<5} | {p[1]:<20} | ₹{p[2]:<9.2f} | {p[3]:<5}")
        print("="*50 + "\n")
        
    conn.close()