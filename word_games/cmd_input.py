import sys
from typing import Any, Callable


def q_to_exit(string):
    if string == "Q":
        sys.exit()


def get_usr_input(prompt: str, input_type: Callable[[str], Any] = str) -> str:
    while True:
        result = input(f"{prompt} (Type Q to exit) ")
        q_to_exit(result)
        try:
            result = input_type(result)
            break
        except Exception:
            print("Incorrect input type, please try again.")
    return result


def print_options(options):
    for k, v in options.items():
        print(f"{k} {v}")


def choose_option(options):
    while True:
        usr_input_str = input(
            "Type the name of the game you would like to play, or Q to quit. "
        )
        try:
            chosen_option = options[usr_input_str.upper()]
            break
        except KeyError:
            print("Invalid option, please choose again.")

    return chosen_option


class Option:
    def __init__(self, name, command):
        self.name = name
        self.command = command

    def __str__(self):
        return self.name

    def run(self):
        self.command.run()
