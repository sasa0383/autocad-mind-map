import unittest
from unittest.mock import MagicMock
from modules.drawer.node_drawer import NodeDrawer
from modules.config_manager import ConfigLoader
from modules.node import Node

class TestNodeDrawer(unittest.TestCase):
    def setUp(self):
        self.mock_modelspace = MagicMock()
        config = {"colors": {"node": 7, "text": 5}}
        self.config_loader = ConfigLoader(config_path=None)
        self.config_loader.config_data = config  # Mock configuration
        self.drawer = NodeDrawer(self.mock_modelspace, self.config_loader)

    def test_draw_container(self):
        node = Node(1, "TestNode", 0)
        self.drawer.draw_container(node, 50, 50)

        # Assert rectangle was added
        self.mock_modelspace.add_lwpolyline.assert_called_once()

    def test_draw_text(self):
        node = Node(1, "TestNode", 0)
        self.drawer.draw_text(node, 50, 50)

        # Assert text was added
        self.mock_modelspace.add_text.assert_called_once_with(
            "TestNode",
            dxfattribs={"height": 2.5, "color": 5}
        )

if __name__ == "__main__":
    unittest.main()
