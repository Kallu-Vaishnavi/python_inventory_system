# Retail Inventory & Billing System 🛒

When I first started writing Python, my projects existed entirely in the terminal and vanished the second I hit `Ctrl+C`. I wanted to build something tangible—a tool that a local shop owner could actually use to run their day-to-day business.

This project is a lightweight, fully functional Point of Sale (POS) and inventory manager. It steps away from purely academic coding to solve real-world problems: managing live stock levels, preventing you from selling inventory you don't have, and safely persisting all data using a local database.

## 💡 What It Actually Does

* **Real-Time Checkout:** No manual math required. It takes the product, calculates the total with taxes, prints a clean text-based receipt, and instantly removes the item from your live inventory.
* **The "Low Stock" Lifesaver:** Every time you boot up the system, it scans your database. If you are down to your last few items, it triggers a warning so you can reorder before a customer gets turned away.
* **Frictionless Search:** Because nobody remembers a 5-digit product ID. You can search your catalog by typing partial names, then easily update the counts when a new delivery truck arrives.
* **Dashboard Ready:** With one keystroke, it pulls your raw database tables and exports them into a clean `.csv` file, making it incredibly easy to plug into Excel or Power BI to visualize your daily revenue.

## 🛠️ How It Was Built

I specifically avoided dumping hundreds of lines of code into a single file. The architecture is modular so it's easy to read, debug, and expand.

| Component | What I Used | Why I Chose It |
| --- | --- | --- |
| **Language** | Python 3 | Clean syntax and handles data manipulation effortlessly. |
| **Database** | SQLite3 | Built directly into Python. No heavy server setup or passwords required for whoever downloads this repo. |
| **Architecture** | Modular Scripts | Separating the billing logic from the database setup makes it function like a real enterprise application. |

## 📂 The File Structure

```text
retail_inventory_system/
├── database/
│   └── db_setup.py        # Run this once to build the database and tables!
├── modules/
│   ├── alerts.py          # The script that yells (nicely) when stock is low
│   ├── billing.py         # Handles the cash register math and receipts
│   ├── inventory.py       # Let's you view the catalog and add new items
│   ├── reporting.py       # Pushes data to CSV for analytics
│   ├── restock.py         # For updating counts when shipments arrive
│   └── search.py          # The text-based search engine
├── main.py                # The central menu that ties everything together
└── README.md              

```

## 🚀 How to Run It on Your Machine

1. **Download the Code:** Clone this repo and open the folder in your favorite editor (I use VS Code).
2. **Build the Database:** Open your terminal and run `python database/db_setup.py`. This generates the `inventory.db` file and adds a sample product to get you started.
3. **Start Selling:** Run `python main.py` to launch the interactive terminal menu and try processing your first transaction!
