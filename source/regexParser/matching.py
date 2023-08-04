def _match_backtrack(node, text, index):
    if not node:
        yield index
    elif node == "dot":
        if index < len(text):
            yield index+1
    elif isinstance(node, str):
        if index < len(text) and text[index] == node:
            yield index+1
    elif node[0] == "cat":
        yield from _match_backtrack_concat(node, text, index)
    elif node[0] == "split":
        yield from _match_backtrack(node[1], text, index)
        yield from _match_backtrack(node[2], text, index)
    elif node[0] == "repeat":
        yield from _match_backtrack_repeat(node, text, index)
    else:
        raise ValueError(f"Unknown instruction: {node[0]}!")

def _match_backtrack_concat(node, text, index):
    met = set()  # quick element present lookup, only unique elements
    for index_1 in _match_backtrack(node[1], text, index):
        if index_1 in met:
            continue  # duplication
        met.add(index_1)
        yield from _match_backtrack(node[2], text, index_1)

def _match_backtrack_repeat(node, text, index):
    _, node, rmin, rmax = node
    
    output = []
    if rmin == 0:
        output.append(index)
    start = {index}
    for i in range(1, rmax+1):
        found = set()
        for idx1 in start:
            for idx2 in _match_backtrack(node, text, idx1):
                found.add(idx2)
                if i >= rmin:
                    output.append(idx2)
            if not found:
                break
        start = found
    yield from reversed(output)

def match(node, text):
    if not text and not node:
        return True
    for index in _match_backtrack(node, text, 0):
        if index == len(text):
            return True
    return False