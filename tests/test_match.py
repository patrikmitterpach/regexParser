import regexParser.main as regex


def test_generic():
    """Test generic matching patterns"""
    assert regex.match("", "")
    assert regex.match("a", "a")

    assert regex.match("abcde", "ab.{3}")

    # Wikipedia provided examples
    assert regex.match("Handel", "H(ä|ae?)ndel")
    assert regex.match("Händel", "H(ä|ae?)ndel")
    assert regex.match("Haendel", "H(ä|ae?)ndel")

    assert regex.match("gray", "gray|grey")
    assert regex.match("grey", "gray|grey")

    assert regex.match("grey", "gr(a|e)y")
    assert regex.match("grey", "gr(a|e)y")
