from parser_strategy import ParserStrategy
import xml.etree.ElementTree as ElementTree


class XmlParserStrategy(ParserStrategy):

    def parse(self, file):
        result = {}

        root = ElementTree.parse(file).getroot()
        result[root.tag] = self.parse_node(root)

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
