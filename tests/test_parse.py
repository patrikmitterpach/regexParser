import regexParser.main as regex


def test_generic():
    """Test generic character parsing"""
    assert regex.parse("") is None

    assert regex.parse("a") == "a"
    assert regex.parse("b") == "b"
    assert regex.parse("c") == "c"

    assert regex.parse("0") == "0"
    assert regex.parse("2") == "2"
    assert regex.parse("7") == "7"

    assert regex.parse("_") == "_"
    assert regex.parse("#") == "#"
    assert regex.parse("%") == "%"
    assert regex.parse("\\") == "\\"


def test_dots():
    """Test the correct parsing of the dot character"""
    assert regex.parse(".") == "dot"


def test_cat():
    """Test the concatanation of multiple characters"""
    assert regex.parse("ab") == ["cat", "a", "b"]
    assert regex.parse("cdd") == ["cat", ["cat", "c", "d"], "d"]
    assert regex.parse("...") == ["cat", ["cat", "dot", "dot"], "dot"]

    assert regex.parse("a+") == ["repeat", "a", 1, 60]
    assert regex.parse("a{3,6}") == ["repeat", "a", 3, 6]


def test_split():
    """Test the '|' character parsing"""
    assert regex.parse("a|b") == ["split", "a", "b"]

    assert regex.parse("a|bc") == ["split", "a", ["cat", "b", "c"]]
    assert regex.parse("(a|b)c") == ["cat", ["split", "a", "b"], "c"]
