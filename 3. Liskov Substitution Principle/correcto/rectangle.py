from typing import _SpecialForm
from figure import Figure

class Rectangle(Figure):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def set_width(self, width):
        self.width = width

    def set_length(self, length):
        self.length = length    

    def get_area(self) -> float:
        return self.width * self.length
