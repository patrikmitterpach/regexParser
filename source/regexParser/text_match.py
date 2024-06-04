import regexParser.parsing as parsing
import regexParser.matching as matching

def matchLine(line: str, pattern: str):
    out_line = line
    start_idx = 0
    while start_idx < len(line):
        run_idx = start_idx+1
        while run_idx < len(line):
            parsed_regex = parsing.parse(pattern)
            current_match = "".join(list(line)[start_idx:run_idx])
            if matching.match(parsed_regex, current_match):
                out_line = out_line.replace(current_match, "\033[;1;31m" + current_match + "\033[0m", 1) 
                print(out_line)
                return
            run_idx += 1
        start_idx += 1
    return

def matchText(path: str, pattern: str):
    with open(path, encoding="utf-8") as file:
        full_text = file.read().split('\n')

    for line in full_text:
        matchLine(line, pattern)
        
        