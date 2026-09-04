import sqlite3
import os

def get_db_connection():
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'inventory.db')
    return sqlite3.connect(db_path)

def add_stock(product_id, quantity_to_add):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT name, stock_quantity FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        
        if not product:
            print("Error: Product ID not found.")
            return
            
        name, current_stock = product
        new_stock = current_stock + quantity_to_add
        
        cursor.execute("UPDATE products SET stock_quantity = ? WHERE id = ?", (new_stock, product_id))
        conn.commit()
        
        print(f"\nSuccess: Restocked {name}. Old Stock: {current_stock} -> New Stock: {new_stock}")
        
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    finally:
        conn.close()