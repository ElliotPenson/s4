from s4.app import match, is_html


def test_match():
    assert match("", ["", "red"]) == ""
    assert match("red", ["red"]) == "red"
    assert match("blue", ["blue"]) == "blue"
    assert match("red", ["red", "blue"]) == "red"
    assert match("yellow", ["blue", "yellow", "red"]) == "yellow"
    assert match("part", ["word part word", "pattern"]) == "word part word"


def test_is_html():
    assert not is_html("")
    assert not is_html("test")
    assert not is_html("test.txt")
    assert not is_html("path/test.txt")
    assert is_html("test.html")
    assert is_html("path/test.html")
    assert is_html("test.HTML")
