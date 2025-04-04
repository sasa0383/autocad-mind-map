import unittest
from modules.node_manager import NodeManager
from modules.config_manager import ConfigLoader

class TestNodeManager(unittest.TestCase):
    def setUp(self):
        config = {"layout": {"horizontal_spacing": 100, "vertical_spacing": 50}}
        self.config_loader = ConfigLoader(config_path=None)
        self.config_loader.config_data = config  # Mock configuration
        self.manager = NodeManager(":memory:", self.config_loader)

    def test_calculate_positions(self):
        self.manager.load_data()
        positions = self.manager.calculate_positions()
        self.assertIsInstance(positions, dict)

if __name__ == "__main__":
    unittest.main()
