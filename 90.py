"""XML 1 - Find the Score

https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=false

Task

You are given a valid XML document, and you have to print its score.
The score is calculated by the sum of the score of each element. For any element, the score is equal to the number of
attributes it has."""

import sys
import xml.etree.ElementTree as Etree


def get_attr_number(node):
    result = 0
    result += len(node.attrib)
    for child in node:
        result += get_attr_number(child)
    return result


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = Etree.ElementTree(Etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
