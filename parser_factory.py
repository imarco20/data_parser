from csv_parser_strategy import CsvParserStrategy
from xml_parser_strategy import XmlParserStrategy


class ParserFactory:

    @staticmethod
    def create_parser(format):

        if format == "csv":
            return CsvParserStrategy()

        elif format == "xml":
            return XmlParserStrategy()