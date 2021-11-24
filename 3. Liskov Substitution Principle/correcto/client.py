from rectangle import Rectangle
from square import Square

class Client:
    def __init__(self):
        rectangle = Rectangle(5,2)
        square = Square(5)

        print(f'Area del rectangulo: {rectangle.get_area()}')
        print(f'Area del cuadrado: {square.get_area()}')
        

if __name__ == '__main__':
    client = Client()
