import json
import os

class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config_data = self.load_config()

    def load_config(self):
        """
        Load configuration data from JSON file.

        Returns:
            dict: Configuration data.
        """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        with open(self.config_path, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        """
        Get configuration value for a given key.

        Args:
            key (str): Key to lookup.
            default: Default value if key not found.

        Returns:
            Value associated with the key or default.
        """
        return self.config_data.get(key, default)

class ColorConfig:
    def __init__(self, config_loader):
        self.config_loader = config_loader

    def get_color(self, item, default=7):
        """
        Get the color configuration for a specific item.

        Args:
            item (str): Item name.
            default (int): Default color if not found.

        Returns:
            int: Color code.
        """
        return self.config_loader.get(f"colors.{item}", default)
