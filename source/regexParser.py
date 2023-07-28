import source.parsing as parsing
import source.matching as matching

def parse(string: str):
    return parsing.parse(string)

def match(string: str, regex: str):
    return matching.match(parsing.parse(regex), string)