from printer import Printer

class StandartOutputHtmlPrinter(Printer):
    def print_page(self, page):
        print("<div>" + page + "</div>")