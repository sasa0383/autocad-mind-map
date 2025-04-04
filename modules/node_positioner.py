from .system import build_hierarchy  # Import coordinate logic
from .node import Node  # Assuming you already have the Node class

class NodePositioningAlgorithm:
    def __init__(self, nodes, relationships, dynamic_names):
        self.nodes = nodes
        self.relationships = relationships
        self.dynamic_names = dynamic_names



    def assign_positions_from_system(self):
        """Assign positions to nodes from system data."""
        print("Assigning positions to nodes from the system data...")
        for node in self.nodes:
            node_id = node.id
            if node_id in self.dynamic_names:
                node_data = self.dynamic_names[node_id]
                x = node_data.get('x', 0)
                y = node_data.get('y', 0)
                # Create a Postio object and set the node's position using it
                node.set_position(x, y)
                print(f"Position set for Node '{node.name}' (ID {node_id}): ({x}, {y})")
            else:
                print(f"Warning: No position data found for Node ID {node_id}.")

    def get_positioned_nodes(self):
        """
        Return nodes with updated positions.
        """
        return list(self.nodes.values())
