"""HTML Parser - Part 1

https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=false

Task

You are given an HTML code snippet of n lines.
Your task is to print start tags, end tags and empty tags separately."""


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for t in attrs:
            print(f"-> {t[0]} > {t[1]}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for t in attrs:
            print(f"-> {t[0]} > {t[1]}")


if __name__ == "__main__":
    parser = MyHTMLParser()
    for _ in range(int(input())):
        parser.feed(input())
