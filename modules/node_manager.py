import sqlite3

from.node import Node
from .node_positioner import NodePositioningAlgorithm

class NodeManager:
    def __init__(self, db_path):
        """
        Initialize the NodeManager with the database path.

        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path
        self.nodes = []
        self.relationships = []

    def load_data(self):
        """Load nodes and relationships from the database."""
        self.nodes = self.load_nodes_from_db()
        self.relationships = self.load_relationships_from_db()

    def load_nodes_from_db(self):
        """Load nodes from the `topics` table in the database."""
        nodes = []
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Query to fetch all nodes
            cursor.execute("SELECT id, name, level FROM topics")
            rows = cursor.fetchall()

            for row in rows:
                node_id, name, level = row
                nodes.append(Node(node_id, name, level))

            conn.close()
        except sqlite3.Error as e:
            print(f"Error loading nodes from database: {e}")
        return nodes

    def load_relationships_from_db(self):
        """Load relationships from the `relationships` table in the database."""
        relationships = []
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Query to fetch all relationships
            cursor.execute("SELECT parent_id, child_id FROM relationships")
            rows = cursor.fetchall()

            relationships.extend(rows)
            conn.close()
        except sqlite3.Error as e:
            print(f"Error loading relationships from database: {e}")
        return relationships

    def get_node_by_id(self, node_id):
        """Get a node by its ID."""
        return next((node for node in self.nodes if node.id == node_id), None)
