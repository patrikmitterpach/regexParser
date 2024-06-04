import regexParser.parsing as parsing
import regexParser.matching as matching
import regexParser.text_match as text

import sys


def parse(string: str):
    return parsing.parse(string)


def match(string: str, regex: str):
    parsed_regex = parsing.parse(regex)
    return matching.match(parsed_regex, string)


def matchText(path: str, pattern: str):
    return text.matchText(path, pattern)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        matchText("onShortnessOfLife.txt", sys.argv[1])
    elif len(sys.argv) == 3:
        matchText(sys.argv[2], sys.argv[1])
    else:
        matchText("onShortnessOfLife.txt", ".* ")