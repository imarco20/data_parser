from parser_strategy import ParserStrategy
import csv
import os


class CsvParserStrategy(ParserStrategy):

    def parse(self, file):
        result = {}
        rows = []
        if os.path.exists(file):
            with open(file, "r") as data:
                for line in csv.DictReader(data):
                    rows.append(line)

            if "customer" in file.split("/")[-1].lower():
                result["customers"] = rows
            else:
                result["vehicles"] = rows

        return result
