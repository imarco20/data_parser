import json

from json_converter_strategy import JsonConverterStrategy


class CsvJsonConverterStrategy(JsonConverterStrategy):

    def convert(self, data):

        if data[0].get("customers"):
            customers = data[0]["customers"]
            vehicles = data[1]["vehicles"]
        else:
            vehicles = data[0]["vehicles"]
            customers = data[1]["customers"]

        for customer in customers:
            for vehicle in vehicles:
                if customer["id"] == vehicle["owner_id"]:
                    customer["vehicles"] = customer.get("vehicles", [])
                    customer["vehicles"].append(vehicle)

        return json.dumps(customers)
