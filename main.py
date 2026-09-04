from modules.billing import process_transaction
from modules.inventory import view_all_products, add_new_product
from modules.reporting import export_inventory_to_csv
from modules.alerts import check_low_stock
from modules.search import search_product_by_name
from modules.restock import add_stock

def main():
    check_low_stock()
    
    while True:
        print("\n--- Retail Inventory System ---")
        print("1. Process a Sale")
        print("2. View All Inventory")
        print("3. Search Product by Name")
        print("4. Add New Product (Initial Setup)")
        print("5. Restock Existing Product")
        print("6. Export Inventory to CSV")
        print("7. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            try:
                pid = int(input("Enter Product ID: "))
                qty = int(input("Enter Quantity: "))
                process_transaction(pid, qty)
                check_low_stock()
            except ValueError:
                print("Error: Please enter valid numbers.")
                
        elif choice == '2':
            view_all_products()
            
        elif choice == '3':
            term = input("Enter product name to search: ")
            search_product_by_name(term)
            
        elif choice == '4':
            try:
                pid = int(input("Enter new Product ID: "))
                name = input("Enter Product Name: ")
                price = float(input("Enter Price: "))
                stock = int(input("Enter Initial Stock: "))
                add_new_product(pid, name, price, stock)
            except ValueError:
                print("Error: Invalid input format.")
                
        elif choice == '5':
            try:
                pid = int(input("Enter Product ID to restock: "))
                qty = int(input("Enter quantity received: "))
                add_stock(pid, qty)
            except ValueError:
                print("Error: Please enter valid numbers.")
                
        elif choice == '6':
            export_inventory_to_csv()
            
        elif choice == '7':
            print("Closing system.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()