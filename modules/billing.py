import sqlite3
import os
from datetime import datetime

# Connects to the database we just created
def get_db_connection():
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'inventory.db')
    return sqlite3.connect(db_path)

def process_transaction(product_id, quantity_purchased):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Check if the product exists
        cursor.execute("SELECT name, price, stock_quantity FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        
        if not product:
            print("Error: Product ID not found.")
            return
            
        name, price, current_stock = product
        
        # Check stock levels
        if current_stock < quantity_purchased:
            print(f"Transaction Failed: Insufficient stock. Only {current_stock} left.")
            return
            
        # Calculate totals
        subtotal = price * quantity_purchased
        tax = subtotal * 0.18
        total_due = subtotal + tax
        
        # Update database
        new_stock = current_stock - quantity_purchased
        cursor.execute("UPDATE products SET stock_quantity = ? WHERE id = ?", (new_stock, product_id))
        
        conn.commit()
        print_receipt(name, price, quantity_purchased, subtotal, tax, total_due)
        
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()

def print_receipt(item_name, price, qty, subtotal, tax, total):
    print("\n" + "="*40)
    print("             CASH RECEIPT")
    print("="*40)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)
    print(f"Item: {item_name}")
    print(f"Price: ₹{price:.2f} x {qty}")
    print("-" * 40)
    print(f"Subtotal:     ₹{subtotal:.2f}")
    print(f"Tax (18%):    ₹{tax:.2f}")
    print("=" * 40)
    print(f"TOTAL DUE:    ₹{total:.2f}")
    print("=" * 40)
    print("       Thank you for shopping!\n")