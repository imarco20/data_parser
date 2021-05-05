from csv_json_converter_strategy import CsvJsonConverterStrategy
from xml_json_converter import XmlJsonConverterStrategy


class JsonConverterFactory:

    @staticmethod
    def create_json_converter(format):
        if format == "xml":
            return XmlJsonConverterStrategy()

        elif format == "csv":
            return CsvJsonConverterStrategy()
