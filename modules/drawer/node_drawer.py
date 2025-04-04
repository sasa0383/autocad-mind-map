from ezdxf.enums import TextEntityAlignment

class NodeDrawer:
    def __init__(self, modelspace, color_config):
        self.modelspace = modelspace
        self.color_config = color_config
        self.node_width = 30  # Node rectangle width
        self.node_height = 10  # Node rectangle height

    def draw_container(self, node, x, y):
        print(f"Drawing container for node {node.id} at ({x}, {y})")  # Debugging
        x1, y1 = x - self.node_width / 2, y - self.node_height / 2
        x2, y2 = x + self.node_width / 2, y + self.node_height / 2
        self.modelspace.add_lwpolyline(
            [(x1, y1), (x2, y1), (x2, y2), (x1, y2)],
            close=True,
            dxfattribs={"color": self.color_config.get_color("node", 7)}
        )

    def draw_text(self, node, x, y):
        print(f"Drawing text for {node.name} at ({x}, {y})")  # Debugging
        self.modelspace.add_text(
            node.name,
            dxfattribs={"height": 2.5, "color": self.color_config.get_color("text", 5)}
        ).set_placement((x, y), align=TextEntityAlignment.MIDDLE_CENTER)
