from block_type import * 

class Block:

    def __init__(self, color):
        self.color = color
        self.block_type = BlockType.get_block_type_from_color(color)
        self.orientation = self.block_type.default_orientation
        self.offset = self.block_type.default_offset

    def __repr__(self):
        return f"""Block Type: {self.block_type.name}, 
Color: {self.color.name}, 
Orientation: 
{self.orientation}, 
Offset: {self.offset}"""


