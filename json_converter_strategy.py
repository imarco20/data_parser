from abc import ABC, abstractmethod


class JsonConverterStrategy(ABC):

    @abstractmethod
    def convert(self, data):
        pass
