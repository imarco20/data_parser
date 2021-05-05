import json
from abc import ABC, abstractmethod
from collections import defaultdict


class JsonConverterStrategy(ABC):

    @abstractmethod
    def convert(self, data):
        pass


class CsvJsonConverterStrategy(JsonConverterStrategy):

    def convert(self, data):

        if data[0].get("customers"):
            customers = data[0]["customers"]
            vehicles = data[1]["vehicles"]
        else:
            vehicles = data[0]["vehicles"]
            customers = data[1]["customers"]

        vehicles_dict = defaultdict(list)

        for vehicle in vehicles:
            vehicles_dict[vehicle["owner_id"]].append(vehicle)

        for customer in customers:
            customer["vehicles"] = vehicles_dict.get(customer["id"])

        return json.dumps(customers)


class XmlJsonConverterStrategy(JsonConverterStrategy):

    def convert(self, data):
        return json.dumps(data[0])
