from book import Book
from standart_output_printer import StandartOutputPrinter

class Client:
    def __init__(self):
        book = Book()
        current_page = book.get_current_page()
        printer = StandartOutputPrinter()
        printer.print_page(current_page)

if __name__ == '__main__':
    client = Client()
