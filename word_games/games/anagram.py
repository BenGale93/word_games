from collections import Counter


class Dictionary:
    def __init__(self, word_list: list[str]) -> None:
        self.word_list = [word.lower() for word in word_list]

    def compute_anagrams(
        self, input_str: str, target_length: int = None, reusable: str = None
    ) -> set[str]:
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

        input_str = self._clean_input(input_str)

        if target_length is None:
            target_length = len(input_str)

        if reusable is not None:
            reusable = self._clean_input(reusable)
            input_str = self._reusable_letters(input_str, target_length, reusable)

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
                    break

            if all(check):
                output.add(word)

        return output

    @staticmethod
    def _reusable_letters(input_str: str, target_length: int, reusable: str) -> str:
        """Extends the input string with the a set of reusable letters. Each
        letter is added to the string so that the total number of that letter
        is equal to target_length.

        Args:
            input_str: A string, which could be a word or jumbled set of letters,
            target_length: Number of times the reusable letters will appear in
                the output string.
            reusable: A string containing the letters to repeat

        Raises:
            ValueError: If the letters specified in "reusable" cannot be found in
                "input_str".

        Returns:
            Modified string.
        """
        reusable = set(reusable)
        unique_letters = set(input_str)
        all_letters = list(input_str)
        letter_counter = Counter(input_str)

        excess_letters = reusable - unique_letters
        if excess_letters:
            raise ValueError(
                "The letters specified as reusable do not all appear in the input string."
            )

        for letter in reusable:
            count = letter_counter[letter]
            for i in range(count, target_length):
                all_letters.append(letter)

        return "".join(sorted(all_letters))

    @staticmethod
    def _clean_input(string):
        string = string.lower()
        return "".join(e for e in string if e.isalpha() or e == "*")
