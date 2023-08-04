import regexParser.parsing as parsing
import regexParser.matching as matching

def parse(string: str):
    return parsing.parse(string)

def match(string: str, regex: str):
    parsed_regex = parsing.parse(regex)
    return matching.match(parsed_regex, string)