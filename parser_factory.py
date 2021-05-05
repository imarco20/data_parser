from data_parser import CsvParserStrategy, XmlParserStrategy


class ParserFactory:

    @staticmethod
    def create_parser(format):

        if format == "csv":
            return CsvParserStrategy()

        elif format == "xml":
            return XmlParserStrategy()
