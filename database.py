import sqlite3

DATABASE = "inventory.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_code TEXT UNIQUE,
            product_name TEXT NOT NULL,
            category TEXT,
            unit TEXT NOT NULL,
            purchase_price REAL DEFAULT 0,
            selling_price REAL DEFAULT 0,
            stock REAL DEFAULT 0,
            minimum_stock REAL DEFAULT 0
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_code TEXT,
            transaction_type TEXT,
            quantity REAL,
            unit_price REAL,
            party TEXT,
            remarks TEXT,
            date TEXT
        )
    """)

    conn.commit()
    conn.close()