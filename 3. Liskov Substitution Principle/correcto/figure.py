import abc

class Figure(abc.ABC):
    @abc.abstractmethod
    def get_area() -> float:
        raise NotImplementedError