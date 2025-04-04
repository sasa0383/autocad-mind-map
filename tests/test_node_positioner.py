import unittest
from modules.node import Node
from modules.node_positioner import NodePositioner
from modules.config_manager import ConfigLoader
import sys
import os

class TestNodePositioner(unittest.TestCase):
    def setUp(self):
        config = {"layout": {"horizontal_spacing": 100, "vertical_spacing": 50}}
        self.config_loader = ConfigLoader(config_path=None)
        self.config_loader.config_data = config  # Mock configuration
        self.positioner = NodePositioner(self.config_loader)

    def test_calculate_positions(self):
        # Mock nodes
        nodes = [
            Node(1, "Root", 0),
            Node(2, "Child1", 1),
            Node(3, "Child2", 1),
            Node(4, "Leaf1", 2),
            Node(5, "Leaf2", 2)
        ]
        # Mock relationships
        relationships = [
            (1, 2), (1, 3),
            (2, 4), (2, 5)
        ]

        positions = self.positioner.calculate_positions(nodes, relationships)

        # Assertions
        self.assertEqual(positions[4], (0, -100))  # Leaf1
        self.assertEqual(positions[5], (100, -100))  # Leaf2
        self.assertEqual(positions[2], (50, -50))  # Child1
        self.assertEqual(positions[1], (50, 0))  # Root

if __name__ == "__main__":
    unittest.main()
