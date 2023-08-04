import regexParser.main as regex

def test_generic():
    """Test generic matching patterns"""
    assert regex.match("", "")
    assert regex.match("a", "a")
    
    assert regex.match("abcde", "ab.{3}")