import json
import sys
import os

from json_converter_factory import JsonConverterFactory
from parser_factory import ParserFactory


def main(argv):
    try:
        format = argv[0]
    except IndexError:
        print("You didn't specify a data format. Please choose either CSV or XML")
        sys.exit()

    try:
        files = argv[1:]
    except IndexError:
        print(
            "Not enough arguments. Please specify a valid format, and file(s) that you want to parse and convert to JSON.")
        sys.exit()

    if format in ["csv", "xml"]:
        parser = ParserFactory.create_parser(format)
    else:
        print(
            "The specified format is either an invalid format or one that we don't support. We currently support CSV and XML formats only.")
        sys.exit()

    data = []

    for file in files:
        data.append(parser.parse(file))

    converter = JsonConverterFactory.create_json_converter(format)

    current_directory = os.path.dirname(os.path.realpath(__file__))
    parsing_directory = current_directory + "/parsing_result"

    if not os.path.exists(parsing_directory):
        os.mkdir(parsing_directory)

    json_file_path = os.path.join(parsing_directory, 'sample.json')

    with open(json_file_path, 'w') as f:
        json.dump(converter.convert(data), f)


if __name__ == "__main__":
    main(sys.argv[1:])
