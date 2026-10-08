import sqlite3

DB_FILE = "store.db"


def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row   # lets us read columns by name: row["name"]
    return conn


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT    NOT NULL,
            price INTEGER NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    # Add starting products only if the table is empty
    count = conn.execute("SELECT COUNT(*) FROM products").fetchone()[0]
    if count == 0:
        conn.executemany(
            "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
            [
                ("Rice 5kg", 10000, 20),
                ("Beans 5kg", 8000, 20),
                ("Palm Oil 5L", 15000, 10),
            ],
        )

    conn.commit()
    conn.close()