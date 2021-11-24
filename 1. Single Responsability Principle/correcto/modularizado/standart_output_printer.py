from printer import Printer

class StandartOutputPlainPrinter(Printer):
    def print_page(self, page):
        print(page)