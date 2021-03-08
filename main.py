from word_games.games import commands
from word_games import cmd_input


def main():
    game_options = {
        "ANAGRAM": cmd_input.Option("Play the anagram game.", commands.AnagramGame()),
        "Q": cmd_input.Option("Quit", commands.Quit()),
    }

    cmd_input.print_options(game_options)

    chosen_game = cmd_input.choose_option(game_options)

    chosen_game.run()


if __name__ == "__main__":
    main()
