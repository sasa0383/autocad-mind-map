import unittest
from unittest.mock import MagicMock
from modules.drawer.connection_drawer import ConnectionDrawer
from modules.config_manager import ConfigLoader

class TestConnectionDrawer(unittest.TestCase):
    def setUp(self):
        self.mock_modelspace = MagicMock()
        config = {"colors": {"connection": 3}}
        self.config_loader = ConfigLoader(config_path=None)
        self.config_loader.config_data = config  # Mock configuration
        self.drawer = ConnectionDrawer(self.mock_modelspace, self.config_loader)

    def test_draw_connection(self):
        # Mock positions
        parent_position = (50, 50)
        child_position = (100, 100)

        self.drawer.draw_connection(parent_position, child_position)

        # Assert line was added
        self.mock_modelspace.add_line.assert_called_with(
            parent_position,
            child_position,
            dxfattribs={"color": 3}
        )

if __name__ == "__main__":
    unittest.main()
