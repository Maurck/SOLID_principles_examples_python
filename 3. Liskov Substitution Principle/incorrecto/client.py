from rectangle import Rectangle
from square import Square

class Client:

    def __init__(self):
        rectangle = Rectangle(5,2)
        square = Square(2)

        print(f'Area del rectangulo: {rectangle.get_area()}')
        square.set_width(5)
        print(f'Area del cuadrado: {square.get_area()}')

if __name__ == '__main__':
    client = Client()