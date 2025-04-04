from typing import List

class Node:
    def __init__(self, id, name, level):
        """
        Initialize the Node with ID, optional name, level, and children.

        Args:
            id (int): Unique identifier for the node.
            name (str): Name of the node (default: None).
            level (int): Level in the hierarchy (default: 0 for root).
            children (list): List of child nodes (default: None).
        """
        self.id = id
        self.name = name
        self.level = level
        self.position = None
        

    def set_position(self, x, y):
        """
        Set the position of the node.

        Args:
            x (float): X-coordinate.
            y (float): Y-coordinate.
        """
        self.position = (x, y)
        self.x = x
        self.y = y

    def get_position(self):
        """
        Get the position of the node.

        Returns:
            tuple: (x, y) position of the node.
        """
        return self.position
        
       

    def add_child(self, child_node):
        """
        Add a child node to this node.

        Args:
            child_node (Node): The child node to be added.
        """
        self.children.append(child_node)