from abc import ABC
from abc import abstractmethod

class Mesurable(ABC):
    @abstractmethod
    def get_total_length(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_sent_length(self) -> float:
        raise NotImplementedError

    def get_length_percentage(self):
        return self.get_sent_length() * 100 / self.get_total_length()