import sqlite3
import csv
import os

def get_db_connection():
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'inventory.db')
    return sqlite3.connect(db_path)

def export_inventory_to_csv():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, price, stock_quantity FROM products")
    products = cursor.fetchall()
    
    # Creates the CSV file in the root folder
    export_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'inventory_report.csv')
    
    with open(export_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Product ID', 'Product Name', 'Price (INR)', 'Stock Quantity'])  # Headers
        writer.writerows(products)
        
    print(f"\nSuccess: Inventory exported to {export_path}")
    conn.close()