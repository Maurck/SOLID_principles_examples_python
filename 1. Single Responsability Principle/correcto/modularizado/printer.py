import abc
class Printer(abc.ABC):

    @abc.abstractmethod
    def print_page(self, page):
        raise NotImplementedError