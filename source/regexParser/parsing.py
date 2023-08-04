def parse(string):
    index, node = _parsing_split(string, 0)
    if index != len(string):
        raise Exception("Unexpected )!")
    return node


def _parsing_integer(string, index):
    start_point = index

    while index < len(string) and string[index].isdigit():
        index += 1
    return index, int(string[start_point:index]) if start_point != index else None


def _parsing_postfix(string: str, index: int, node: str):
    if index == len(string) or string[index] not in "*+{":
        return index, node

    character = string[index]
    index += 1

    if character == "*":
        rmin, rmax = 0, float("inf")
    if character == "+":
        rmin, rmax = 1, float("inf")
    else:
        index, i = _parsing_integer(string, index)
        if i is None:
            raise Exception("Integer expected!")
        rmin = rmax = i
        # Optional number of repetitions
        if index < len(string) and string[index] == ",":
            index, j = _parsing_integer(string, index + 1)
            rmax = j if j is not None else float("inf")
        if index < len(string) and string[index] == "}":
            index += 1
        else:
            raise Exception("Unbalanced braces")

    return index, ["repeat", node, rmin, rmax]


def _parsing_node(string: str, index: int):
    character = string[index]
    index += 1

    assert character not in ")|"

    if character == "(":
        index, node = _parsing_split(string, index)
        if index < len(string) and string[index] == ")":
            index += 1
        else:
            raise Exception("Unbalanced parentheses!")
    elif character == ".":
        node = "dot"
    elif character in "*+{":
        raise Exception("Nothing to repeat!")
    else:
        node = character
    index, node = _parsing_postfix(string, index, node)
    return index, node


def _parsing_concatenated(string: str, index: int):
    previous = None

    while index < len(string):
        if string[index] in ")|":
            break
        index, node = _parsing_node(string, index)
        if not previous:
            previous = node
        else:
            previous = ["cat", previous, node]  # type: ignore [unreachable]
    return index, previous


def _parsing_split(string: str, index: int):
    index, previous = _parsing_concatenated(string, index)

    while index < len(string):
        if string[index] == ")":
            break
        assert string[index] == "|", "BUG"
        index, node = _parsing_concatenated(string, index + 1)
        previous = ["split", previous, node]
    return index, previous
