import os
import sqlite3

def ensure_schema(db_path):
    """
    Ensures the database schema is consistent.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # Ensure 'topics' table exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            level INTEGER NOT NULL
        )""")

        # Ensure 'relationships' table exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS relationships (
            parent_id INTEGER NOT NULL,
            child_id INTEGER NOT NULL,
            FOREIGN KEY (parent_id) REFERENCES topics(id),
            FOREIGN KEY (child_id) REFERENCES topics(id)
        )""")

if __name__ == "__main__":
    # Ensure the `data` directory exists
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "../data")
    os.makedirs(data_dir, exist_ok=True)

    # Set the database path
    db_path = os.path.join(data_dir, "tree_structure.db")

    # Ensure the schema
    ensure_schema(db_path)
    print(f"Schema ensured successfully at {db_path}.")
