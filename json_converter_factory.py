from json_converter import XmlJsonConverterStrategy, CsvJsonConverterStrategy


class JsonConverterFactory:

    @staticmethod
    def create_json_converter(format):
        if format == "xml":
            return XmlJsonConverterStrategy()

        elif format == "csv":
            return CsvJsonConverterStrategy()
