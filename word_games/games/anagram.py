from collections import Counter


class Dictionary:
    def __init__(self, word_list: list[str]) -> None:
        self.word_list = [word.lower() for word in word_list]

    def compute_anagrams(self, input_str: str, target_length: int = None) -> set[str]:
        """Computes all anagrams of the input string

        Args:
            input_str: A string, which could be a word or jumbled set of letters,
            anagrams should be computed for. Use * for wildcard characters.
            target_length: Specifies the target length of the output anagrams.
                Default to None which results in anagrams that match the length of
                input_str.

        Raises:
            TypeError: If the input is not a string.

        Returns:
            A set of anagrams which are contained within the input string.
        """
        if not isinstance(input_str, str):
            raise TypeError(f"input_str: {input_str} is not a string.")

        if target_length is None:
            target_length = len(input_str)

        input_str = input_str.lower()

        output = set()
        wilcard_temp = Counter({"*": 1})

        for word in self.word_list:
            if len(word) != target_length:
                continue
            input_counts = Counter(input_str)
            check = []
            for letter in word:
                if input_counts[letter] > 0:
                    check.append(True)
                    input_counts = input_counts - Counter(letter)
                elif input_counts["*"] > 0:
                    check.append(True)
                    input_counts = input_counts - wilcard_temp
                else:
                    check.append(False)

            if all(check):
                output.add(word)

        return output
