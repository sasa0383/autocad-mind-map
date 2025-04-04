import matplotlib.pyplot as plt
import networkx as nx
from modules.node_loader import NodeLoader
from modules.node_positioner import NodePositioner
from modules.config_manager import ConfigLoader

# Load configurations
config_path = "config/config.json"
config_loader = ConfigLoader(config_path)

# Initialize database loader and positioner
db_path = "data/tree_structure.db"
node_loader = NodeLoader(db_path)
node_loader.load_data()

nodes = node_loader.get_nodes()
relationships = node_loader.get_relationships()

node_positioner = NodePositioner(config_loader)
positions = node_positioner.calculate_positions(nodes, relationships)

# Create a directed graph
graph = nx.DiGraph()

# Group nodes by level
levels = {}
for node in nodes:
    levels.setdefault(node.level, []).append(node)

# Adjust positions to ensure no overlap
adjusted_positions = {}
spacing_multiplier = 2.5  # Increase spacing multiplier for larger gaps
for level, level_nodes in levels.items():
    num_nodes = len(level_nodes)
    horizontal_spacing = config_loader.get("layout.horizontal_spacing", 100) * spacing_multiplier
    vertical_spacing = config_loader.get("layout.vertical_spacing", 50) * spacing_multiplier

    # Center nodes at this level
    x_start = -(num_nodes - 1) * horizontal_spacing / 2
    for i, node in enumerate(level_nodes):
        x = x_start + i * horizontal_spacing
        y = -level * vertical_spacing  # Negative to make root at the bottom
        adjusted_positions[node.name] = (x, y)

# Add nodes and positions to the graph
for node in nodes:
    graph.add_node(node.name, pos=adjusted_positions[node.name])

# Add edges
for parent_id, child_id in relationships:
    parent = next(node for node in nodes if node.id == parent_id)
    child = next(node for node in nodes if node.id == child_id)
    graph.add_edge(parent.name, child.name)

# Extract adjusted positions for visualization
pos = adjusted_positions

# Adjust text position offset to avoid overlap
label_pos = {name: (x, y + 10) for name, (x, y) in pos.items()}  # Offset text slightly above the nodes

# Dynamic font sizes for levels
base_font_size = 14
font_sizes = {node.name: max(base_font_size - node.level, 8) for node in nodes}  # Smaller font for deeper levels

# Calculate dynamic canvas size
max_x = max(x for x, y in pos.values())
min_x = min(x for x, y in pos.values())
max_y = max(y for x, y in pos.values())
min_y = min(y for x, y in pos.values())

# Adjust figure size dynamically based on graph size
canvas_width = (max_x - min_x) / 100 + 10  # Add padding
canvas_height = (max_y - min_y) / 100 + 10  # Add padding

plt.figure(figsize=(canvas_width, canvas_height))
nx.draw(
    graph,
    pos,
    node_size=2500,
    node_color="lightblue",
    with_labels=False,
    arrowsize=20
)

# Draw labels with dynamic font sizes
for node in nodes:
    nx.draw_networkx_labels(
        graph,
        {node.name: label_pos[node.name]},  # Position for the current label
        labels={node.name: node.name},
        font_size=font_sizes[node.name],  # Dynamic font size
        font_color="black",
        font_weight="bold"
    )

# Enable zooming and panning
plt.title("Node Position Visualization with Proper Y-Coordinates", fontsize=16)
plt.axis("off")
plt.show()
