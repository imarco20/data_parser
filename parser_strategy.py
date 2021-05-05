from abc import ABC, abstractmethod


class ParserStrategy(ABC):

    @abstractmethod
    def parse(self, file):
        pass
