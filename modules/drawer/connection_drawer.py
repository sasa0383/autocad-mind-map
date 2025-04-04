class ConnectionDrawer:
    def __init__(self, modelspace, color_config):
        self.modelspace = modelspace
        self.color_config = color_config

    def draw_connection(self, parent_position, child_position, parent_height, child_height):
        """
        Draw a connection from the bottom edge of the parent to the top edge of the child.

        Args:
            parent_position (tuple): Center (x, y) of the parent node.
            child_position (tuple): Center (x, y) of the child node.
            parent_height (float): Height of the parent node.
            child_height (float): Height of the child node.
        """
        parent_bottom = (parent_position[0], parent_position[1] - parent_height / 2)
        child_top = (child_position[0], child_position[1] + child_height / 2)

        self.modelspace.add_line(
            start=parent_bottom,
            end=child_top,
            dxfattribs={"color": self.color_config.get_color("connection", 3)}
        )
