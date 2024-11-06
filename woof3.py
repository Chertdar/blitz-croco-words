def is_valid(words: str) -> bool:
    return words.isalpha()


def test():
    assert is_valid('') == False
    assert is_valid(' ') == False
    assert is_valid('0') == False
    assert is_valid('.') == False
    assert is_valid('слово') == True
