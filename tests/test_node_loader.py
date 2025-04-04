import unittest
from unittest.mock import MagicMock
from modules.node_loader import NodeLoader

class TestNodeLoader(unittest.TestCase):
    def setUp(self):
        self.mock_db_path = ":memory:"
        self.loader = NodeLoader(self.mock_db_path)

    def test_load_data(self):
        # Mock data insertion
        self.loader.node_loader = MagicMock()
        self.loader.node_loader.return_value = [("1", "Root", 0)]
        self.loader.load_data()

        self.assertIsNotNone(self.loader.get_nodes())

if __name__ == "__main__":
    unittest.main()

import sys
import os
import unittest
from modules.node_loader import NodeLoader

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestNodeLoader(unittest.TestCase):
    def test_print_level1_nodes(self):
        db_path = "d:/my code/autocad/new mind map/project3/data/tree_structure.db"
        loader = NodeLoader(db_path)
        loader.load_data()

        print("Level 1 Nodes:")
        for node in loader.get_nodes():
            if node.level == 1:
                print(f"ID: {node.id}, Name: {node.name}, Level: {node.level}")

if __name__ == "__main__":
    unittest.main()
