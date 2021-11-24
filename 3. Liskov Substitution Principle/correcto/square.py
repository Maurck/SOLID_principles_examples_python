from figure import Figure

class Square(Figure):
    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side

    def get_area(self) -> float:
        return self.side * self.side
