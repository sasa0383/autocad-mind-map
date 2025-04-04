import sqlite3
import pandas as pd

# Constants
DB_PATH = "data/tree_structure.db"
OUTPUT_PATH = "D:/my code/autocad/new mind map/project3/output/node_hierarchy.xlsx"

HORIZONTAL_DISTANCE = 50  # Base horizontal distance
VERTICAL_DISTANCE = -30     # Vertical spacing between levels


def fetch_data():
    """Fetch data from the database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, level FROM topics")
        topics = cursor.fetchall()

        cursor.execute("SELECT parent_id, child_id FROM relationships")
        relationships = cursor.fetchall()

        conn.close()
        return topics, relationships
    except Exception as e:
        print(f"Database Error: {e}")
        return [], []


def build_hierarchy(topics, relationships):
    """Build a tree structure and calculate coordinates."""
    nodes = {node[0]: {"name": node[1], "level": node[2], "children": [], "x": None, "y": None} for node in topics}

    # Build parent-child relationships
    for parent, child in relationships:
        nodes[parent]["children"].append(child)

    # Position nodes
    x_offset = [0]  # Track the x-coordinate offset
    def position_node(node_id, depth=0):
        node = nodes[node_id]
        node["y"] = depth * VERTICAL_DISTANCE  # Set y-coordinate based on depth

        # Position child nodes
        children = node["children"]
        if children:
            for child in children:
                position_node(child, depth + 1)
            # Center parent node
            node["x"] = (nodes[children[0]]["x"] + nodes[children[-1]]["x"]) // 2
        else:
            # Leaf nodes get sequential x-coordinates
            node["x"] = x_offset[0]
            x_offset[0] += HORIZONTAL_DISTANCE

    # Find root node
    root_id = find_root_node(relationships)
    if root_id:
        position_node(root_id)

    return nodes


def find_root_node(relationships):
    """Find the root node without a parent."""
    all_children = {child for _, child in relationships}
    all_parents = {parent for parent, _ in relationships}
    root_candidates = all_parents - all_children
    return next(iter(root_candidates), None)


def export_to_excel(node_data):
    """Export data to Excel with updated coordinates."""
    rows = [
        {
            "Node ID": node_id,
            "Name": data["name"],
            "Level": data["level"],
            "X-coordinate": data["x"],
            "Y-coordinate": data["y"]
        }
        for node_id, data in node_data.items()
    ]
    df = pd.DataFrame(rows)
    df.to_excel(OUTPUT_PATH, index=False)
    print(f"Excel exported to {OUTPUT_PATH}")


def main():
    topics, relationships = fetch_data()
    if not topics or not relationships:
        print("No data found.")
        return

    node_data = build_hierarchy(topics, relationships)
    export_to_excel(node_data)
    return node_data


if __name__ == "__main__":
    main()
