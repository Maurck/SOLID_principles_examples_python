from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, length_and_width):
        super().__init__(length_and_width, length_and_width)

    def set_length(self, length):
        self.length = length
        self.width = length

    def set_width(self, width):
        self.width = width
        self.length = width
