import pytest

from word_games.games import anagram


def test_compute_anagrams():
    test_word_list = ["tell", "set", "board", "Test"]
    full_dict = anagram.Dictionary(test_word_list)
    result = full_dict.compute_anagrams("llet")
    expected = set(["tell"])
    assert expected == result


def test_invalid_input():
    test_word_list = ["let", "set", "board", "Test"]
    full_dict = anagram.Dictionary(test_word_list)
    with pytest.raises(TypeError):
        full_dict.compute_anagrams(["test"])


def test_target_length():
    test_word_list = ["tell", "set", "board", "Test"]
    full_dict = anagram.Dictionary(test_word_list)
    result = full_dict.compute_anagrams("sett", 3)
    expected = set(["set"])
    assert expected == result


def test_wildcard():
    test_word_list = ["dee", "see", "tho", "the", "ono"]
    full_dict = anagram.Dictionary(test_word_list)
    result = full_dict.compute_anagrams("H**", 3)
    expected = set(["tho", "the"])
    assert expected == result
