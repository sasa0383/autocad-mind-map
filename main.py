import os
from modules.node_manager import NodeManager
from modules.node_positioner import NodePositioningAlgorithm
from modules.drawer.document_manager import DocumentManager
from modules.drawer.node_drawer import NodeDrawer
from modules.drawer.connection_drawer import ConnectionDrawer
from modules.config_manager import ConfigLoader, ColorConfig
from modules.system import main as load_dynamic_names

def safe_call(obj, method_name, *args, **kwargs):
    """Call a method safely if it exists."""
    if hasattr(obj, method_name):
        method = getattr(obj, method_name)
        return method(*args, **kwargs)
    else:
        print(f"Warning: {method_name} is not implemented yet.")
        return None

def main():
    # Define paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "data", "tree_structure.db")
    config_path = os.path.join(base_dir, "config", "config.json")
    output_path = os.path.join(base_dir, "output", "output.dxf")

    # Load configurations
    config_loader = ConfigLoader(config_path)
    color_config = ColorConfig(config_loader)

    # Initialize NodeManager
    node_manager = NodeManager(db_path)
    node_manager.load_data()

    # Print loaded nodes and relationships
    print("Loaded Nodes:", [(node.id, node.name, node.level) for node in node_manager.nodes])
    print("Loaded Relationships:", node_manager.relationships)

    # Load dynamic names
    dynamic_names = load_dynamic_names()
    print("Loaded Dynamic Names:", dynamic_names)

    # Initialize NodePositioningAlgorithm
    positioner = NodePositioningAlgorithm(node_manager.nodes, node_manager.relationships, dynamic_names)

    # Assign positions from system
    print("Assigning positions from the system...")
    safe_call(positioner, 'assign_positions_from_system')

    # Create DXF document
    doc_manager = DocumentManager(output_path)
    msp = doc_manager.get_modelspace()

    # Initialize drawers
    node_drawer = NodeDrawer(msp, color_config)
    connection_drawer = ConnectionDrawer(msp, color_config)

    # Draw nodes
    print("Drawing nodes...")
    for node in node_manager.nodes:
        position = node.get_position()
        if position is None:
            print(f"Warning: Node '{node.name}' has no position set!")
            continue
        x, y = position
        node_drawer.draw_container(node, x, y)
        node_drawer.draw_text(node, x, y)
        print(f"Node '{node.name}' drawn at position ({x}, {y}).")

    # Draw connections
    print("Drawing connections...")
    for parent_id, child_id in node_manager.relationships:
        parent = node_manager.get_node_by_id(parent_id)
        child = node_manager.get_node_by_id(child_id)

        if not parent or not child:
            print(f"Warning: Missing parent ({parent_id}) or child ({child_id}) node!")
            continue

        parent_position = parent.get_position()
        child_position = child.get_position()

        if not parent_position or not child_position:
            print(f"Warning: Missing position for parent ({parent_id}) or child ({child_id})!")
            continue

        parent_height = node_drawer.node_height
        child_height = node_drawer.node_height

        connection_drawer.draw_connection(parent_position, child_position, parent_height, child_height)
        print(f"Connection drawn between Node {parent_id} and Node {child_id}.")

    # Save DXF document
    try:
        doc_manager.save_document()
        print(f"DXF file saved successfully at {output_path}.")
    except Exception as e:
        print(f"Error saving DXF document: {e}")

if __name__ == "__main__":
    main()
