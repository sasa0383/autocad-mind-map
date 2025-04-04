import sqlite3

class Serializer:
    def __init__(self, db_path):
        """
        Initialize the Serializer with the database path.

        Args:
            db_path (str): Path to the SQLite database.
        """
        self.db_path = db_path

    def execute_query(self, query, params=None):
        """
        Executes a query on the database.

        Args:
            query (str): SQL query string.
            params (tuple): Query parameters.

        Returns:
            list: Query results.
        """
        params = params or ()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchall()

    def save_node(self, node_id, name, level):
        """
        Save a node to the database.

        Args:
            node_id (int): Node ID.
            name (str): Node name.
            level (int): Node level.
        """
        query = "INSERT INTO topics (id, name, level) VALUES (?, ?, ?)"
        self.execute_query(query, (node_id, name, level))

    def save_relationship(self, parent_id, child_id):
        """
        Save a parent-child relationship to the database.

        Args:
            parent_id (int): Parent node ID.
            child_id (int): Child node ID.
        """
        query = "INSERT INTO relationships (parent_id, child_id) VALUES (?, ?)"
        self.execute_query(query, (parent_id, child_id))

    def get_all_nodes(self):
        """
        Retrieve all nodes from the database.

        Returns:
            list: List of nodes.
        """
        query = "SELECT id, name, level FROM topics"
        return self.execute_query(query)

    def get_all_relationships(self):
        """
        Retrieve all relationships from the database.

        Returns:
            list: List of relationships.
        """
        query = "SELECT parent_id, child_id FROM relationships"
        return self.execute_query(query)
