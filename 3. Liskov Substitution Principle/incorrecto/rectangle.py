
class Rectangle:
    width=1
    length=1
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width
    
    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def get_area(self) -> float:
        return self.length * self.width
        