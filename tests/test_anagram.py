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


def test_reusable_letters():
    test_word_list = ["test"]
    full_dict = anagram.Dictionary(test_word_list)
    result = full_dict._reusable_letters("help", 3, "h")
    expected = "ehhhlp"
    assert expected == result


def test_reusable_letters_input_multiple():
    test_word_list = ["test"]
    full_dict = anagram.Dictionary(test_word_list)
    result = full_dict._reusable_letters("hell", 3, "l")
    expected = "ehlll"
    assert expected == result


def test_multiple_reusable_letters():
    test_word_list = ["test"]
    full_dict = anagram.Dictionary(test_word_list)
    result = full_dict._reusable_letters("help", 3, "he")
    expected = "eeehhhlp"
    assert expected == result


def test_reusable_letters_error():
    test_word_list = ["test"]
    full_dict = anagram.Dictionary(test_word_list)
    with pytest.raises(ValueError):
        full_dict._reusable_letters("help", 3, "brp")


def test_reusable_letters_full():
    test_word_list = ["tools", "sloth", "help", "python"]
    full_dict = anagram.Dictionary(test_word_list)
    result = full_dict.compute_anagrams("tolsh", 5, "o")
    expected = set(["tools", "sloth"])
    assert expected == result
