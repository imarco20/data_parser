import sys

from json_converter_factory import JsonConverterFactory
from parser_factory import ParserFactory


def main(argv):
    # TODO: Try Except
    format = argv[0]
    files = argv[1:]

    parser = ParserFactory.create_parser(format)

    data = []

    for file in files:
        data.append(parser.parse(file))

    converter = JsonConverterFactory.create_json_converter(format)
    return converter.convert(data)


if __name__ == "__main__":
    result = main(sys.argv[1:])
    print(result)
