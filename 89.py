"""Detect HTML Tags, Attributes and Attribute Values

https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=false

Input Format

The first line contains an integer n, the number of lines in the HTML code snippet.
The next n lines contain HTML code.

Output Format

Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet."""


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for item in attrs:
            print(f"-> {item[0]} > {item[1]}")


if __name__ == "__main__":
    parser = MyHTMLParser()
    for _ in range(int(input())):
        parser.feed(input())
