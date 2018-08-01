import pytest
from missing_alphabet import insert_missing_letters as missing 


def test_type():
    with pytest.raises(TypeError):
        missing(['a', 'b', 'cde', 'ff'])


def test_type_2():
    with pytest.raises(TypeError):
        missing('1')


def test_simple_string():
    assert missing('hl') == 'hIJKMNOPQRSTUVWXYZlMNOPQRSTUVWXYZ'


def test_string_with_duplicates():
    assert missing('clvvdfaqego') == 'cHIJKMNPRSTUWXYZlMNPRSTUWXYZvWXYZvdHIJKMNPRSTUWXYZfHIJKMNPRSTUWXYZaBHIJKMNPRSTUWXYZqRSTUWXYZeHIJKMNPRSTUWXYZgHIJKMNPRSTUWXYZoPRSTUWXYZ'


def test_sting_with_caps_and_characters():
    assert missing('clVvdfaqego') == 'cHIJKMNPRSTUWXYZlMNPRSTUWXYZvWXYZvdHIJKMNPRSTUWXYZfHIJKMNPRSTUWXYZaBHIJKMNPRSTUWXYZqRSTUWXYZeHIJKMNPRSTUWXYZgHIJKMNPRSTUWXYZoPRSTUWXYZ'


def test_sting_one():
    assert missing('uebaknintapehzbeozgjjhotlnklqqvccvhatltmsndog') == 'uWXYeFRWXYbFRWXYaFRWXYkRWXYnRWXYiRWXYntWXYapRWXYehRWXYzbeoRWXYzgRWXYjRWXYjhotlRWXYnklqRWXYqvWXYcFRWXYcvhatltmRWXYsWXYndFRWXYog'


def test_sting_two():
    assert missing('grnxufqvrbjhulpgktjresglvrxzumgtlfqbplhvbd') == 'gIOWYrWYnOWYxYuWYfIOWYqWYvWYrbCIOWYjOWYhIOWYulOWYpWYgkOWYtWYjreIOWYsWYglvrxzumOWYgtlfqbplhvbdIOWY'


def test_sting_thee():
    assert missing('hjapfxwjdilgukvzxeemuzubdrodqkqizfhlepujttwegb') == 'hNSYjNSYaCNSYpSYfNSYxYwYjdNSYiNSYlNSYgNSYuYkNSYvYzxeNSYemNSYuzubCNSYdrSYoSYdqSYkqizfhlepujtYtwegb'


def test_sting_four():
    assert missing('czpdvyhhunaqwpbxpjvwoqqoshunynjbeojhdvvpuyorhzch') == 'cFGIKLMTzpTdFGIKLMTvyhIKLMThunTaFGIKLMTqTwpbFGIKLMTxpjKLMTvwoTqqosThunynjbeFGIKLMTojhdvvpuyorThzch'
