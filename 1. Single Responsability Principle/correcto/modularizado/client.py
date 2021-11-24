from book import Book
from standart_output_printer import StandartOutputPlainPrinter
from standart_output_html_printer import StandartOutputHtmlPrinter

class Client:
    def __init__(self):
        book = Book()
        current_page = book.get_current_page()

        plain_printer = StandartOutputPlainPrinter()
        plain_printer.print_page(current_page)

        html_printer = StandartOutputHtmlPrinter()
        html_printer.print_page(current_page)

if __name__ == '__main__':
    client = Client()
