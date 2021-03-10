import sys

from abc import ABC, abstractmethod

from . import anagram
from word_games import cmd_input


class Game(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError("Commands must implement an execute method")


class AnagramGame(Game):
    def run(self):
        while True:
            dict_path = cmd_input.get_usr_input("Input the dictionary location:")

            try:
                with open(dict_path, "r") as f:
                    file_contents = f.read()
                break
            except FileNotFoundError:
                print("File not found, try again.")

        word_list = file_contents.split("\n")

        full_dict = anagram.Dictionary(word_list)

        while True:
            input_str = cmd_input.get_usr_input(
                "Input the string you want to find anagrams of:", str
            )
            target_length = cmd_input.get_usr_input(
                "Input the length of the output words you would like:", int
            )
            reusable = cmd_input.get_usr_input(
                "Input the letters from the original string you'd like to repeat:", str
            )
            try:
                result = full_dict.compute_anagrams(input_str, target_length, reusable)
            except ValueError:
                print(
                    "At least one of the letters you'd like to repeat couldn't "
                    "be found in the original string."
                )
                continue

            if not result:
                print("No anagrams of that length.")
            else:
                print(result)


class Quit(Game):
    def run(self):
        sys.exit()
