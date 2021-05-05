import json

from json_converter_strategy import JsonConverterStrategy


class XmlJsonConverterStrategy(JsonConverterStrategy):

    def convert(self, data):
        return json.dumps(data[0])
