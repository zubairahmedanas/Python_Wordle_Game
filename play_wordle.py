from typing import List

from letter_state import LetterState
from wordle import Wordle
from colorama import Fore
import random


def main():
    # print("hello")
    word_set = load_word_set("/home/zubair/game/new_word.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)

    while wordle.can_attempt:
        x = input("\nType your word: ")

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.LIGHTRED_EX
                  + f"Word must be {wordle.WORD_LENGTH} character"
                  + Fore.RESET
                  )
            continue

        # print(word_set)
        if not x.upper() in word_set:
            print(
                Fore.RED
                + f"{x} is not a valid word!"
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
        print("you have failed...!!!")
        print(f"the secret word is : {wordle.secret}")


def display_result(worlde: Wordle):
    print("\nyour result so far...")
    print(f"You have {worlde.reamining_attempts} attempts remaining")
    lines = []
    for word in worlde.attempts:
        result = worlde.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)
    for _ in range(worlde.reamining_attempts):
        lines.append(" ".join(["_"] * worlde.WORD_LENGTH))
    draw_border_around(lines)


def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


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
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)
    for line in lines:
        print("│" + space + line + space + "│")
    print(bottom_border)


if __name__ == "__main__":
    main()
