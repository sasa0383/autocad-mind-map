import sqlite3
from .node import Node  # Ensure Node is imported correctly


class NodeLoader:
    def __init__(self, db_path):
        """
        Initialize the NodeLoader with the database path.

        Args:
            db_path (str): Path to the SQLite database.
        """
        self.db_path = db_path
        self.nodes = []
        self.relationships = []

    def load_data(self):
        """
        Load nodes and relationships from the database.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Load nodes
            cursor.execute("SELECT id, name, level FROM topics")
            self.nodes = [Node(id=row[0], name=row[1], level=row[2]) for row in cursor.fetchall()]

            # Load relationships
            cursor.execute("SELECT parent_id, child_id FROM relationships")
            self.relationships = cursor.fetchall()

        print("Loaded Nodes:", [(node.id, node.name, node.level) for node in self.nodes])  # Debugging
        print("Loaded Relationships:", self.relationships)  # Debugging

    def get_nodes(self):
        """
        Get the list of nodes.

        Returns:
            list: List of Node objects.
        """
        return self.nodes

    def get_relationships(self):
        """
        Get the relationships.

        Returns:
            list: List of (parent_id, child_id) tuples.
        """
        return self.relationships




