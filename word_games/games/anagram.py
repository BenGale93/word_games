from collections import Counter


class Dictionary:
    def __init__(self, word_list: list[str]) -> None:
        self.word_list = [word.lower() for word in word_list]

    def compute_anagrams(self, input_str: str, target_length: int = None) -> set[str]:
        """Computes all anagrams of the input string

        Args:
            input_str: A string, which could be a word or jumbled set of letters,
            anagrams should be computed for.
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

        input_counts = Counter(input_str)
        output = set()

        for word in self.word_list:
            word_counts = Counter(word)
            check = []
            for letter, count in word_counts.items():
                if count <= input_counts[letter]:
                    check.append(True)
                else:
                    check.append(False)

            if all(check) and len(word) == target_length:
                output.add(word)

        return output
