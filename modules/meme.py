import sqlite3
import matplotlib.pyplot as plt
import networkx as nx

DB_PATH = "D:/my code/autocad/new mind map/project3/data/tree_structure.db"

def fetch_data():
    """Fetch topics and relationships from the database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Fetch topics
        cursor.execute("SELECT id, name, level FROM topics")
        topics = cursor.fetchall()

        # Fetch relationships
        cursor.execute("SELECT parent_id, child_id FROM relationships")
        relationships = cursor.fetchall()

        conn.close()
        return topics, relationships
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return [], []

def build_positions(topics, relationships):
    """Dynamically position nodes in a zigzag flowchart starting bottom-up."""
    G = nx.DiGraph()
    node_levels = {node_id: level for node_id, _, level in topics}
    node_names = {node_id: name for node_id, name, _ in topics}
    parent_map = {child: parent for parent, child in relationships}

    # Initialize positions
    pos = {}
    visited = set()

    def position_node(node_id, x, y):
        """Recursively position nodes in zigzag flow."""
        if node_id in visited:
            return
        visited.add(node_id)

        # Position current node
        pos[node_id] = (x, y)

        # Process siblings
        siblings = [child for parent, child in relationships if parent_map.get(child) == parent_map.get(node_id)]
        siblings.sort()  # Sort siblings by ID for consistent order
        sibling_index = siblings.index(node_id)

        # Place siblings horizontally
        spacing = 50
        x_sibling = x + (sibling_index - len(siblings) // 2) * spacing
        pos[node_id] = (x_sibling, y)

        # Move to mother (parent node)
        parent_id = parent_map.get(node_id)
        if parent_id:
            parent_x = sum(pos[child][0] for child in siblings) / len(siblings)
            parent_y = y + 100  # Move up one level
            position_node(parent_id, parent_x, parent_y)

        # Left-to-right zigzag for neighbors
        for sibling in siblings:
            if sibling != node_id and sibling not in visited:
                position_node(sibling, x_sibling + spacing, y)

        # Process children of the current node
        children = [child for parent, child in relationships if parent == node_id]
        for i, child_id in enumerate(children):
            child_x = x_sibling - (len(children) // 2 - i) * spacing
            position_node(child_id, child_x, y - 100)  # Move down one level

    # Start from the first node at the lowest level
    lowest_level = max(node_levels.values())
    first_node = min([node for node, level in node_levels.items() if level == lowest_level])
    position_node(first_node, 0, 0)

    return G, pos, node_names

def draw_flowchart(G, pos, node_names):
    """Draw the zigzag dynamic flowchart."""
    plt.figure(figsize=(12, 8))
    labels = {node: node_names.get(node, str(node)) for node in G.nodes()}
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color="lightgreen", font_size=8, font_weight="bold")
    plt.title("Dynamic Zigzag Tree Flowchart")
    plt.show()

def main():
    """Main execution."""
    topics, relationships = fetch_data()
    if not topics or not relationships:
        print("No data found in the database.")
        return

    G = nx.DiGraph()
    for parent, child in relationships:
        G.add_edge(parent, child)

    G, pos, node_names = build_positions(topics, relationships)
    draw_flowchart(G, pos, node_names)

if __name__ == "__main__":
    main()
