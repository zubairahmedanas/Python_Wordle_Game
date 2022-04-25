from typing import List

from letter_state import LetterState
from wordle import Wordle
from colorama import Fore


def main():
    # print("hello")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("\nType your word: ")

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.LIGHTRED_EX
                  + f"Word must be {wordle.WORD_LENGTH} character"
                  + Fore.RESET
                  )

            continue

        wordle.attempt(x)
        # result = wordle.guess(x)
        # print(*result, sep="\n")
        display_result(wordle)
    if wordle.is_solved:
        print("You have solve it")
    else:
        print("you failed...!!!")


def display_result(worlde: Wordle):
    print("\nyour result so far...")
    print(f"You have {worlde.reamining_attempts} attempts remaining")
    lines = []
    for word in worlde.attempts:
        result = worlde.guess(word)
        colored_result_str = convert_result_to_color(result)
        print(colored_result_str)
    for _ in range(worlde.reamining_attempts):
        print(" ".join(["_"] * worlde.WORD_LENGTH))
    draw_border_around(lines)


def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.RED
        elif letter.is_in_word:
            color = Fore.GREEN
        else:
            color = Fore.WHITE
        colered_letter = color + letter.character + Fore.RESET

        result_with_color.append(colered_letter)
    return " ".join(result_with_color)


def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"

    print(top_border)


if __name__ == "__main__":
    main()
