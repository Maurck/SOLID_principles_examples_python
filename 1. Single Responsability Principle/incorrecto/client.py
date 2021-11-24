from book import Book

# No se respeta el Single Responsability Principle debido a que la clase Book está acoplada al canal estandar de salida:  "print()"
class Client:
    def __init__(self):
        book =  Book()
        book.print_current_page()

if __name__ == '__main__':
    client = Client()