import csv
import os
import xml.etree.ElementTree as ElementTree
from abc import ABC, abstractmethod


class ParserStrategy(ABC):

    @abstractmethod
    def parse(self, file):
        pass


class CsvParserStrategy(ParserStrategy):

    def parse(self, file):
        result = {}
        rows = []
        if os.path.exists(file):
            try:
                with open(file, "r") as data:
                    for line in csv.DictReader(data):
                        rows.append(line)

                if "customer" in file.split("/")[-1].lower():
                    result["customers"] = rows
                else:
                    result["vehicles"] = rows
            except UnicodeDecodeError:
                print("The entered file isn't a proper CSV file. Please its source.")

        return result


class XmlParserStrategy(ParserStrategy):

    def parse(self, file):
        result = {}

        try:
            root = ElementTree.parse(file).getroot()
            result[root.tag] = self.parse_node(root)
        except ElementTree.ParseError:
            print("The entered file isn't a valid XML one. Please check the source of your file")

        return result

    def parse_node(self, node):
        result = {}

        for item in node.items():
            result[item[0]] = item[1]

        if not node.getchildren():
            return node.text

        for child in node.getchildren():
            result[child.tag] = self.parse_node(child)

        return result
